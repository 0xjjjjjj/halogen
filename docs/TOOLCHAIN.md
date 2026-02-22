# Halogen Toolchain Setup

Environment setup for Snowblind Engine reverse engineering.

## Prerequisites

- Linux (WSL2 fine) or macOS
- Git, CMake 3.20+, C++20 compiler (GCC 11+ or Clang 13+)
- Python 3.11+
- Rust (for future binary analysis tools)
- Java 17+ (for Ghidra)
- Vulkan SDK (for paraLLEl-GS)

---

## 1. PS2Recomp

Static recompiler: PS2 ELF → C++.

```bash
git clone --recurse-submodules https://github.com/ran-j/PS2Recomp
cd PS2Recomp
mkdir build && cd build
cmake .. -DCMAKE_BUILD_TYPE=Release
make -j$(nproc)
```

Binary ends up at `build/ps2recomp` (or similar — check after build).

### Champions of Norrath config

`configs/champions-of-norrath.toml`:

```toml
# PS2Recomp config for Champions of Norrath (NTSC-U, SLUS-20565)
input = "BASLUS_20565.ELF"
output_dir = "output/champions-of-norrath/"

# Standard PS2 libc stubs
stubs = [
    "printf",
    "sprintf",
    "malloc",
    "free",
    "memcpy",
    "memset",
    "strlen",
    "strcmp",
]

skips = ["abort", "exit"]

# Single file for easier initial analysis
# Switch to multi-file once we know the structure
single_file = false
```

### Running recompilation

```bash
./build/ps2recomp configs/champions-of-norrath.toml
# Output: output/champions-of-norrath/
```

### What to look for in output

```bash
# Check for VU1 programs
readelf -S BASLUS_20565.ELF | grep -i "vudata\|vu1\|microcode"

# Check for debug symbols (huge win if present)
readelf -S BASLUS_20565.ELF | grep "mdebug\|debug"

# Count functions found
grep -c "^void \|^int \|^float " output/champions-of-norrath/*.cpp
```

---

## 2. Ghidra + ghidra-emotionengine-reloaded

Manual RE and symbol recovery.

### Install Ghidra

```bash
# Download from https://ghidra-sre.org/
# Requires Java 17+
sudo apt install openjdk-17-jdk  # or your distro equivalent
# Extract Ghidra, run ghidraRun
```

### Install ghidra-emotionengine-reloaded

This extension adds:
- Full MIPS R5900 / EE instruction set
- MMI (128-bit multimedia) instructions
- VU0 macro mode
- `.mdebug` section parsing (recovers original function names)
- PCSX2 save state import (for runtime analysis)

```bash
git clone https://github.com/chaoticgd/ghidra-emotionengine-reloaded
# See repo README for build + install instructions
# Targets Ghidra 11.3.2
```

### Loading a PS2 ELF

1. File → Import File → select `BASLUS_20565.ELF`
2. Format: ELF
3. Language: MIPS R5900 (provided by extension)
4. Let auto-analysis run
5. Check Symbol Table for debug symbols (Window → Symbol Table)

---

## 3. paraLLEl-GS

Vulkan compute-shader Graphics Synthesizer emulator. This replaces the GS in native builds. **Evaluated 2026-02-22**: all 3 CoN GS dumps pass cleanly (see `docs/parallel-gs-eval.md`).

### Build (Windows, native Vulkan required)

```bash
git clone --recursive https://github.com/Arntzen-Software/parallel-gs.git C:\parallel-gs
cd C:\parallel-gs
cmake -B build -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --target parallel-gs-replayer -j 16
```

No Vulkan SDK needed — uses volk (dynamic loader). Requires Vulkan 1.2+ GPU with `descriptorIndexing`, `timelineSemaphore`, `shaderInt16`. Any desktop GPU from ~2018+ works.

**Note**: WSL2 on Windows 10 lacks Vulkan ICD for NVIDIA — build natively on Windows. Windows 11 WSL2 should work.

### Testing with GS dumps

```bash
# Basic replay (headless)
build\tools\Release\parallel-gs-replayer.exe dump.gs

# 4x SSAA + full mode
build\tools\Release\parallel-gs-replayer.exe dump.gs --ssaa 4 --full

# For visual inspection, launch from RenderDoc
```

Integration point: Phase 3. PS2Recomp output calls GS via GIF DMA packets. We intercept these and route to paraLLEl-GS via `gs_interface.h`.

