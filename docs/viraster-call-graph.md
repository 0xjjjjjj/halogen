# VIRaster Rendering Pipeline — Call Graph Analysis

Extracted from PS2Recomp C++ output of Champions of Norrath (SLUS-20565).

## Core Render Loop

```
BeginScene
├── sceGsResetGraph          ← Reset GS hardware
├── sceGsSyncV (loop)        ← Wait for VSync (loops for Hz switching!)
├── sceGsSwapDBuffDc         ← Swap double buffer with display context
└── SetGSScissoring          ← Set clip rectangle

EndScene
├── Flush                    ← Submit pending DMA
│   ├── FlushCache           ← CPU cache writeback
│   ├── VIEEDMASend          ← DMA transfer to GS
│   └── VIEEDMASync          ← Wait for DMA completion
├── Flip                     ← Display buffer swap
│   ├── sceGsSyncV           ← VSync wait
│   ├── sceGsSyncPath        ← Wait for GS pipeline drain
│   └── sceGsSwapDBuffDc     ← Swap display buffer
└── ReleaseDeferred          ← Free resources queued during frame
```

## VU1 Microcode Upload System

```
UploadRasterMicro            ← Uploads VU1 microcode for geometry processing
UploadBillboardMicro         ← Billboard-specific VU1 program
UploadMatrices               ← Uploads transform matrices via sceVu0CopyMatrix
UploadPreTrans               ← Pre-translation offsets (zone streaming!)
UploadPerMaterial            ← Per-material GS state
```

**Key insight**: Multiple VU1 microprograms exist — at least `RasterMicro` (general geometry) and `BillboardMicro` (billboards). These are swapped dynamically per draw call type.

## Material/DMA Pipeline

```
SetMaterial(id)
├── AddMaterial(id, dmaTag**)
│   ├── VIPool<VIRasterMaterialLRU>::Begin/MoveToLast  ← LRU cache!
│   ├── VIEESurfCache::Cache                            ← Surface/texture cache
│   ├── VIMaterial::ConstructDMAPacket                  ← Build GIF tags
│   │   ├── ConstructTextPass       ← Textured pass (uses GetZBufferReg)
│   │   ├── ConstructSolidFillPass  ← Solid fill pass
│   │   └── ConstructWirePass       ← Debug wireframe
│   ├── SetGSDitherMatrix           ← Dithering for 16-bit color
│   └── UploadPerMaterial           ← Upload to GS
└── FlushDMABufferIfFull
    ├── FlushCache
    ├── VIEEDMASend                 ← DMA to GS
    ├── VIEEDMASync                 ← Wait for transfer
    └── Flip (if buffer full!)      ← Force flip if DMA overflows!
```

**Key insight**: Materials use an **LRU cache** (`VIRasterMaterialLRU`). When cache is full, oldest material is evicted. `VIEESurfCache` handles texture/surface caching to EDRAM. This is the texture streaming system that Fast Texture Invalidation affects.

## Drawing Primitives

```
DrawPrimBuffer(id, flags)
├── UploadRasterMicro                ← Ensure correct VU1 program loaded
└── DrawPrimBufferPackVU variants:
    ├── DrawPrimBufferPackVU          ← Standard vertex format
    ├── DrawPrimBufferPackVUNC        ← Normal + Color vertex format
    ├── DrawPrimBufferPackVUNCG       ← Normal + Color + Gouraud
    │   ├── UploadPreTrans            ← Zone pretranslation!
    │   └── DrawPrimBufferTessPackVUNCG ← Tessellated variant
    │       └── TessTriangle → RasterTess::Tessellate
    ├── DrawPrimBufferPackVUNBW       ← Normal + Bone Weights (skinned mesh)
    └── DrawPrimBufferVUNC            ← Direct VU NC (no packing?)

    All variants call:
    ├── AddMaterial                   ← Material/texture setup
    ├── CalcMatrices                  ← MVP calculation
    │   ├── InvertAffine(Matrix44)
    │   ├── Mul(Matrix44, Matrix44)
    │   ├── Normalize(Vect3)
    │   └── SubMatrixMul(Matrix44, Vect3)
    ├── FlushDMABufferIfFull          ← DMA management
    └── UploadMatrices                ← Send matrices to VU1
```

**Key insight**: Multiple vertex formats exist:
- **PackVU** — standard textured geometry
- **PackVUNC** — normal + color (lit geometry)
- **PackVUNCG** — normal + color + gouraud (world geometry with pretranslation)
- **PackVUNBW** — normal + bone weights (character meshes)
- **VUNC** — direct VU (no CPU-side packing, VU1 handles everything)

## 2D Rendering

```
Begin2D
├── UploadRasterMicro           ← Switch to 2D VU1 program
├── Store2D (save 3D state)     ← sceVu0CopyMatrix
├── Identity(Matrix44)          ← Reset transform
└── sceVu0CopyMatrix            ← Upload identity to VU0

End2D
└── Restore2D                   ← sceVu0CopyMatrix (restore 3D state)
```

## Billboard System

