# Snowblind Engine — Deep Subsystem Analysis

Extracted from PS2Recomp C++ output + ELF symbol table of Champions of Norrath (SLUS-20565).

## 1. Zone/World Streaming Architecture

### VIZone (63 methods, 34.2 KB)

The zone system is the Snowblind Engine's core spatial architecture — evolved from Slavedriver's flat `sSectorType` array into a hierarchical streaming system.

#### Data Structures

```
VIZone
├── VIZoneTree           ← BSP/spatial tree for visibility
│   ├── VIZoneNode[]     ← Interior tree nodes
│   └── VIZoneLeaf[]     ← Leaf nodes (renderable volumes)
├── VIZoneRoom[]         ← Individual rooms within the zone
│   └── VIBBox           ← Bounding box per room
├── VIResourceElem[]     ← Streamable resource references
├── VIVect3[]            ← Pre-translation vectors (one per zone)
├── VIZoneStaticTableElem[] ← Static geometry lookup
├── VIZoneRadialFlora    ← Flora system per zone
│   ├── VIRadialFloraSet[]
│   ├── VIRadialFloraDist[]
│   └── VIRadialFloraModel[]
└── IdentityMatrix       ← Static global (4x4 identity)
```

#### Rendering Pipeline

```
VIZone::RenderByVolume(nodeIndex, VISceneRendVars)
├── Check node flags (0xF0000000 mask → leaf detection)
├── Portal plane frustum test (dot product vs planes)
│   ├── If behind all planes → skip subtree
│   └── If visible → recurse children
├── RenderByVolume (left child)     ← RECURSIVE BSP traversal
├── RenderByVolume (right child)    ← RECURSIVE BSP traversal
└── RenderLeaf (at leaf node)       ← Actual room rendering
```

**Key finding**: `RenderByVolume` is a **recursive BSP traversal** — it recursively visits left/right children, testing each node against portal planes. The dot product + compare pattern at 0x1115688-0x11156A8 is a classic plane distance test. This is the *exact same pattern* as Slavedriver's sector visibility, now in 3D.

#### Collision System

The zone integrates deeply with collision:

```
VIZone::Collide(VISceneCollVars)
├── SetPreTranslations(VICollide, VIVect3*)  ← Pre-translate collision!
└── Collide(nodeIndex, VISceneCollVars)
    └── CollideLeaf → CollideRoom
        ├── SetWorld(VICollide, Matrix44)     ← Room transform
        ├── CollideActor(VIScene, ...)        ← Entity collision
        └── CollideSprite(VIScene, ...)       ← Sprite collision

VIZone::Pick(VIScenePickVars)
├── SetPreTranslations(VIRaster, VIVect3*, VIVect3) ← Pre-translate picks too!
└── Pick(nodeIndex, VIScenePickVars)
    └── PickLeaf → PickRoom
        ├── SetModelView(VIRaster, Matrix44)
        ├── PickActor(VIScene, PickSegment, ...)
        └── PickSprite(VIScene, PickSegment, ...)
```

**Key finding**: Pre-translation is used everywhere — rendering, collision, *and* picking all apply zone pre-translation offsets. This prevents floating-point precision loss far from the world origin.

#### Zone Loading

```
VIZone::Load(resourceId, zoneIndex, VILoader, flags)
├── Find(resourceId, &offset, &size)  ← Locate zone in resource file
└── VILoader::Load(zoneIndex, ...)     ← Async streaming load
```

#### Query System

VIZone supports multiple spatial query types, all following the same BSP traversal pattern:

| Query | Purpose |
|-------|---------|
| `QueryVisible` | Visibility determination (for rendering) |
| `QueryThroughPortals` | Portal-based visibility (indoor areas) |
| `QueryProximal` | Proximity queries (nearby actors) |
| `QueryVolume` | AABB intersection queries |
| `QueryIntersection` | Triangle-level intersection |
| `QueryEmitters` | Find particle/sound emitters in range |

---

## 2. Particle System (Performance Bottleneck)

### Architecture

```
VIParticleSystem (manages all particles globally)
├── VIParticleDefinition[] (pool)       ← Particle type templates
│   └── VIParticleDefinitionEx          ← Extended definition
│       ├── VIParticleMotif[]           ← Visual "looks" (blendable)
│       └── VIParticleAttributes        ← Per-motif physics/visuals
├── VIParticleEmitter[] (linked list)   ← Active emitter instances
│   └── VIParticleAttributes (current)  ← Interpolated from motifs
└── VIParticleSprite (scene graph node) ← Renderable sprite wrapper
```

### Particle Attributes (fully data-driven)

Each `VIParticleAttributes` contains:
- **Spawn**: Birthrate, BirthrateVar, DeltaSpawn, Lifespan, LifespanVar
- **Size**: StartSize, StartSizeVar, EndSize, EndSizeVar
- **Velocity**: Velocity, VelocityVar, InheritVelocity, Friction
- **Color**: StartColorVar, EndColorVar, GradientColor[], GradientRepeat
- **Direction**: NozzleAxis, NozzleHprVar, InnerHprVar, OuterHprVar
- **Offset**: InnerOffset, OuterOffset
- **Physics**: GravityOn
- **Visual**: Pattern[] (sprite sheet frames), BlendMode

### Motif Blending System

The engine supports **real-time interpolation between particle "looks"**:

```
VIParticleEmitter::BlendMotifs
├── VIParticleDefinitionEx::BlendMotifs(VIParticleAttributes*)
│   ├── Iterates VIParticleMotif pool
│   └── Interpolates all attributes between motifs
└── RecomputeStaticBBox
```

This is how fire transitions to smoke (motif A = flame, motif B = smoke, blend over particle lifetime).

### Rendering Path (THE BOTTLENECK)

```
VIParticleSprite::Raster(camera, scene, raster, flags)
├── GetModelView(VIRaster)              ← Get current view matrix
├── GetParticleUISprite(VIScene)        ← UI sprite for debug?
├── For each emitter:
│   ├── SetLocation(VIVect3)            ← Emitter world position
│   ├── SetDirection(VIMatrix33)        ← Emitter orientation
│   ├── SetSpace(VIMatrix44)            ← Coordinate space transform
│   ├── Update(VIParticleEmitter)       ← SIMULATE all particles
│   ├── Purge(VIParticleEmitter)        ← Remove dead particles
│   └── Magnitude(VIVect3)             ← Distance for LOD?
├── Transpose + Mul(Matrix44)           ← Camera-relative transform
├── SetModelView(VIRaster, Matrix44)    ← Upload transform
└── RasterUISprite(VIScene, ...)        ← Submit to renderer

VIParticleSystem::Render(count, VIRaster)   ← Called by VIRaster
├── BeginBillboards(VIRaster, ...)      ← START BILLBOARD MODE
├── For each live particle:
│   ├── SetMaterial(VIRaster, matId)    ← Per-particle-type material
│   ├── Mul(Matrix44, VIVect3)          ← Position in world
│   ├── Normalize(VIVect3)              ← Face camera
│   └── [submit billboard vertex]
├── EndBillboards(VIRaster)             ← END BILLBOARD MODE
└── Clean up dead emitters (RemHead/AddTail/Remove)
```

### Why Caves Are Slow

Each torch/fire in a cave:
1. Has a `VIParticleSprite` with an emitter
2. The emitter spawns N particles per frame (Birthrate)
3. Each particle is a **camera-facing billboard** (BeginBillboards)
4. Each particle has its own material setup (SetMaterial → LRU cache)
5. The fire also has a `VIPointLight` attached (Slavedriver heritage!)
6. The point light requires an **additional render pass** for affected geometry

With 10 torches × 20 particles × 2 passes (particle + light) = **400+ draw operations per frame** in a cave, all going through the DMA/GIF pipeline.

