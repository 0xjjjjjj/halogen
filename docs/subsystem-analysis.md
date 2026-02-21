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

## 6. Atmosphere System

From the recomp file listing:

```
VIAtmosphere (28 methods, 21.1 KB)
├── RenderSky(VIScene, VICamera)          ← Sky dome
├── RenderStars(VIScene, VICamera)        ← Night sky stars
├── RenderWeather(VIScene, VICamera)      ← Rain/snow particles
├── RenderSplashes(VIScene, VICamera)     ← Rain splash effects
├── Clear(VIScene)
└── [24 more methods]
```

The atmosphere system renders **four layers**: sky dome, stars, weather particles, and ground splashes. In outdoor areas, this adds 4 additional render passes. Combined with indoor lighting, this explains performance differences between indoor/outdoor scenes.

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
