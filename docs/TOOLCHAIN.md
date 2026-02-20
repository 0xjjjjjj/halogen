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

Vulkan compute-shader Graphics Synthesizer emulator. This replaces the GS in native builds.

```bash
git clone https://github.com/Arntzen-Software/parallel-gs
# Follow repo build instructions
# Requires Vulkan SDK
```

Integration point: Phase 3. PS2Recomp output calls GS via GIF DMA packets. We intercept these and route to paraLLEl-GS instead.

Reference: [ps2tek GS documentation](https://psi-rockin.github.io/ps2tek/)

---

## 4. Python Analysis Stack (future — Phase 1.5+)

When we have the binary, we'll build Python scripts for:

```bash
# Install analysis libs
pip install lief capstone construct pyelftools

# lief      - ELF parsing, section analysis
# capstone  - MIPS R5900 disassembly
# construct - Binary format parsing (GIF tags, VIF packets)
# pyelftools - ELF utilities
```

Planned scripts in `tools/`:
- `elf_info.py` — ELF sections, symbols, entry point
- `sym_dump.py` — Extract .mdebug symbols
- `vu_extract.py` — Extract .vudata VU1 programs
- `pcsx2_hacks.py` — Parse PCSX2 GameDatabase for CoN entries

---

## 5. Rust Analysis Stack (future — Phase 2+)

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