### VIParticleEmitter::Update (2856 bytes — largest particle function)

```
Update(VIParticleEmitter)
├── BlendMotifs                     ← Interpolate motif states
├── Distance(VIVect3, VIVect3)     ← Distance calculations
├── RotateHPR(VIVect3)             ← Heading/pitch/roll per particle
├── Mul(Matrix44, VIVect3)         ← Transform positions
├── TextureConfiguration           ← Animated texture frames
└── Linked list management          ← Live/dead particle pools
```

---

## 3. ESF Asset Format (Engine Scene File)

### Pipeline

```
VICSFFile::Parse(filename, VIESFParse, VIScene)
├── VIFile::Open(filename)
└── VICSFFile::Parse(VIFile, VIESFParse, VIScene)
    ├── Decompress(VIFile, ...)           ← CSF = Compressed Scene File!
    │   ├── VIFile::Read → VIBufferSwap   ← Byte-order swap (endian)
    │   └── Decompression algorithm
    ├── VIObjFile::Open(memSegments)       ← Open decompressed in-memory
    └── VIESFParse::Parse(VIObjFile, VIScene) ← Parse object graph
```

**Key finding**: CSF = **Compressed Scene File**. The format is compressed + byte-swapped. `VIBufferSwap` handles endianness (PS2 is little-endian, but the format may store big-endian for portability — the engine was ported to multiple platforms).

### Object Types in ESF

The 117 VIESFParse methods reveal the complete asset type hierarchy:

#### World/Zone (Level Structure)
```
ParseWorld → ParseWorldBase → ParseWorldBaseHeader
                            → ParseWorldRegions
                            → ParseWorldTree
                            → ParseWorldZones
                              → ParseWorldZoneProxies

ParseZoneBase → ParseZoneRooms → ParseZoneRoom
             → ParseZoneTree
             → ParseZoneActors → ParseZoneActor
             → ParseZonePreTranslations      ← Float precision offsets!
             → ParseZoneStaticLightings
             → ParseZoneStaticTable
             → ParseZoneFlora → ParseZoneFloraSets
                              → ParseZoneFloraSpriteArray
             → ParseZoneRoomActors
             → ParseZoneRoomStaticLightings
             → ParseZoneResources → ParseZoneResource
```

#### Sprites (Renderable Objects)
```
ParseHSpriteObj       ← Hierarchical sprite
  → ParseHSpriteHierarchy
  → ParseHSpriteAttachments
  → ParseHSpriteTriggers
  → ParseHSpriteSpriteArray
  → ParseHSpriteAnimObj → ParseHSpriteAnim → ParseHSpriteAnimArray

ParseCSpriteObj       ← Complex sprite
  → ParseCSpriteNodeIDList
  → ParseCSpritePlayList
  → ParseCSpriteSkinList
  → ParseCSpriteASlotList (attach slots)
  → ParseCSpriteTSlotList (trigger slots)
  → ParseCSpritePartDefinitions
  → ParseCSpritePartEmitters
  → ParseCSpriteContSound
  → ParseCSpriteSpriteArray

ParseSimpleSpriteObj, ParseSimpleSubSpriteObj
ParseLODSpriteObj → ParseLODSpriteLevels → ParseLODSpriteSpriteArray
ParseSkinLODSpriteObj → ParseSkinLODSpriteLevels
ParseSkinSubSpriteObj
ParseGroupSpriteObj → ParseGroupSpriteMembers → ParseGroupSpriteSpriteArray
ParseFloraSpriteObj
ParsePointSpriteObj
ParseEffectVolumeSpriteObj
ParseSoundSpriteObj
ParseStreamAudioSpriteObj
ParseParticleSpriteObj
ParsePointLightObj
```

#### Materials & Geometry
```
ParseMaterial, ParseMaterialPal, ParseMaterialPalObj
ParseSurface, ParseSurfaceObj, ParseSurfaceArray, ParseSurfaceArrayObj, ParseSurfaces
ParsePrimBuffer, ParsePrimBufferObjV0    ← "V0" = version 0!
ParseSkinPrimBuffer, ParseSkinPrimBufferObjV0
ParseFloraPrimBuffer
ParseCollBuffer                          ← Collision geometry
ParseColorBuffer                         ← RTT targets
ParseStaticLighting, ParseStaticLightingObj
```

#### Other
```
ParseParticleDefinition, ParseParticleDefinitionObj
ParseSpellEffectObj
ParseRefMap, ParseRefMapObj              ← Environment reflection maps
ParseFontObj
ParseSound, ParseSoundArray, ParseAdpcmObj
ParseXmObj                               ← Unknown format (XM music?)
```

### Pixel Format Conversion

```
Convert4(VIPixelStore, src, dst, size)   ← 4-bit indexed (palettized)
Convert8(VIPixelStore, src, dst, size)   ← 8-bit indexed
Convert16(VIPixelStore, src, dst, size)  ← 16-bit color (5551/565?)
Convert24(VIPixelStore, src, dst, size)  ← 24-bit RGB
Convert32(VIPixelStore, src, dst, size)  ← 32-bit RGBA
AdpcmToPcm(src, size, dst, size)         ← Audio decompression
```

---

## 4. Lighting Subsystem

### VIPointLight

```
VIPointLight (inherits VISprite)
├── Init(radius, VIColor32F)             ← Light color + falloff radius
├── ClampScale(VIMatrix44)               ← Clamp light scale to bounds
├── Raster(camera, scene, raster, flags) ← Render light volume
│   ├── ClampScale(Matrix44)
│   ├── GetLightUISprite(VIScene)
│   ├── GetModelView(VIRaster)
│   ├── SetModelView(VIRaster, Matrix44)
│   └── RasterUISprite(VIScene, camera, spriteId, flags)
├── Copy / Release / Pick              ← Standard sprite operations
└── Collide (sphere collision only)     ← Lights have physical volume
```

**Key insight**: Point lights render via `RasterUISprite` — they use the **same billboard rendering path** as particles. This means a point light is essentially a colored billboard that also affects nearby geometry colors via `VIColorBuffer`.

### VIColorBuffer (Render-to-Texture)

```
VIColorBuffer
├── Init(index, VIRaster)
│   ├── Allocate → vec_new                ← Dynamic allocation
│   ├── CalcDataSize(VIPrimBuffer)        ← Size from geometry
│   ├── SharePrimBuffer(VIRaster, id)     ← Share vertex data
│   └── PrimBuffer(VIRaster, id)          ← Get vertex buffer
├── Lock(VIRaster)                         ← Lock for rendering
│   └── PrimBuffer(VIRaster, id)
├── Unlock                                 ← Release lock
├── Color(VIColor32)                       ← Set light color
└── Clear / Release
```

**VIColorBuffer = per-vertex color overlay**: Each color buffer is tied to a `VIPrimBuffer` (geometry). `Lock` → render light color → `Unlock`. This is how dynamic lighting works on PS2 without pixel shaders — **per-vertex color buffers** that get blended with base geometry colors.

### VIStaticLighting

```
VIStaticLighting
├── Init(count)                            ← Count of color buffers
│   └── Init(VIArray<int>, count)
├── ShareResources(VIRaster)
│   └── ShareColorBuffer(VIRaster, id)     ← Share pre-baked lighting
├── ReleaseResources(VIRaster, VIDictionary)
│   └── ReleaseColorBuffer(VIRaster, id, VIDictionary)
└── Clear(VIRaster, VIDictionary)
    └── ReleaseResources
```

Static lighting is pre-baked per-vertex colors stored in VIColorBuffer. Dynamic lights (VIPointLight) add their contribution on top at runtime.

### Lighting Architecture Summary