Reference: [ps2tek GS documentation](https://psi-rockin.github.io/ps2tek/)

---

## 4. PCSX2 (Runtime Tracing)

PCSX2 for GS dump capture and runtime analysis. Installed as portable (no installer).

### Setup (Windows — sleeper5)

```
# Already installed at C:\pcsx2\pcsx2-qt.exe (v2.7.136 nightly)
# Portable .7z extract, no registry changes
```

### Configuration

1. First launch: Settings → BIOS → point to your PS2 BIOS folder
2. Settings → Game List → add folder containing `Champions of Norrath (USA).iso`
3. Boot the game, verify it reaches in-game

### GS Dump Capture

1. Navigate to target scene in-game
2. Press **Shift+F8** to capture single-frame GS dump
3. Dumps land in `C:\pcsx2\snaps\` as `.gs` + `.png` files
4. Copy dumps to local machine for analysis

Two scenes needed:
- **Cave with torches** — bottleneck case (VIPointLight overdraw, VIColorBuffer passes)
- **Outdoor/town** — normal rendering (VIAtmosphere, VIWorld streaming)

### GS Dump Analysis

```bash
# Human-readable report
python3 tools/parse-gs-dump.py dump.gs

# JSON output
python3 tools/parse-gs-dump.py dump.gs --json

# Verbose (every GIFTag)
python3 tools/parse-gs-dump.py dump.gs -v

# Generate synthetic test dump
python3 tools/parse-gs-dump.py --create-test-dump test.gs
```

Output includes: draw call count, primitive type histogram, GS register write frequency, per-path transfer sizes, texture upload stats.

### VU1 Microcode Extraction

```bash
# Extract VU1 programs from ELF DVP overlay sections
python3 tools/extract-vu1.py bin/SLUS_205.65

# Verbose (hex instruction listing)
python3 tools/extract-vu1.py bin/SLUS_205.65 -v

# Custom output directory
python3 tools/extract-vu1.py bin/SLUS_205.65 -o output/vu1
```

Extracts 2 VU1 programs (RasterMicro + BillboardMicro) from 18 DVP overlay sections. Output to `output/vu1/` with raw binaries, assembled programs, and analysis.

---

## 5. Python Analysis Stack

Scripts in `tools/`:
- `parse-gs-dump.py` — PCSX2 GS dump parser (draw calls, primitives, register writes)
- `extract-vu1.py` — VU1 microcode extraction from ELF DVP overlay sections
- `parse-dwarf1-types.py` — DWARF1 struct layout parser (Demon Stone prototype)
- `map-types.py` — Cl* → VI* type mapping (Demon Stone → CoN)
- `ghidra-batch-decompile.py` — Jython script for Ghidra headless batch decompilation
- `ghidra-apply-types.py` — Apply struct types to Ghidra project
- `ghidra-retype-params.py` — Retype function `this` pointers in Ghidra
- `pcsx2_hacks.py` — Parse PCSX2 GameDatabase for CoN entries

---

## 6. Rust Analysis Stack (future — Phase 2+)

For performance-critical binary processing.

```bash
rustup update stable

# Planned crates:
# goblin   - ELF/PE/Mach-O parsing
# capstone - Disassembly
```

---

## Workflow (when binary is available)

```bash
# 1. Extract ELF from ISO
7z x champions-of-norrath.iso -o./extracted/
# or: isoinfo -i champions-of-norrath.iso -x /SYSTEM.CNF\;1

# 2. Check disc structure
cat extracted/SYSTEM.CNF    # finds the boot ELF path
ls extracted/               # locate BASLUS_20565.ELF

# 3. Check for debug symbols (the big question)
readelf -S extracted/BASLUS_20565.ELF | grep "mdebug"

# 4. Run PS2Recomp
./PS2Recomp/build/ps2recomp configs/champions-of-norrath.toml

# 5. Open in Ghidra with EE extension
# File → Import → BASLUS_20565.ELF

# 6. Cross-reference: PS2Recomp C++ output ↔ Ghidra disassembly
# Build a map: address → function name → purpose
```

---

## References

- [PS2Recomp](https://github.com/ran-j/PS2Recomp)
- [ghidra-emotionengine-reloaded](https://github.com/chaoticgd/ghidra-emotionengine-reloaded)
- [paraLLEl-GS](https://github.com/Arntzen-Software/parallel-gs)
- [ps2tek — PS2 hardware reference](https://psi-rockin.github.io/ps2tek/)
- [retroreversing.com/ps2](https://www.retroreversing.com/ps2)