```
BeginBillboards(billboard*, count)
├── CalcMatrices
├── Material(id)                ← Set billboard material
├── Mul(Matrix44)               ← Orient to camera
├── UploadBillboardMicro        ← Special VU1 program for billboards
└── FlushDMABufferIfFull

EndBillboards
└── FlushDMABufferIfFull
```

## Particle Rendering

```
VIParticleSystem::Render(raster)
├── BeginBillboards             ← Particles are billboards!
├── SetMaterial                  ← Per-particle-type material
├── Mul(Vect3)                   ← Position each particle
├── Normalize(Vect3)             ← Face camera
└── EndBillboards

VIParticleSprite::Raster(camera, scene, raster)
├── Update(ParticleEmitter)      ← Tick particle simulation
├── SetDirection/SetLocation     ← Update emitter transform
├── SetSpace(Matrix44)           ← Coordinate space
├── Purge(ParticleEmitter)       ← Remove dead particles
└── RasterUISprite               ← Render sprite in scene
```

## Lighting & Effects

```
VILightning::Render(raster)          ← Lightning bolt VFX
├── SetMaterial
└── RenderBoltVertices               ← Triangle strip bolt geometry
    ├── BeginTriStrip
    ├── Color / UV / Vertex          ← Per-vertex attributes
    └── EndTriStrip

VITrailFx::Render(raster, camera)    ← Weapon trail VFX
├── SetMaterial
├── SetModelView(Matrix44)
├── BeginTriStrip
├── Color / Vertex                   ← Trail vertices
└── EndTriStrip
```

## Resource Management

```
Init(VIRaster)
├── sceGsResetGraph              ← Reset GS
├── sceGsSetDefDBuffDc           ← Setup double buffer display context
├── InitDMADoubleBuffer          ← Allocate DMA double buffer
├── InitSPRDoubleBuffer          ← Scratchpad double buffer
├── InitMaterialLRU              ← Material cache (LRU eviction)
├── InitGSRegisters              ← Configure GS hardware state
├── CreateDefaultResources       ← Default materials (solid fill, blend modes)
├── UploadRasterMicro            ← Initial VU1 program upload
├── SetClipAndLight              ← Clip planes + light setup
├── SetDefaultLights             ← Ambient/directional lights
└── SetFog                       ← Fog parameters

Clear(VIRaster)                  ← Complete resource teardown
├── ClearDMADoubleBuffer
├── ClearMaterialLRU
├── VIPool/VIList::Clear for:
│   ├── VIPrimBuffer             ← Vertex buffers
│   ├── VISurface                ← Texture surfaces
│   ├── VIColorBuffer            ← Color buffers (RTT targets!)
│   ├── VIMaterialPal            ← Material palettes
│   └── VIRFont                  ← Fonts
```

## SCE SDK Calls (Hardware Interface)

| Function | Purpose |
|----------|---------|
| `sceGsResetGraph` | Reset Graphics Synthesizer hardware |
| `sceGsSetDefDBuffDc` | Setup double buffer display context |
| `sceGsSwapDBuffDc` | Swap display/draw buffers |
| `sceGsSyncV` | Wait for vertical sync |
| `sceGsSyncPath` | Wait for GS pipeline to drain |
| `sceVu0CopyMatrix` | Copy 4x4 matrix to VU0 data memory |
| `FlushCache` | CPU data cache writeback |
| `AddDmacHandler` | Register DMA interrupt handler |
| `EnableDmac` / `DisableDmac` | DMA channel control |

## Key Architectural Findings

1. **VU1 microcode is swappable** — `UploadRasterMicro` and `UploadBillboardMicro` are separate programs. At least 2 VU1 programs, likely more for different vertex formats.

2. **Material LRU cache** — `VIRasterMaterialLRU` with `MoveToLast` pattern confirms LRU eviction. Materials are expensive to upload (DMA packet construction + texture cache), so the engine keeps recently used ones hot.

3. **DMA double buffering** — Engine maintains two DMA buffers. While GS processes one, CPU fills the other. `FlushDMABufferIfFull` can trigger a `Flip` if the current buffer is full — meaning a single frame can span multiple DMA submissions.

4. **Pretranslation system** — `UploadPreTrans` and `SetPreTranslations` in VIZone — the zone streaming system uses pretranslation offsets to avoid floating point precision loss. Each zone has its own origin, and vertices are translated relative to it.

5. **Tessellation** — `VIRasterTess` with `TessTriangle` and `Split` operations. The engine can tessellate triangles at runtime, likely for large terrain polygons near the camera.

6. **VIColorBuffer = RTT targets** — `CreateColorBuffer`, `Lock`, `GetNextColorBuffer` — these are render-to-texture targets. Confirms the RTT hypothesis for dynamic lighting/shadows.

7. **Particles are billboards** — `VIParticleSystem::Render` uses `BeginBillboards/EndBillboards`. Each fire particle is a camera-facing quad submitted as a billboard. In caves with many torches, this means hundreds of billboards + their associated point lights.

8. **Debug infrastructure exists** — `DebugEEMicro` calls `VIEEDebugVU1Memory` — the engine has VU1 debugging support built in. `DebugResources` prints all active resource counts.