```
VIScene render pass:
  1. Render geometry with static VIColorBuffer (pre-baked)
  2. For each VIPointLight in view:
     a. Lock affected VIColorBuffer
     b. Render light contribution (additive color)
     c. Unlock VIColorBuffer
  3. Re-render affected geometry with updated colors

Cave scenario (10 torches):
  - 10 VIPointLight::Raster calls
  - 10 VIColorBuffer Lock/Unlock cycles
  - Geometry re-rendered per light = 10x overdraw
  - PLUS particle billboards for fire visual effect
  = MASSIVE fill rate + DMA bandwidth consumption
```

---

## 5. VIScene — Scene Manager

### Core Architecture (140 methods, 44.1 KB)

VIScene is the central coordinator. Key method groups:

#### Actor Management
```
CreateActor, ReleaseActor, RemoveActor, UpdateActor
SetActorLocation, SetActorHPR, SetActorScale, SetActorTransform
SetActorVisibility, SetActorCollideable, SetActorAudible
SetActorLighting, SetActorSprite, SetActorID
GetActorID, GetActorTransform, GetEnvFlags
IsActorVisible, IsActorAudible, IsActorCollideable, IsActorProxy, IsActorStatic
InsertActor (into zone spatial structure)
```

#### Rendering
```
Render(VICamera)                    ← MAIN RENDER ENTRY POINT
RasterActor, RasterSprite, RasterUISprite
RenderShadow, RenderShadows, ClearShadowQueue
RenderDeferredList                  ← Deferred rendering (transparent objects?)
SetSky, SetSky(camera, zoneIndex)
CalcFarPlane, SetFarPlane
```

#### Spatial Queries
```
Collide (sphere, ray, envray)
CollideActor, CollideSprite
Pick (segment)
PickActor, PickSprite
QueryVisibleActors, QueryProximalActors, QueryActorsInVolume
QueryEmittersAtLocation, QueryEmittersActor
QueryIntersection, QueryIntersectionActor, QueryIntersectionSprite
```

#### Streaming
```
Stream(location, VILoader, flags)
StreamClearCache, StreamFillCache
StreamInStaticActor, StreamOutStaticActor, StreamHaltStaticActor
StreamInCompleteActor
ReleaseStatic(VIZone, VILoader)
RemoveActorsFromZone, ReplaceProxyActors, ReplaceProxyRooms
```

#### Time of Day
```
InitTimeOfDay, SetTimeOfDay(float)
SetupTimeOfDay(camera, terrainProfile, flags)
SetupTimeOfDayFog, SetupTimeOfDayLights, SetupTimeOfDaySky
CalcTimeOfDayClipPlanes, CalcOutdoorsIntensity
```

#### Personal Lighting (Player light)
```
SetPersonalLight(index, radius, color)    ← Per-player light
SetPersonalLight(location, radius, color)
SetPersonalLightMode(mode)
```

---

## 6. Atmosphere System (VIAtmosphere — 28 methods, 21.1 KB)

### Call Graph (ast-grep extracted)

```
Update(VIScene, VICamera, time, deltaTime)
├── ProcessTransitions(VIScene, deltaTime1, deltaTime2)    ← Weather state machine
│   ├── CopyLayer(VIMaterial)                               ← Transition blending
│   ├── SetNumLayers / SetLayerBlendMode / SetLayerTexture ← Material reconfiguration
│   ├── SetLayerColor(VIMaterial, VIColor32)                ← Sky color interpolation
│   ├── Play / Stop / SetVolume / SetPan / SetPitch(VISoundDevice) ← Ambient audio!
│   ├── ClearAllSplashes                                    ← Reset rain effects
│   └── ResetLightning                                      ← Reset lightning system
├── ProcessWeather(VIScene, VICamera)                       ← Per-frame weather sim
│   ├── Init(VICollRay) / Init(VIEnvRay)                   ← Create raycasts
│   ├── Collide(VIScene, ray)                               ← Cast rays at terrain!
│   ├── GetHitPoint(VICollRay/VIEnvRay)                    ← Where rain hits ground
│   ├── AddSplash(VIVect3)                                  ← Create splash at hit
│   └── ProcessLavastorm(VIScene, VICamera)                 ← Lava effects
│       ├── Create(VIParticleEmitter)                       ← Spawn lava particles
│       ├── SetLocation(VIParticleEmitter)                  ← Position particles
│       ├── Update(VIParticleEmitter)                       ← Tick simulation
│       └── Destroy(VIParticleEmitter)                      ← Cleanup dead emitters
├── RotateHPR(VIMatrix44)                                   ← Rotate sky dome
├── Scale(VIMatrix44)                                       ← Scale sky dome
└── Mul(VIMatrix44)                                         ← Compose transform

RenderSky(VIScene, VICamera)
├── SetModelView(VIRaster, Matrix44)     ← Sky orientation
├── RenderStars(VIScene, VICamera)       ← Stars sub-pass
│   ├── SetFog(VIRaster, 0)             ← Disable fog for stars
│   ├── BeginBillboards(VIRaster)        ← Stars are billboards!
│   ├── SetMaterial(VIRaster)            ← Star material
│   └── EndBillboards(VIRaster)
└── Mul(VIMatrix44)                      ← Sky dome transform

RenderWeather(VIScene, VICamera)
├── Plane(VIFrustum, i)                  ← Frustum planes for culling
├── Normalize(VIVect3)                   ← Direction vectors
├── BeginBillboards(VIRaster)            ← Rain/snow are billboards!
├── SetMaterial(VIRaster)                ← Weather particle material
├── SetModelView(VIRaster)               ← Camera-relative transform
├── RenderSplashes(VIScene, VICamera)    ← Ground splash sub-pass
│   ├── BeginBillboards(VIRaster)        ← Splashes are billboards too
│   ├── SetMaterial(VIRaster)
│   └── EndBillboards(VIRaster)
└── EndBillboards(VIRaster)

Init(VIRaster, flags)
├── CreateMaterial(VIRaster) × many      ← Pre-create sky/weather materials
├── Init(VIMaterial)                     ← Configure each layer
├── SetLayerBlendMode / FillType / Modulate / LODBias / ZTest / ZWrite
├── RotateHPR(VIMatrix44)               ← Pre-compute star rotations
├── Mul(VIMatrix44, VIVect4)            ← Pre-compute star positions
├── ps2__(VIParticleEmitter) × pool     ← Pre-allocate lava emitter pool
└── Init(VILList) × several             ← Linked lists for splash/fireball pools
```

**Key findings**:
1. **Weather raycasting** — Rain doesn't just fall; the system casts rays at terrain to determine splash positions. This means outdoor weather has collision overhead per raindrop.
2. **Everything is billboards** — Stars, rain/snow, splashes, and lava particles all use BeginBillboards/EndBillboards. In a storm, this could be hundreds of billboards.
3. **Lavastorm has its own particle subsystem** — ProcessLavastorm creates/updates/destroys VIParticleEmitters dynamically, separate from the static particle system. Lava areas have both zone particles AND atmosphere particles.
4. **Weather transitions involve audio** — ProcessTransitions calls Play/Stop/SetVolume/SetPan/SetPitch on VISoundDevice. Weather changes crossfade ambient sound.
5. **Material layer manipulation** — Transitions reconfigure materials (layer count, blend mode, texture, color) per frame for sky dome blending. This is how sunrise/sunset works.

---

## 11. Audio System (VISoundDevice)

### Architecture

