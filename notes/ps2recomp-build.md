# PS2Recomp Build Notes

## Status: Built successfully (2026-02-20)

## Binaries

| Binary | Path | Size |
|--------|------|------|
| ps2_recomp | `vendor/PS2Recomp/build/ps2xRecomp/ps2_recomp` | ~1.3M |
| ps2_analyzer | `vendor/PS2Recomp/build/ps2xAnalyzer/ps2_analyzer` | ~1.3M |
| ps2x_tests | `vendor/PS2Recomp/build/ps2xTest/ps2x_tests` | ~4.3M |

Usage: `ps2_recomp <config.toml>`

## Build on NixOS

```bash
nix-shell -p cmake gcc gnumake pkg-config \
  xorg.libX11 xorg.libX11.dev \
  xorg.libXcursor xorg.libXcursor.dev \
  xorg.libXrandr xorg.libXrandr.dev \
  xorg.libXinerama xorg.libXinerama.dev \
  xorg.libXi xorg.libXi.dev \
  libGL libGL.dev \
  zlib zlib.dev \
  zstd zstd.dev \
  --run "cmake -B build -DCMAKE_BUILD_TYPE=Release && cmake --build build -j\$(nproc)"
```

## Patches Required

### 1. SSE4.1 flag missing (upstream bug)

PS2Recomp uses `_mm_extract_epi32` (SSE4.1) in public headers but doesn't set `-msse4.1` compile flag. On NixOS (where `-march=native` is blocked by `NIX_ENFORCE_NO_NATIVE`), this causes build failure.

**Fix applied in two places:**

`CMakeLists.txt` (top-level): Added `-msse4.1` for non-ARM, non-MSVC:
```cmake
else()
    # x86_64: SSE4.1 required for _mm_extract_epi32 in ps2_runtime headers
    if(NOT MSVC)
        add_compile_options(-msse4.1)
    endif()
endif()
```

`ps2xRuntime/CMakeLists.txt`: Added per-target SSE4.1 options (belt-and-suspenders).

**TODO:** File upstream PR for this fix.

## Dependencies (NixOS)

- cmake, gcc, gnumake
- pkg-config
- X11 libs (libX11, libXcursor, libXrandr, libXinerama, libXi) — for raylib
- libGL — for raylib OpenGL
- zlib, zstd — for DWARF/compression support
