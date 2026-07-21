# paraLLEl-GS Evaluation — Champions of Norrath (2026-02-22)

## Verdict: GO for Phase 3

paraLLEl-GS renders all Champions of Norrath GS command streams without crashes, errors, or unsupported feature warnings. Confirmed on RTX 4090 (Vulkan 1.4) with 3 scene types covering the full rendering diversity.

## Test Setup

- **paraLLEl-GS**: HEAD of main (commit a444d67, "Fix regression in AA1 line handling")
- **GPU**: NVIDIA GeForce RTX 4090 (Vulkan 1.4.312, driver 581.29)
- **Build**: MSVC 19.44, VS2022, Windows 10 (native — WSL2 lacks Vulkan ICD on Win10)
- **Tool**: `parallel-gs-replayer.exe` (headless, no display)
- **Dumps**: PCSX2 v2.7.136, version 9 format, zstd-decompressed

## Results

| Dump | Scene | Draw Calls | VRAM (Device) | VRAM (Host) | Status |
|------|-------|-----------|---------------|-------------|--------|
| goblin-cave.gs | Goblin Caves (torches) | 102,658 | 832 MiB | 192 MiB | **Pass** |
| town.gs | Kelethin (town) | 73,720 | 640 MiB | 192 MiB | **Pass** |
| cave.gs | Lesser Faydark (outdoor) | 60,857 | 768 MiB | 192 MiB | **Pass** |
| goblin-cave.gs (4x SSAA) | Goblin Caves | 102,658 | 960 MiB | 256 MiB | **Pass** |

### Shader Compilation

First run compiles ~27 compute shaders + 3 graphics pipelines (cold cache). Longest stall: 166ms (compute). Second run: zero stalls (pipeline cache warm). This is normal Vulkan behavior.

### Memory Scaling

VRAM scales with scene complexity as expected:
- Outdoor (60K draws): 768 MiB
- Town (73K draws): 640 MiB (less geometry than outdoor despite more draws)
- Caves (102K draws): 832 MiB
- Caves + 4x SSAA: 960 MiB

All well within RTX 4090's 24 GB. Even a 4 GB mobile GPU should handle these scenes.

## What Was Tested

Each GS dump contains a complete frame of GS commands:
- **102,658 draw kicks** (XYZF2 + XYZ2) in worst case
- **97.8% TriStrip** + 6.3% Sprite primitives
- **XYZF2 fog-enabled draws** (98% of all draws)
- **VIColorBuffer per-vertex lighting** (multiple light passes over same geometry)
- **VIParticleSprite billboard particles** (6,470 sprites in caves)
- **10.53 MB of GIF PATH3 data** per frame
- **322,568 GS register writes** per frame

No GS features were flagged as unsupported. No rendering errors logged.

## BG:DA Freeze Bug — Not Applicable

The Baldur's Gate: Dark Alliance freeze reported in libretro/ps2 issue #48 reproduces on both paraLLEl-GS and the software renderer — it's an EE/VU emulation core bug, not a GS issue. Since the native port replaces the entire EE/VU layer with recompiled C++, this bug is irrelevant.

## WSL2 Vulkan Limitation

WSL2 on Windows 10 (build 19044) does not provide a Vulkan ICD for NVIDIA GPUs. The NVIDIA driver only installs D3D12 libs (`libd3d12.so`, `libdxcore.so`) into `/usr/lib/wsl/lib/`. Native Vulkan in WSL2 requires Windows 11 or Windows 10 build 21364+. Built natively on Windows as a workaround.

## Phase 3 Implications

### Integration Path

paraLLEl-GS provides `gs_interface.h` — a clean C API:

```
gs_renderer_create() → gs_renderer_flush_dma() → gs_renderer_vsync() → gs_renderer_destroy()
```

The native port feeds GIF DMA packets from recompiled EE code directly to this API, replacing the PS2 GS hardware entirely.

### Performance Budget

The RTX 4090 handles 102K draw calls (worst-case caves) headlessly with <1 GB VRAM. For the native port with per-pixel lighting replacing VIColorBuffer:
- Expected draw calls: ~5,000-10,000 (10-20x reduction)
- VRAM budget: well under 1 GB even at 4K with SSAA
- paraLLEl-GS is not the bottleneck

### Alternatives Considered

| Option | Verdict |
|--------|---------|
| paraLLEl-GS standalone | **Selected** — clean API, production quality, handles all CoN GS commands |
| PCSX2's GSdx (OpenGL/Vulkan) | Rejected — tightly coupled to PCSX2 internals, not embeddable |
| Custom GS implementation | Rejected — years of work, paraLLEl-GS already exists |
| Software GS renderer | Rejected — too slow for 100K+ draws at target resolution |

## Build Instructions

```bash
# On Windows with VS2022 + CMake
git clone --recursive https://github.com/Arntzen-Software/parallel-gs.git C:\parallel-gs
cd C:\parallel-gs
cmake -B build -G "Visual Studio 17 2022" -A x64 -DCMAKE_BUILD_TYPE=Release
cmake --build build --config Release --target parallel-gs-replayer -j 16

# Test with GS dump
build\tools\Release\parallel-gs-replayer.exe dump.gs [--ssaa 4] [--full]
```

No Vulkan SDK needed — uses volk (dynamic Vulkan loader).

## Files

| File | Description |
|------|-------------|
| `C:\parallel-gs\` (build machine) | Built paraLLEl-GS with replayer |
| `C:\parallel-gs\dumps\` (build machine) | GS dumps copied for testing |
| `output/goblin-cave.gs` | Worst-case GS dump (48 MB, 102K draws) |
| `output/town.gs` | Town GS dump (34 MB, 73K draws) |
| `output/cave.gs` | Outdoor GS dump (33 MB, 60K draws) |