```
VISoundDevice
├── VIPlayback[]                ← Active sound instances (linked list pool)
│   ├── VISound*                ← Reference to sound asset
│   │   ├── VIWave (ADPCM)     ← Compressed audio (SPU2 hardware decode)
│   │   └── VIXm (tracker)     ← XM tracker module format
│   ├── channelMask (uint64)    ← Bitmask of allocated SPU2 channels (46 max!)
│   └── soundClass              ← VISOUNDCLASS enum for volume grouping
├── VILList<freeSpuMem>         ← SPU memory free list (linked list allocator)
├── VILList<freeXmMem>          ← XM memory free list
├── VILList<playbackPool>       ← Reusable playback instances
└── IOP interface               ← EE→IOP RPC bridge
```

### Key Call Patterns

```
Play(soundId, flags, VISOUNDCLASS)
├── Type(VISound) → Wave or Xm         ← Dispatch by format
├── ChannelCount(VIWave/VIXm)           ← How many SPU2 channels needed
├── AllocateChannels(channelsNeeded, priority)
│   ├── FirstPlayback / NextPlayback    ← Walk active sounds
│   ├── ChannelCount(existing)          ← Check if can steal channels
│   └── Stop(existingId)               ← Evict lower-priority sounds!
├── FirstChannel / NextChannel          ← Walk allocated channel IDs
├── NewPlayback                         ← Get from pool
└── SetIopFunction(cmd, params)         ← Send play command to IOP

Stop(playbackId)
├── Playback(id)                        ← Find playback instance
├── StopChannels(channelMask)           ← Stop SPU2 hardware channels
│   ├── FindIopFunction(cmd)            ← Look up IOP command slot
│   └── SetIopFunction(cmd, 0)          ← Send stop to IOP
├── DeallocateChannels(channelMask)     ← Free channel bitmask
└── DeletePlayback(playback)            ← Return to pool

SetVolume / SetPan / SetPitch(playbackId, value)
├── Playback(id)                        ← Find instance
├── Type(VISound) → Wave or Xm         ← Dispatch
├── FirstChannel / NextChannel          ← Apply to all channels
└── SetIopFunction(cmd, value)          ← Send to IOP
```

### IOP Communication

The PS2 has a dedicated I/O Processor (IOP) that handles audio hardware (SPU2). All sound commands go through:

```
SetIopFunction(commandSlot, value)      ← Write to shared memory ring buffer
FlushIopCommand(wait)                   ← sceSifSetDma → flush to IOP
FindIopFunction(commandSlot)            ← Read back from IOP
```

This uses **SIF DMA** (`sceSifSetDma`, `sceSifDmaStat`) — the EE↔IOP communication bridge. For the native port, this entire IOP layer needs replacement with a modern audio backend.

### Audio Formats

| Format | Type | Hardware | Notes |
|--------|------|----------|-------|
| VIWave (ADPCM) | Compressed PCM | SPU2 decode | Most sound effects |
| VIXm | Tracker module | Software decode | Music, ambient loops |
| BGM | Background music | Streaming | `StreamBgm`, `StopAllBgm`, `BgmVersion` |

### Channel Management

SPU2 has **48 hardware voices**, but the engine reserves 46 (2 for system). Channel allocation uses a **bitmask** (uint64) where each bit = one SPU2 voice. When channels are exhausted, `AllocateChannels` **steals from lower-priority sounds** — priority eviction.

**Key for native port**: Replace VISoundDevice + IOP bridge entirely. The VIWave ADPCM format is PS2-specific (Sony VAG/ADPCM). Need to either decode VAG→PCM or find a VAG decoder library.

---

## 12. World/Terrain System (VIWorld)

### Architecture

```
VIWorld
├── VIWorldTree                          ← Spatial tree for world geometry
├── VIArray<VIZone>                      ← Zone array (from VIWorld::Init)
├── VIArray<VIWorldRegion>               ← Regions (sub-zone groupings)
├── VIVect3 origin                       ← World origin (pre-translation base)
├── VIBBox extents                       ← World bounding box
├── float cellSize                       ← Terrain grid cell size
├── int xCells, zCells                   ← Grid dimensions (x × z multiply!)
└── terrain profiles                     ← Height/material lookup
```

### Init Call Graph

```
Init(xCells, yUnused, zCells, cellSize, origin, extents)
├── Init(VIArray<VIZone>, zoneCount)            ← Allocate zone array
├── for each zone:
│   └── Init(VIZone)                             ← Individual zone init
│       ├── VIZoneTree::Init                     ← BSP tree per zone
│       ├── VIArray<VIZoneRoom>::Init            ← Room array
│       └── VIZoneRoom::Init per room            ← Per-room setup
├── Init(VIWorldTree, xCells*zCells, 1)          ← World spatial tree
├── SetProfiles(VIWorld)                         ← Terrain profile setup
├── Init(VIArray<VIWorldRegion>, regionCount)    ← Region allocation
└── Copy origin, extents, cell dimensions        ← Store grid params
```

**Key finding**: VIWorld uses a **grid-based terrain** with `xCells × zCells` cells of `cellSize` each. The terrain cell multiplication (`xCells * zCells`) uses hardware multiply (`MULT` instruction). `VIWorldTree` provides spatial lookups, while individual `VIZone`s handle BSP-based rendering within each cell.

### Spatial Operations

```
RenderByFrustum(VISceneRendVars)
├── PushFrustum(VIClipStack, VICamera)   ← Camera frustum to clip stack
├── GetTop(VIClipStack)                  ← Get clip planes
├── RenderByVolume(VIWorld)              ← Recursive render
│   └── per zone: RenderByVolume(VIZone, VISceneRendVars)
└── Pop(VIClipStack)                     ← Restore clip state

Collide(zoneIndex, VISceneCollVars)      ← Delegates to VIZone::Collide
InsertActor(zoneIndex, VISceneInsertVars) ← Delegates to VIZone::InsertActor
Pick(zoneIndex, VIScenePickVars)          ← Delegates to VIZone::Pick

QueryVisible(zoneIndex, VISceneVisQueryVars)
QueryVisibleBySphere(VISceneVisQueryVars) ← Sphere-based visibility
QueryProximal(zoneIndex, VISceneProxQueryVars)
QueryEmitters(zoneIndex, VISceneEmitterQueryVars)
QueryIntersection(zoneIndex, VISceneIntersectVars)
QueryVolume(zoneIndex, VISceneBBoxQueryVars)
```

### Terrain Profile System

```
CalcTerrainCell(position) → (cellX, cellZ)     ← Position to grid cell
CalcTerrainProfile(position) → profile          ← Get terrain material/height
CalcTerrainCellBVolume(cellX, cellZ) → VIBBox   ← Cell bounding volume
CalcProfileBlend(position) → VITerrainProfileBlend ← Blend between cells
SetProfiles(VIWorld)                             ← Initialize profile table
```

**Terrain profiles** provide ground material type and height at any world position. `CalcProfileBlend` interpolates between adjacent cells for smooth transitions. This drives footstep sounds, movement speed, and visual effects.

### Streaming Integration

```
Stream(zoneIndex, VISceneBBoxStreamVars)     ← Box-based streaming
Stream(zoneIndex, VISceneStreamRadialVars)   ← Radial streaming
StreamLeaf(zoneIndex, VISceneBBoxStreamVars) ← Per-leaf streaming decisions
```

VIWorld delegates streaming to per-zone, per-leaf granularity. Two streaming modes:
- **BBox**: Stream zones overlapping a bounding box (for portals/doorways)
- **Radial**: Stream zones within radius of player (for open areas)

---

## 13. Sprite Hierarchy (VIHSprite — 101 methods, VICSprite — 55 methods)

### Type Hierarchy

