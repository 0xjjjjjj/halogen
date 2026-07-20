# Modified paraLLEl-GS replayer with PNG dump

The upstream `parallel-gs-replayer.exe` requires RenderDoc to actually see any
rendered output.  For headless-halogen workflow we need a way to inspect what
the recompiled engine emits without launching a GUI capture tool.

`parallel-gs-replayer-png-patch.cpp` is a patch of `tools/gs_dump_replayer.cpp`
in the paraLLEl-GS repo that adds:

- `--dump-png OUT_DIR` CLI flag
- After each `parser.iterate_until_vsync`, calls `consume_vsync_result()`.
- If a scanout image is available (`sr.image` non-null), copies it back to
  CPU via `Granite::save_image_to_cpu_buffer` and writes as PNG via
  `stbi_write_png`.
- Fallback: if no scanout image (game hasn't set up priv registers yet),
  dumps raw VRAM as 1024x1024 RGBA PNG every 5th frame.  Reveals texture
  atlases and framebuffer contents even without a proper scanout config.

## Build (Windows, from WSL bash)

Requires MSVC BuildTools v143 at the standard path.  The Enterprise install
has only v170 headers, not the v143 toolset — cmake-generated .vcxproj files
target v143.

```bash
cp tools/parallel-gs-replayer-png-patch.cpp /mnt/c/parallel-gs/tools/gs_dump_replayer.cpp
cat > /mnt/c/parallel-gs/build/rebuild-replayer.bat << 'BAT'
@echo off
call "C:\Program Files (x86)\Microsoft Visual Studio\2022\BuildTools\VC\Auxiliary\Build\vcvarsall.bat" x64
cd /d C:\parallel-gs\build
msbuild tools\parallel-gs-replayer.vcxproj /p:Configuration=Release /p:Platform=x64 /p:BuildProjectReferences=false /m /verbosity:minimal
BAT
/mnt/c/Windows/System32/cmd.exe /c 'C:\parallel-gs\build\rebuild-replayer.bat'
```

## Run

```bash
mkdir -p /mnt/c/parallel-gs/dumps/pngs
HALOGEN_GS_DUMP=/mnt/c/parallel-gs/dumps/halogen.gs \
  ./halogen-headless --cd-root bin/disc bin/disc/SLUS_205.65
/mnt/c/parallel-gs/build/tools/Release/parallel-gs-replayer.exe \
  'C:\parallel-gs\dumps\halogen.gs' --iterations 1 --dump-png 'C:\parallel-gs\dumps\pngs'
```

## Known issues

- `sr.image` is null because our GS dump writes zeroed priv-register state
  (we don't intercept the game's DISPFB1/DISPLAY1 writes).  Only the VRAM
  fallback fires.
- Windows-native argv paths (`C:\...`) required — `/mnt/c/...` fails
  silently after RenderDoc-load error.