```
VISprite (base — 8 types)
├── VISimpleSprite          ← Textured quad
├── VILODSprite             ← Level-of-detail switching
├── VIHSprite               ← Hierarchical sprite (bone animation)
│   └── VICSprite           ← Character sprite (armor, weapons, customization)
├── VIGroupSprite           ← Transform group (parent→children)
├── VIFloraSprite           ← Vegetation (billboard + wind)
├── VIPointSprite           ← Point in space (waypoint, etc.)
├── VIPointLight            ← Dynamic point light (VIColorBuffer overlay)
├── VIParticleSprite        ← Particle emitter (billboard particles)
├── VINameSprite            ← Text label (fonts)
├── VISkinSprite            ← Skinned mesh (GPU skinning)
└── VIStreamAudioSprite     ← Spatial audio emitter (3D sound)
```

### VIHSprite (Hierarchical Animated Sprite)

```
VIHSprite
├── VIHSpriteNode[]                ← Bone hierarchy (VIVector<VIHSpriteNode>)
├── VIHSpriteAnim                  ← Animation data
│   ├── playMode, playSpeed        ← Playback settings
│   └── numFramesPerNode           ← Animation clip data
├── VIPool<VIHSpritePlay>          ← Active animations (blending pool)
├── VIPool<VIHSpritePlayNode>      ← Per-node animation state
├── VIPool<VIHSpriteAttachment>    ← Attached items (weapons, shields)
├── VIArray<VIHSpriteTrigger>      ← Animation triggers (sound, VFX at frame N)
├── VIVector<VIMatrix44>           ← Bone matrices (current pose)
└── LOD level index                ← Current detail level
```

#### Animation System

```
AddPlay(animId, VIPlaybackType, speed, VIScene)          ← Start animation
AddInterpolatedPlay(animId, type, blendTime, VIScene)    ← Blended transition
AddInterpolatedPlayWithSync(animId, syncSource, syncTarget) ← Synced blend
AddPlayWithSync(animId, syncFrame, VIScene)               ← Start at sync point
StopPlayback(animId, VIScene)                             ← Stop animation
FreezePlayback(animId, VIScene)                           ← Pause at current frame
SetPlayFrame(animId, frame, VIScene)                      ← Seek to frame
ErasePlay / EraseAllPlay                                  ← Remove from blend pool

Process(animIndex, VIScene)                                ← Per-frame update
├── ProcessPlayList(animIndex, VIScene)                    ← Advance all active anims
├── ProcessPlayTiming(animIndex, VIScene)                  ← Handle blend timing
├── ProcessHierarchy(VIHSprite)                            ← Compute bone transforms
│   ├── ProcessUpHierarchy(boneIndex)                      ← Walk up to root
│   └── CalcNodeTransform(boneIndex, Matrix44, VIScene)    ← Per-bone matrix
└── UpdateCenterTransform(VIScene)                         ← Model center update

Raster(VICamera, VIScene, VIRaster, flags)                 ← Render
├── CalcLODLevelIndex(Matrix44)                            ← Distance-based LOD
├── GetModelView(VIRaster)                                 ← Camera transform
├── SetBlendMatrices(VIRaster)                             ← Upload bone matrices
│   └── SetObjectBlends(VIRaster, count, Matrix44*)        ← GPU blend matrices
└── [per attachment] Raster recursively                     ← Render attached items
```

### VICSprite (Character Sprite — extends VIHSprite)

```
VICSprite
├── VICSpriteAttachSlot[]         ← Weapon hand, shield hand, helmet, etc.
├── VICSpritePartEmitter[]        ← Per-bone particle emitters (fire hands, etc.)
├── VICSpriteCust                 ← Customization system
│   ├── VICSpriteRace             ← Race (elf, human, etc.)
│   ├── VICSpriteArmorSet         ← Armor visual set
│   ├── VICSpriteTint             ← Color tinting
│   └── VICSpriteTextSlot         ← Texture slots (body, robe, face, hair)
├── VICSpriteAnimID               ← Animation state machine
└── VITrailFx                     ← Weapon trail VFX

Key methods:
SetAnimation(VICSpriteAnimID, flags, VIScene)    ← State machine transition
SetArmorSlot(slot, armorSet, tint, VIScene)      ← Visual equipment change
SetHelm(armorSet, tint, VIScene)                 ← Helmet change
SetHair(style, color, flags, VIScene)            ← Hair customization
SetItemAction(itemId, VIScene)                   ← Weapon type change
SetLocomotion(animId, VIScene)                   ← Movement animation
AttachItem(spriteId, slot, attackType, flags, VIScene) ← Attach weapon
DetachItem(slot, VIScene)                        ← Remove weapon
ProcessWeaponTrails(VICamera, VIScene, Matrix44) ← Weapon trail VFX update
CalcVolumeAndPan(VICamera, position) → (vol, pan) ← 3D sound attenuation
CalcSlotWorldTransform(nodeId, boneIndex, VIScene) → Matrix44 ← Attachment point
```

**Key finding**: VICSpriteCust reveals the character customization system — race, armor set, tint color, and per-slot textures (body, robe, face, hair) are all hot-swappable at runtime. `GetArmorSetTexture`, `GetFaceTexture`, `GetHairTexture`, `GetRobeTexture` show the texture lookup pipeline.

### Sprite Copy Protocol

Every sprite type implements `Copy(VIScene, VIRaster, VISoundDevice, VICollide, flags)` for multiplayer entity duplication. The copy protocol creates a new sprite in the scene, shares (ref-counts) all assets, and deep-copies mutable state.

---

## 15. Engine Boot Sequence (engineInit → ps2_main → gameLoop)

### engineInit(frameRate) — Hardware Initialization

Called once at startup. Initializes ALL engine subsystems in order:

```
engineInit(frameRate)
├── memInit(heapBase, heapSize)          ← Memory system (before everything!)
├── blockAllocInit                       ← Block allocator
├── listInit                             ← Global linked list system
├── sceGsResetGraph / sceDmaReset        ← Graphics Synthesizer + DMA reset
├── initSif                              ← SIF (EE↔IOP bridge)
├── initVIF                              ← VIF (VU Interface)
├── initSupersample                      ← Supersampling setup
├── sceGsSetDefDispEnv / sceGsPutDispEnv ← Display environment
├── textureInit(width, height)           ← Texture cache + decompress
├── textureAllocateCacheBuffer           ← EDRAM texture cache
├── emathInit                            ← Engine math (VU0 math routines)
├── drawInit                             ← Draw list system
├── animInit                             ← Animation system
├── floorInit                            ← Floor/terrain system
├── lightInit                            ← Lighting (VIColorBuffer setup)
├── objectInit                           ← Object system (game entities)
├── padInit                              ← Controller input
├── soundInit(frameRate)                 ← VISoundDevice + IOP audio
├── cdInit                               ← CD/DVD filesystem
├── worldInit                            ← World/terrain system
├── scriptInit                           ← AMX/Pawn VM
├── P_Init                               ← Particle system
├── lumpLoad("common")                   ← Load common resource lumps
├── lumpLock(0)                          ← Lock common resources
└── AddIntcHandler / EnableIntc          ← Register interrupt handlers
```

**Key insight**: The init order reveals dependencies. Memory → lists → GPU → DMA → textures → drawing → lighting → objects → input → audio → filesystem → world → scripting → particles. For the native port, this is the replacement order — each subsystem can be replaced independently as long as the initialization order is preserved.

### ps2_main — Application Entry Point

```
ps2_main(argc, argv)
├── initChars(argc, argv)                ← Parse command line
├── engineInit(frameRate)                ← Engine init (above)
├── gameInit                             ← Game-specific init
├── MC_Init / MC_Configure               ← Memory card system
├── frontEndInit(mode)                   ← UI/menu system
├── DLG_Init / DLG_InitNet              ← Dialog system + network dialogs
├── commInitNet                          ← Network message handlers
├── hudInitNet / inventoryInitNet / shopInitNet / textInitNet
│                                        ← Net-aware subsystems
├── cutInitNet                           ← Cutscene network sync
├── gameBoot                             ← Game boot (just Camera + skill ramps)
├── gameLoop                             ← MAIN LOOP (never returns during play)
│   ├── [see below]
├── lumpClear / netFree                  ← Cleanup
└── [cleanup sequence]
```

### gameLoop — Main Frame Loop

```
gameLoop
├── engineFrameStart(vsyncCount, isGameActive)  ← Begin frame
│   ├── sceGsResetGraph / sceGsSyncV            ← VSync
│   └── [DMA buffer swap]
├── padProcess                                   ← Read controller input
├── cdProcess                                    ← Check async CD reads
├── texProcessLoad / texProcessDecompress        ← Async texture pipeline
├── lumpCheck                                    ← Resource lump management
├── soundFrame                                   ← Audio frame (VISoundDevice)
├── animFrame                                    ← Animation tick
├── runMusic                                     ← Music system update
├── netGameStep(...)                             ← Network frame sync
├── coreGameStep(step, flags)                    ← SIMULATION
│   ├── padRunFrame                              ← Process input
│   ├── engineRunTasks(step, flags)              ← Run registered tasks
│   ├── enumerateAlivePlayers                    ← Player state
│   └── gameCheckForDeathScreen                  ← Death check
├── scriptRun                                    ← AMX/Pawn VM execution
├── Update(Camera)                               ← Camera update
├── gameDrawWorld                                ← RENDERING
│   ├── worldSetViewCenter                       ← Set camera in world
│   ├── worldDrawWorld(worldHeader)              ← World geometry render
│   ├── drawAutoMap                              ← Minimap overlay
│   └── drawDome                                 ← Sky dome
├── drawListClear                                ← Reset draw lists
├── P_Clear                                      ← Reset particle system
├── engineFrameEnd(isActive)                     ← End frame
│   ├── [DMA flush + buffer swap]
│   └── [VSync wait]
└── [loop back to engineFrameStart]
```

**Key insight**: The frame loop is split into simulation (`coreGameStep` + `scriptRun`) and rendering (`gameDrawWorld`). These are NOT decoupled — simulation and rendering happen sequentially in the same frame. For the native port, we could potentially decouple these for multi-threaded rendering.

### Window/UI System (VIWnd — 14+ window types)

```
VIWnd (base)
├── VIWndCombo          ← Dropdown/combo box
├── VIWndConnect        ← Network connection wizard (DNAS, ISP config)
├── VIWndDnas           ← Sony DNAS authentication
├── VIWndEdit           ← Text input field
├── VIWndEula           ← EULA/legal text display
├── VIWndGenericRenderer ← Data-driven UI renderer (VIGUIPage, VIFlatFile)
├── VIWndLegal          ← Legal notice screen
├── VIWndMcErr          ← Memory card error dialogs (18+ screens!)
├── VIWndMessage        ← Message/dialog box
├── VIWndOptions        ← Game options (sound, interface, graphics)
├── VIWndPatcher        ← Online patch downloader
├── VIWndReadMessage    ← Message reader (scrollable text)
├── VIWndSplash         ← Splash/loading screen
└── VIWndStationLogin   ← Station.com login (SOE online services)
```

The UI system is a widget hierarchy: `VIWnd` is the base, with `AddChild/RemoveChild` for tree structure, `OnDraw/OnDrawSelf` for rendering, `OnKeyDown/OnKeyUp/OnSelect` for input, and `HandleEvent/OnMessage` for event dispatch. `VIWndGenericRenderer` is the most complex — a data-driven renderer using `VIGUIPage` and `VIFlatFile` for XML-like UI definitions.

**For native port**: VIWndConnect, VIWndDnas, VIWndStationLogin, VIWndPatcher are all PS2/SOE online-specific — these entire windows can be removed. VIWndMcErr (memory card errors) becomes save file errors. The core VIWnd hierarchy and VIWndGenericRenderer are reusable.

---

## 16. Networking Stack (344 files!)

```
Transport Layer:
├── VITCPSocket2         ← TCP socket wrapper
├── VIUDPSocket          ← UDP socket wrapper
├── TcpManager           ← Connection management
├── TcpConnection        ← Per-connection state (refcounted)
├── connection_t         ← Low-level connection struct
│   ├── connection_allocate_state_channels
│   ├── connection_add_rtt_sample     ← RTT tracking!
│   └── connection_append             ← Buffer management
└── GenericAPI::GenericConnection      ← Abstraction layer

Protocol Layer:
├── packet_*             ← Packet serialization
├── message_list_t       ← Message queuing
├── drdp_*               ← "DRDP" protocol (Dark Alliance Reliable Data Protocol?)
│   └── drdp_address_to_endpoint
└── buffer_t             ← I/O buffers

Game Network:
├── netInit / netStart / netFree       ← Lifecycle
├── netGameStep(isActive, isHost)      ← Per-frame sync
├── netPlayerIsConnected / netPlayerIsLocal
├── netRegisterMessageHandler          ← Message dispatch table
├── netRegisterPacketHandler           ← Packet dispatch table
├── netWaitForPeersToCatchUp           ← Frame sync barrier
├── netClearContact / netInContact     ← Connection status
└── netStartNetworkGameInit            ← Game session setup

Platform:
├── sceInetCtlGetState     ← PS2 network adapter state
├── sceSifLoadModule       ← Load IOP network modules
├── VIEELoadIrx            ← Load IRX (IOP Relocatable eXecutable)
├── sceDNAS2Status         ← Sony DNAS authentication
└── commInitNet            ← Register all network handlers
```

**Key finding**: The networking stack is substantial — 344 files, a custom reliable protocol ("DRDP"), RTT tracking, frame sync barriers. This is a peer-to-peer architecture (no dedicated server). For the native port, this needs replacement with a modern networking library (ENet, GameNetworkingSockets, etc.) but the game-level message/packet handler registration pattern (`netRegisterMessageHandler`) can be preserved.

---

## 17. Full Engine Dependency Map

```
                        ps2_main
                           │
                ┌──────────┼──────────┐
           engineInit    gameInit    gameLoop
                │           │           │
         ┌──────┤      ┌────┤      ┌────┼────────┐
         │      │      │    │      │    │         │
      VIRaster  │   createByName  coreGameStep  gameDrawWorld
         │      │      │           │              │
    [DMA/GS]    │   Creature    scriptRun      worldDrawWorld
                │   Player      (AMX/Pawn)        │
            VIScene                            drawDome
               │                              drawAutoMap
    ┌──────────┼───────────────┐
    │          │               │
VIWorld   VIAtmosphere   VISoundDevice   VILoader
    │          │               │             │
 VIZone    [Raycasts]    [IOP Bridge]    [Async I/O]
  / | \    [Billboards]   [SPU2 HW]     [ESF Parse]
BSP Room Flora   │             │
  │         VIParticle      VIWave/VIXm
  │        /    │    \
  └─ VIRaster ──┘   VIPointLight
       │                │
  VIHSprite         VIColorBuffer
       │          (per-vertex overlay)
  VICSprite
  (customize, trails)

  VIWnd (UI)              Network
  ├── VIWndGenericRenderer  ├── VITCPSocket2/VIUDPSocket
  ├── VIWndOptions          ├── DRDP protocol
  ├── VIWndEdit             ├── netGameStep (frame sync)
  └── [14+ window types]    └── netRegisterMessageHandler
```

---

## Key Architectural Insights

### 1. Everything is a BSP traversal
Zone rendering, collision, picking, proximity queries, emitter queries — ALL follow the same recursive BSP pattern: test node planes, recurse into visible children, process at leaf level.

### 2. Pre-translation is pervasive
Not just rendering — collision, picking, and all spatial queries apply zone pre-translation. This is critical for the native port: we need to either maintain this system or use double-precision math.

### 3. The lighting bottleneck is architectural
Each VIPointLight requires locking a VIColorBuffer, computing per-vertex colors, and re-rendering geometry. With N dynamic lights, you get N× overdraw. This is the *fundamental* cave performance issue — it's not a bug, it's how the engine does dynamic lighting without pixel shaders.

### 4. Particles compound the lighting problem
Fire particles are billboards (VIParticleSystem::Render uses BeginBillboards). Fire also has attached VIPointLight. So each torch = billboards + light passes + DMA bandwidth for all of it.

### 5. ESF is the master asset format
Everything goes through VIESFParse — world geometry, sprites, materials, particles, sounds, collision. Understanding ESF = understanding the entire asset pipeline. The "V0" version markers on PrimBuffer/SkinPrimBuffer suggest format evolution across games.

### 6. The scene manager is the integration point
VIScene::Render coordinates zones, actors, sprites, shadows, deferred rendering, sky, and time-of-day. For the native port, this is where we hook in paraLLEl-GS or a modern rendering backend.

### 7. Streaming is zone-based
VIScene::Stream loads/unloads zones based on player position. Each zone has its own pre-translation, resource table, and static actor set. Zone transitions are managed by proxy actors that get replaced when the real zone loads.

### 8. Engine vs Game code are two distinct layers
The engine uses C++ OOP (`VI*` prefix, `VIVect3`, `VIMatrix44`, `VIPool`/`VIArray`). The game code uses C-style free functions (`objectFindInBox`, `worldHitscan`, `modelDraw`), `Point3`/`Matrix34` math types, and `ListHead` linked lists. This is the Slavedriver heritage — game code preserved the old patterns while the engine was rewritten for PS2.

### 9. createByName is the entity factory boundary
The 15.6 KB `createByName` function is the bridge between data-driven ESF loading and game entity instantiation. It constructs 100+ entity types via constructor calls, each parameterized by tag strings.

### 10. Audio is IOP-dependent — needs full replacement
VISoundDevice communicates with PS2 IOP via SIF DMA (`sceSifSetDma`). All audio goes through a command ring buffer to the IOP, which drives SPU2 hardware. VIWave uses Sony ADPCM (VAG format). For native port: replace entire VISoundDevice + IOP bridge with SDL_mixer or similar. VIXm (XM tracker) can use libxm.

### 11. Weather has physics — rain raycasts into terrain
VIAtmosphere::ProcessWeather casts VICollRay/VIEnvRay at terrain to find splash positions. Outdoor areas with weather incur per-drop collision overhead. Combined with billboard rendering for rain/snow, storms are expensive.

### 12. Sprite hierarchy is deep and branching
VIHSprite has 101 methods managing bone animation, LOD, attachments, triggers, and blend pools. VICSprite extends with 55 more for armor customization, weapon trails, and 3D audio attenuation. Each animated character involves: bone matrix computation → LOD selection → blend matrix upload → per-attachment recursive rendering → weapon trail VFX → particle emitter updates → sound attenuation.

### 13. ast-grep works perfectly on PS2Recomp output
`ast-grep --lang cpp --pattern '$FUNC(rdram, ctx, runtime)'` cleanly extracts all function calls from recomp files. This enables automated call graph extraction at scale across all 9,395 files. Tool saved as `tools/extract-callgraph.sh`.

### 14. The boot sequence defines the replacement order
`engineInit` initializes subsystems in dependency order: memory → lists → GPU → DMA → textures → drawing → lighting → objects → input → audio → filesystem → world → scripting → particles. For native port, replace from leaves inward: GPU (paraLLEl-GS), audio (SDL_mixer), filesystem (stdio), then work toward the core.

### 15. Frame loop is sequential — opportunity for threading
`gameLoop` runs simulation (`coreGameStep` + `scriptRun`) and rendering (`gameDrawWorld`) sequentially in the same frame. Native port could decouple simulation from rendering for multi-threaded performance. The `engineFrameStart/End` boundary is clean.

### 16. Networking is peer-to-peer with custom protocol
344 networking files, a custom "DRDP" reliable protocol, RTT tracking, and frame sync barriers (`netWaitForPeersToCatchUp`). The game-level handler registration pattern (`netRegisterMessageHandler/PacketHandler`) is clean and reusable. PS2-specific parts (DNAS auth, IRX loading, `sceInetCtl`) are isolatable.

### 17. UI is a retained-mode widget tree
VIWnd forms a tree with AddChild/RemoveChild, event dispatch via OnMessage/HandleEvent, and rendering via OnDraw. VIWndGenericRenderer is data-driven using VIGUIPage/VIFlatFile. PS2-specific windows (DNAS, Station login, memory card errors) can be removed; core widget system is reusable.

---

## 7. Asset Loading Pipeline (VILoader)

### Architecture

```
VILoader
├── VIFile[]                           ← Open resource files (CD/HDD)
├── VIPool<VILoaderTrans>              ← Transaction pool (pending loads)
├── VIMap<uint, int>                   ← Resource ID → transaction index
├── VIESFParse (embedded)              ← Parser instance
├── VIObjFile (embedded)               ← Object file reader
└── VIArray<VIResourceElem>            ← Resource directory
```

### Async Loading Flow

```
OpenResourceFile(index, filename, VIScene)
├── VIFile::Open(filename)
└── VIESFParse::ParseResourceFile       ← Parse resource directory

Load(fileIndex, resourceId, offset, size, flags)
├── Find(fileIndex, resourceId)         ← Locate in resource table
├── Align(VILoaderTrans)                ← DMA alignment!
│   └── VIFile::AsynchAlignment         ← Async seek alignment
└── VIPool<VILoaderTrans>::Add          ← Queue transaction

Process(VIScene)                        ← Called every frame
├── VIFile::IsAsynchComplete            ← Poll async I/O
├── VIFile::ReadAsynch(offset, buffer, size) ← Start async read
└── Complete(transIndex, VIScene)       ← When read finishes
    ├── VIObjFile::OpenObject            ← Parse loaded data
    ├── VIObjFile::FileType              ← Determine object type
    ├── VIESFParse::Parse(VIObjFile, VIScene)    ← General parse
    ├── VIESFParse::ParseZoneResource    ← Zone-specific parse
    └── VIScene::ShareResource           ← Register in scene
```

**Key finding**: Loading is fully asynchronous. `ReadAsynch` starts a DMA transfer from CD/HDD, `IsAsynchComplete` polls for completion, and `Complete` parses the data into scene objects. `Align` ensures DMA-aligned file offsets (PS2 DMA requires 16-byte alignment).

### Resource Management

```
Release(transIndex, VIScene)
├── VIScene::ReleaseResource             ← Remove from scene
├── VIMap::Erase                         ← Remove from tracking
└── VIPool<VILoaderTrans>::Erase         ← Free transaction slot

ReleaseAllComplete(VILoader, VIScene)    ← Bulk release finished loads
```

---

## 8. Collision System (VICollide)

### Collision Buffer Formats

Three vertex buffer formats for collision geometry (matching VIRaster's rendering formats):

| Format | Method | Description |
|--------|--------|-------------|
| PackV | `CollideBufferPackV` | Standard packed vertices |
| PackVGF | `CollideBufferPackVGF` | Packed vertices + ground flags |
| V | `CollideBufferV` | Raw vertex data |

All collision methods follow the same pattern:
1. `Cull(CollSphere/CollRay, BBox)` — AABB early-out
2. `Collide(primitive, vertexIndex, normal, hitPoint)` — triangle test
3. `PointInTriangle` — containment test via plane classification

### Collision Primitives

```
VICollSphere    ← Sphere vs world/entities
VICollRay       ← Ray cast for picking/hitscan
VICapsule       ← Capsule for character collision (radius + half-height)
VICylinder      ← Cylinder for volume tests
VISphere        ← Simple sphere (bounding volume)
VIPlane         ← Plane for classification
VIBBox          ← Axis-aligned bounding box
```

### Per-Sprite Collision Dispatch

Every sprite type implements virtual `Collide(sphere)` and `Collide(ray)`:

| Sprite Type | Collision Method |
|-------------|-----------------|
| VIHSprite | Traverses attachment hierarchy, transforms per bone |
| VICSprite | Uses VICapsule for character body |
| VIGroupSprite | Composes group transform, recurses children |
| VILODSprite | Delegates to current LOD level |
| VIFloraSprite | Stub (no collision) |
| VIParticleSprite | Stub (no collision) |
| VIPointLight | Sphere collision (lights have physical volume) |
| VINameSprite, VIPointSprite | Stub |

### World Integration

```
VIZone::Collide(VISceneCollVars)
├── SetPreTranslations(VICollide, VIVect3*)   ← Zone pre-translation
└── BSP traversal → CollideRoom
    ├── SetWorld(VICollide, Matrix44)          ← Room transform
    ├── CollideActor(VIScene, ...)             ← Entity collision
    └── CollideSprite(VIScene, ...)            ← Sprite collision
```

---

## 9. AMX/Pawn Scripting VM

### Standard Pawn VM (142 functions)

```
amx_Init          ← Initialize VM instance
  └── amx_BrowseRelocate  ← Relocate code at load time
amx_Exec          ← Execute script function
amx_Register      ← Register native C++ functions
amx_FindPublic    ← Look up script function by name
amx_FindPubVar    ← Look up script variable by name
amx_GetString     ← Get string from script memory
amx_SetString     ← Set string in script memory
amx_Allot         ← Allocate script memory
amx_GetAddr       ← Get pointer into script memory
amx_InitJIT       ← JIT compilation support!
amx_SetDebugHook  ← Debug hook for breakpoints
amx_SetCallback   ← Custom callback handler
amx_RaiseError    ← Trigger script error
amxRegisterNatives ← Register engine→script bridge
```

**Key finding**: The Pawn VM has **JIT compilation support** (`amx_InitJIT`). On PS2, this means Pawn scripts can be JIT-compiled to MIPS — significant for a native port since we'd need to either keep the MIPS JIT or recompile Pawn scripts for the target architecture.

---

## 10. Game Entity Layer (Engine/Game Boundary)

### Two Distinct Codebases

The recomp output reveals a clear boundary between engine and game code:

| Aspect | Engine (VI*) | Game Code |
|--------|-------------|-----------|
| Language style | C++ OOP | C-style free functions |
| Math types | VIVect3, VIMatrix44 | Point3, Matrix34 |
| Containers | VIPool, VIArray, VIList, VIMap | ListHead linked lists |
| Memory | VIPool allocators | blockAlloc (block allocator) |
| Naming | PascalCase methods | camelCase free functions |
| Prefix | VI* classes | object*, model*, world*, game* |

### createByName — Entity Factory (15.6 KB)

Constructs 100+ entity types from string name + position + tag parameters:

**Creatures**: Player1, Orc, Goblin, Skeleton, Mummy, Soul, NPC, Cyclops, SpiderQueen, VampireLord, Innoruuk, AntQueen, Demon, Ghoul, Wraith, Vampire, CloudGiant, SeaMonster, Arenabeast, MaleDarkElf, FemaleDarkElf, WoodElfSoldier, UndeadKnight, Froglock, Mermaid, etc.

**Props**: Chest, Lever, Switch, Teleporter, Torch, Candle, Gold, WeaponRack, DoorSecret, FloorSwitch, PushTrigger, MissileTrap, Catapult, Boat, Lamp, Lantern, Timer, Counter, etc.

**VFX Entities**: StaticFire, WaterSpout, LavaTractor, FireBomb, HateBridge, PokeReflector, Ice, Blocker, etc.

Factory pattern:
```
createByName(name, position, angle, tags)
├── cvProcess(tags)                        ← Parse tag key/value pairs
├── objectFindTagInt/String(tags, key)     ← Extract parameters
├── lumpFindResource(name)                 ← Find model/texture
├── new EntityType(position, angle, tags)  ← Construct
├── hasLightOrParticle(tags)               ← Attach light/particles
└── objectAddToSlowRunList(obj)            ← Register for updates
```

### Player::msg_run (27.5 KB — largest game function)

Per-frame player update handling ALL player state:

```
Player::msg_run
├── Movement: playerMove, playerEvadeHandler
├── Combat: playerAttackEnemy, playerDamageHandler, playerFindTarget
│   └── objectRadialDamage (AOE attacks)
├── Animation: animAddOneShot, animAddTransitionTo, playerAdvanceAnimation
├── Spells: castNewStyle, checkIfSpellIsRunning
│   └── SpellBash, SpellShieldBash, SpellAncestralCall
├── Items: playerItemScan, drinkPotion, playerRecomputeWeight
├── Effects: playerDrawWeaponEffects, playerProcessEffectTimers
│   └── P_AddParticle, LightEffect, UnholyAura, GroundPoundEffect
├── UI: hudSetInfoMessage, hudGetFadeIconPos
├── Network: netPlayerIsConnected, netPlayerIsLocal
├── Input: padGetAnalogButton, padBigRumble
└── Idle: playerPlayRandomIdle
```

### Creature Base Class (77 methods)

```
Creature (inherits Base → GameObject)
├── AI: enemyInZone, alternateEnemyInZone, flee2, findClearPath
│   └── getSmartRandomDestination, wallAndObjectSteering
├── Pathfinding: plotRoute, getCurrentRoutePoint, getNextRoutePoint
├── Movement: move, move2 (with world collision + water checks)
├── Combat: death, dropTreasure, creatureSlamEffect
├── Status: charm, confuse
├── Drawing: draw (modelDraw + shadows + glow effects + lighting)
├── Animation: creatureAdvanceAnimation, everyFrame
├── Events: msg_hurt, msg_alert, msg_collision, msg_collisionWorld
├── World: worldHitscan, worldFindStandHeight, worldCheckForWater
└── Clone: clone (for multiplayer entity duplication)
```

### Low-Level Data Structures (Game Layer)

The game layer uses underscore-prefixed structs for raw binary data:

| Struct | Purpose |
|--------|---------|
| `_modelHeader` | Model binary data (vertices, bones, animations) |
| `_worldHeader` | World geometry (BSP, floors, water) |
| `_texture` | Texture data (raw pixel data) |
| `_vagHeader` | Sony VAG audio format header |
| `_drawRecord` | Draw call record for batching |
| `AnimationState` | Current animation blend state |
| `AnimationHeader` | Animation clip data |

### World Interaction Functions (C-style API)

```
worldHitscan(worldHeader, start, end, flags, ...)
worldFindStandHeight(worldHeader, position, radius)
worldCheckForWater(worldHeader, position, radius, &waterHeight)
worldPerturbWater(worldHeader, position, radius, amplitude)
modelDraw(modelHeader, texture, flags, position, matrix, animState, ...)
modelDrawShadow(modelHeader, flags, matrix, animState, castShadow)
modelGetBoundingBox(modelHeader, ...)
modelGetShadowPos(modelHeader, animState, position, ...)
objectFindInBox(min, max, results, maxResults)
objectMoveWithWorldCollision(position, delta, radius, ...)
objectUpdateInGrid(gameObject)
```

These are the **direct descendants of Slavedriver's free functions** — same patterns (`HITSCAN.C` → `worldHitscan`, `OBJECT.C` → `objectFindInBox`, etc.).
