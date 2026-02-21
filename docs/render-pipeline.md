# VIScene Render Pipeline — Ghidra Decompilation (2026-02-21)

Decompiled from retail Champions of Norrath ELF (SLUS-20565) using Ghidra 11.4.2 + ghidra-emotionengine-reloaded. These are the core rendering functions PS2Recomp missed.

## Call Graph

```
VIScene::Render (0x0113bb48, 912 bytes)
├── VIRaster::SetTime
├── VIScene::ClearShadowQueue
├── VIRaster::SetProjection(camera.matrix)
├── VIScene::CalcOutdoorsIntensity
├── VIRaster::SetStaticLighting(WHITE)
├── VIAtmosphere::Update(scene, camera, time)
├── VIRadialFloraSystem::Update(camera.pos)          [portal mode only]
├── VIScene::GetEnvFlags(camera.pos)
├── VIWorld::CalcProfileBlend(camera.pos, blend)
├── VIScene::SetupTimeOfDay(camera, blend, envflags)
├── VIAtmosphere::RenderSky(scene, camera)
├── VIScene::SetupTimeOfDayFog(blend, envflags)
├── VIRaster::SetModelView(camera.viewmatrix)
├── VIClipStack::Reset
├── VIVector<VISceneDisplayElem>::Init(1000)
│
├── BRANCH on scene[0x12e5]:
│   ├── 0 → VIWorld::RenderByFrustum(world, rendvars)     ← outdoor
│   └── 1 → VIWorld::RenderByPortals(world, rendvars)     ← indoor/caves
│
├── VIScene::RenderDeferredList(cam, 0, 1)                 ← opaque pass
├── VIRadialFloraSystem::Render(cam)                       [portal mode only]
├── VIScene::RenderDeferredList(cam, 1, 0)                 ← transparent pass
├── frame_counter++
├── VIScene::UpdateSoundEmitters(cam)
├── VINameSprite::RasterDeferred(raster)                   ← NPC name labels
├── VIParticleSystem::Render(time, raster)                 ← particles
├── VIRaster::SetModelView(camera.viewmatrix)              ← reset after particles
├── VIScene::RenderShadows
├── VISpellEffectSystem::Process
├── VIRaster::EnableAllLights(0)                           ← disable all lights
├── VITrailFxRender(time, raster, camera)                  ← spell trails
├── VIAtmosphere::RenderWeather(scene, camera)             ← rain/snow (last)
├── VIRaster::SetStaticLighting(WHITE)                     ← reset lighting
└── return 0 (success) or -1 (failure)
```

### Render Order

1. Sky
2. World geometry (portals or frustum)
3. Deferred opaque pass
4. Flora/grass
5. Deferred transparent pass
6. NPC name labels
7. Particles
8. Shadows
9. Spell effects
10. Disable all dynamic lights
11. Trail FX
12. Weather (rain/snow)

### VU1 Upload → Execute Pipeline

```
CalcMatrices(raster)                         ← build scratchpad matrices
├── UploadMatrices(raster, dmaTag)           ← pack 21 QWs → VU1 addr 0-20
│   └── trailing MSCAL(RInitOffset)          ← kick RasterMicro
├── DrawPrimBufferTessPackVUNCG(...)          ← tessellated point light geometry
│   ├── TessTriangle per lit triangle        ← subdivide + repack VUNCG
│   └── MSCAL per bone group                 ← kick VU1 per batch
└── BeginBillboards / EndBillboards          ← particle billboard path
    ├── BeginBillboards: upload BillboardMicro + DMA BASE/OFFSET
    └── EndBillboards: MSCAL(0x14)           ← kick BillboardMicro
```

### Key State

- `scene[0x12e5]`: Indoor/outdoor mode flag. 1 = portal rendering, 0 = frustum culling.
- `scene[0x12e7]`: VIRaster pointer.
- `scene[0x120]`: Current time (for animation/ToD).
- `scene[0x544]`: Frame counter (prevents double-rendering).
- `0x3f800000` = 1.0f — static lighting reset to full white as base, Time of Day modulates it.

---

## VIWorld::RenderByPortals (0x10fb9d0, 376 bytes)

Entry point for indoor/cave rendering. Locates camera in BSP, dispatches to portal or frustum path.

```
RenderByPortals(world, rendvars)
├── rendvars.world = world
├── Early exit: world[0x34] == 0 && world[0x3c] != 0 → skip
├── FindLeaf(world, camera.pos, &cellIndex, &leafIndex)
│   └── BSP traversal to find camera's cell + leaf
├── cell = world.cells[cellIndex]
│   └── cells at world+0x4C, each 0x250 bytes (592 bytes)
├── room = cell.portals[leafIndex]
│   └── portal table at cell+0x50
│
├── CHECK room.flags & 1:
│   ├── outdoor → FALLBACK to RenderByFrustum
│   └── indoor → continue
│
├── INDOOR PATH:
│   ├── rendvars.cellIndex = cellIndex
│   ├── VIZone::SetPretranslations(cell, raster, camera)
│   ├── VIClipStack::PushFrustum(clipstack, camera)
│   ├── VIClipStack::GetTop → get clip planes/verts/edges
│   ├── VIZone::RenderRoom(cell, roomIndex, rendvars)
│   └── VIClipStack::Pop
└── return 0 or -1
```

### Cell Structure

Each cell is 0x250 bytes (592 bytes), stored in array at `world+0x4C`.

---

## VIZone::RenderRoom (0x11164d8, 520 bytes)

Renders a single BSP room: portal neighbors first, then static geometry, then actors.

```
RenderRoom(zone, roomIndex, rendvars)
├── FRUSTUM CULL: CullByTop(clipstack, room.bbox)
│   └── culled → return 0 (not an error)
│
├── RenderThroughPortals(zone, roomIndex, rendvars)
│   └── Recursive — renders visible neighboring rooms first
│
├── FRAME STAMP CHECK:
│   room[0x24] == scene.frameCount → already rendered, skip
│   room.flags & 2 → disabled room, skip
│
├── STATIC GEOMETRY:
│   ├── spriteIndex = room[0x1C]  (0xFFFFFFFF = none)
│   ├── sceVu0CopyMatrix(zone+0x90, camera.viewmatrix)
│   ├── SetModelView(raster, zone_matrix)
│   ├── SetStaticLighting(raster, WHITE)
│   ├── RasterSprite(scene, camera, spriteIndex, 1)
│   └── Add to deferred display list
│
├── DISTANCE CHECK:
│   DistanceSquared(room.bbox, camera.pos) < maxDist²
│
└── ACTOR LOOP (linked list at room+0x68):
    └── while actor_node != -1:
        ├── RasterActor(scene, camera, actor.id, clipstack)
        └── actor_node = actor_node.next
```

### Room Structure (0x78 = 120 bytes)

Array at `zone+0x60`, indexed by room number.

| Offset | Size | Field |
|--------|------|-------|
| +0x00 | 4 | flags (bit 0 = outdoor fallback, bit 1 = disabled) |
| +0x04 | 24 | BBox (bounding box for frustum culling) |
| +0x1C | 4 | spriteIndex (static geometry handle, -1 = none) |
| +0x24 | 4 | frameStamp (prevents double-render per frame) |
| +0x4C | 4 | portalCount |
| +0x50 | 4 | portalLookupTable ptr |
| +0x5C | 4 | portalArray ptr |
| +0x60 | 4 | portalVertexBase ptr |
| +0x68 | 4 | actorListHead (linked list) |

---

## VIZone::RenderThroughPortals (0x11166e0, 628 bytes)

Classic portal rendering algorithm. For each portal in the room, tests visibility and recursively renders the target room through the narrowed frustum.

```
RenderThroughPortals(zone, roomIndex, rendvars)
├── room = zone.rooms[roomIndex]
├── portalCount = room[0x4C]
├── portalArray = room[0x5C]
├── vertexBase = room[0x60]     ← packed VIVect3 vertex arrays
│
└── for i in 0..portalCount:
    ├── portal = portalArray[i]                 ← each 0x20 bytes
    │
    ├── SKIP if portal.flags & 1                ← visited (cycle prevention)
    │
    ├── PLANE TEST:
    │   dot = camera.pos · portal.normal + portal.d
    │   → skip if dot < 0 (camera behind portal)
    │
    ├── CLIP TEST (if dot >= 0.02):
    │   ClipByTop(clipstack, vertexCount, vertices)
    │   → skip if portal fully outside frustum
    │
    ├── TARGET ROOM CHECK:
    │   target.flags & 1 (outdoor) → RenderByFrustum fallback
    │
    ├── NEAR-PLANE PATH (dot < 0.02):
    │   → render target room without frustum narrowing
    │   (portal too close to camera to clip properly)
    │
    ├── STANDARD PATH (dot >= 0.02):
    │   ├── portal.flags |= 1          ← mark visited
    │   ├── PushPortal(clipstack, camera, verts)
    │   │   └── Narrow frustum to portal aperture
    │   ├── RenderRoom(zone, targetRoom, rendvars)  ← RECURSIVE
    │   ├── Pop(clipstack)              ← restore frustum
    │   └── portal.flags &= ~1         ← unmark visited
    │
    └── vertexBase += vertexCount × 12  ← advance packed vertices
```

### Portal Structure (0x20 = 32 bytes)

| Offset | Size | Field |
|--------|------|-------|
| +0x00 | 4 | normal.x |
| +0x04 | 4 | normal.y |
| +0x08 | 4 | normal.z |
| +0x0C | 4 | plane distance (d) |
| +0x10 | 4 | (unknown) |
| +0x14 | 4 | vertexCount |
| +0x18 | 4 | targetRoomIndex |
| +0x1C | 4 | flags (bit 0 = visited/disabled) |

### Portal Vertex Data

Vertices are packed sequentially in a separate array (room+0x60). Each vertex is 12 bytes (VIVect3 = 3 floats: x, y, z). Portal i's vertices start after portal i-1's vertices.

### Cycle Prevention

The visited flag (bit 0) is set before recursing into a target room and cleared after returning. This prevents infinite loops in rooms that have portals pointing back at each other.

### Near-Plane Handling

When the camera is very close to a portal (dot product < 0.02), the portal polygon can't be reliably clipped against the frustum. In this case, the target room is rendered without frustum narrowing — essentially treating the portal as fully open.

---

## VIScene::RasterActor (0x11420c0, 492 bytes)

Renders a single actor (entity). This is where per-vertex dynamic lighting gets applied through the virtual render dispatch.

```
RasterActor(scene, camera, actor, clipstack)
├── FRAME STAMP: actor[0x80] == scene.frameCount → skip
├── FLAGS: actor[0x40] & 5 → skip if hidden (bit 0) or disabled (bit 2)
│
├── DISTANCE:
│   dist² = |actor.pos - camera.pos|²
│   actor.pos at actor+0x44 (x), +0x48 (y), +0x4C (z)
│
├── TYPE LOOKUP:
│   typeIndex = actor[0x60]
│   type = scene.typeTable[typeIndex]
│   └── table at scene+0x3EC, stride 0xC
│   maxDist = type[0x30]
│   → skip if dist² > maxDist²
│
├── FRUSTUM CULL:
│   CullByTop(clipstack, actor.boundingSphere)
│   └── sphere at actor+0x88
│
├── TRANSFORM:
│   tempMatrix = actor.matrix × camera.viewmatrix
│   SetModelView(raster, tempMatrix)
│
├── SHADOW CASTER CHECK (type[0x34] == 5):
│   if dist² < scene.shadowDist (scene+0x187C):
│     shadowList[count++] = actor    ← max 128 shadow casters
│     └── list at scene+0x1888, count at scene+0x1A88
│
├── PER-ACTOR STATIC LIGHTING:
│   scene[0x444] = actor.spriteHandle
│   SetStaticLighting(raster, actor+0x70)
│   └── Each actor carries its own baked light color
│
├── VIRTUAL RENDER DISPATCH:                    ← THE BOTTLENECK
│   vtable = type[0x3C]
│   renderFunc = vtable[0x1C]
│   renderFunc(type + vtable[0x18], camera, scene, raster, 1)
│   └── Dispatches to VIHSprite::Raster, VIParticleSprite, etc.
│   └── VIPointLight/VIColorBuffer applied INSIDE this call
│
└── Add to deferred display list if rendered
```

### Actor Structure (partial)

| Offset | Size | Field |
|--------|------|-------|
| +0x40 | 4 | flags (bit 0 = hidden, bit 2 = disabled) |
| +0x44 | 4 | position.x |
| +0x48 | 4 | position.y |
| +0x4C | 4 | position.z |
| +0x60 | 4 | typeIndex (into scene type table) |
| +0x6C | 4 | spriteHandle |
| +0x70 | 16 | staticLightColor (VIColor32F: r,g,b,a) |
| +0x80 | 4 | frameStamp |
| +0x88 | 16 | boundingSphere (x,y,z,radius) |

### Actor Type Structure (partial)

Type table at `scene+0x3EC`, entries spaced 0xC apart, pointing to type data.

| Offset | Size | Field |
|--------|------|-------|
| +0x30 | 4 | maxDrawDistance (float) |
| +0x34 | 4 | typeClass (5 = shadow caster) |
| +0x3C | 4 | vtable pointer |

### Virtual Render Dispatch

`vtable[0x1C]` is the render method. Different actor types override this:
- VIHSprite (characters): bone animation + skinning
- VIParticleSprite (effects): billboard particle rendering
- VICSprite (simple objects): static mesh rendering

The per-vertex VIPointLight/VIColorBuffer lighting overlay happens inside these virtual render methods. Each dynamic light triggers a VIColorBuffer lock → per-vertex color compute → unlock → geometry re-render cycle. With N lights affecting an actor, this is N× overdraw.

---

## VIScene::RasterSprite (0x1144bf8, 100 bytes)

Pure virtual dispatch — the unified render interface for both room geometry and actors.

```
RasterSprite(scene, camera, spriteIndex, renderMode)
├── raster = scene[0x4B9C]
├── if (!raster) return -1
├── type = scene.typeTable[spriteIndex]
│   └── table at scene+0x3EC, stride 0xC
├── vtable = type[0x3C]
└── return vtable[0x1C](type + vtable[0x18], camera, scene, raster, renderMode)
```

Same virtual dispatch as RasterActor. The type table at `scene+0x3EC` is the unified render interface for all drawable objects. `renderMode` values:
- 1 = immediate (from RenderRoom during portal/frustum traversal)
- 2 = deferred (from RenderDeferredList replay)

---

## VIWorld::RenderByFrustum (0x10fb910, 188 bytes)

Outdoor rendering path. Thin wrapper around RenderByVolume with full camera frustum.

```
RenderByFrustum(world, rendvars)
├── rendvars[0x28] = 1              ← flag: frustum mode active
├── rendvars.world = world
├── Early exit check (same as RenderByPortals)
├── PushFrustum(clipstack, camera)  ← full camera frustum, no portal narrowing
├── GetTop → clip planes/verts/edges
├── RenderByVolume(world, rendvars) ← renders all visible geometry
├── Pop(clipstack)
└── return 0 or -1
```

No BSP cell lookup, no portal traversal. Pushes the full camera frustum and renders everything visible via RenderByVolume. Also used as fallback when portal rooms have the outdoor flag set.

---

## VIScene::RenderDeferredList (0x1142e80, 692 bytes)

Display list replay system. During portal/frustum traversal, visible objects are collected into a list. This function replays that list in two separate passes.

```
RenderDeferredList(scene, camera, renderActors, renderRoomSprites)
├── displayCount = scene[0x458]
├── displayList  = scene[0x460]     ← array of 0xC-byte elements
│
└── for each element:
    ├── element[0] = cellIndex      (-1 = same cell as previous)
    ├── element[4] = actor ptr      (-1 = room sprite, else actor)
    ├── element[8] = typeIndex
    │
    ├── if cellIndex changed:
    │   └── SetPretranslations(cells[cellIndex], raster, camera)
    │
    ├── ROOM SPRITE PATH (actor == -1, renderRoomSprites flag set):
    │   ├── CopyMatrix(camera.viewmatrix)
    │   ├── SetModelView(raster, matrix)
    │   ├── SetStaticLighting(raster, WHITE)
    │   └── vtable->Render(type, cam, scene, raster, 2)
    │
    └── ACTOR PATH (actor != -1, renderActors flag set):
        ├── Mul(matrix, actor.matrix, camera.viewmatrix)
        ├── SetModelView(raster, matrix)
        ├── SetStaticLighting(raster, actor+0x70)  ← per-actor light color
        ├── vtable->Render(type, cam, scene, raster, 2)
        └── Clear actor refs (scene[0x444], scene[0x448] = -1)
```

### The Two Passes (called from VIScene::Render)

| Call | renderActors | renderRoomSprites | What It Draws |
|------|-------------|-------------------|---------------|
| `RenderDeferredList(cam, 0, 1)` | 0 (skip) | 1 (draw) | Room static geometry only |
| `RenderDeferredList(cam, 1, 0)` | 1 (draw) | 0 (skip) | Actors only |

Full render sequence:
1. Immediate pass — RenderRoom draws rooms + actors during portal/frustum traversal (mode=1)
2. Deferred pass 1 — Re-render room sprites (mode=2)
3. Flora (VIRadialFloraSystem)
4. Deferred pass 2 — Re-render actors (mode=2)

Mode 1 vs 2 likely controls alpha/depth behavior — immediate pass writes depth, deferred pass handles transparency or multi-pass lighting effects.

### Display Element Structure (0xC = 12 bytes)

| Offset | Size | Field |
|--------|------|-------|
| +0x00 | 4 | cellIndex (-1 = unchanged from previous element) |
| +0x04 | 4 | actor ptr (-1 = room sprite) |
| +0x08 | 4 | typeIndex (into scene type table) |

Max 1000 elements (initialized in VIScene::Render).

---

## VIWorld::RenderByVolume (0x10fbb48, 644 bytes)

World-level BSP tree traversal. Recursively splits the world, dispatching to VIZone when a leaf is reached.

```
RenderByVolume(world, nodeIndex, rendvars)
├── NODE INDEX ENCODING (upper bits):
│   ├── bit 30 (0x40000000) = LEAF
│   │   ├── cellIndex = world.leafMap[nodeIndex & 0xFFFFFFF]
│   │   │   └── leafMap at world+0x40
│   │   └── VIZone::RenderByVolume(cells[cellIndex], rendvars, cellIndex)
│   └── otherwise: strip flags, treat as BSP interior node
│
├── BSP NODE (0x18 = 24 bytes, array at world+0x38):
│   plane: normal(x,y,z) + distance d
│   frontChild at +0x10, backChild at +0x14
│
├── FRUSTUM vs PLANE TEST:
│   for each clip vertex:
│     dot = vertex · plane.normal + plane.d
│     positive → verts on front side
│     negative → verts on back side
│
├── CAMERA POSITION TEST:
│   dot = camera.pos · plane.normal + plane.d
│
└── TRAVERSAL (back-to-front / painter's order):
    ├── Camera on NEGATIVE side:
    │   ├── if verts on positive: recurse frontChild    ← far side first
    │   ├── if no verts on negative: return             ← frustum doesn't reach us
    │   └── recurse backChild                           ← near side second
    └── Camera on POSITIVE side:
        ├── if verts on negative: recurse backChild     ← far side first
        ├── if no verts on positive: return             ← frustum doesn't reach us
        └── recurse frontChild                          ← near side second
```

---

## VIZone::RenderByVolume (0x11155b0, 628 bytes)

Zone-level BSP traversal. Same algorithm as VIWorld, but operating within a single cell. Leaves dispatch to RenderLeaf for actual room geometry.

```
RenderByVolume(zone, nodeIndex, rendvars)
├── NODE INDEX ENCODING:
│   ├── bit 30 = LEAF → RenderLeaf(zone, nodeIndex & 0xFFFFFFF)
│   └── otherwise: BSP interior node traversal
│
├── BSP NODE (0x18 bytes, array at zone+0x48):
│   Same structure as VIWorld nodes
│
└── TRAVERSAL: identical back-to-front logic
```

### BSP Node Structure (0x18 = 24 bytes, shared by World and Zone)

| Offset | Size | Field |
|--------|------|-------|
| +0x00 | 4 | plane.normal.x |
| +0x04 | 4 | plane.normal.y |
| +0x08 | 4 | plane.normal.z |
| +0x0C | 4 | plane.d (distance) |
| +0x10 | 4 | frontChild (positive side, upper bits = flags) |
| +0x14 | 4 | backChild (negative side, upper bits = flags) |

### Node Index Flag Encoding

| Bits | Meaning |
|------|---------|
| 0-27 | Node/leaf index |
| 30 | Leaf flag — stop recursing, dispatch to geometry |
| 28-31 | Reserved flags |

---

## VIZone::RenderLeaf (0x1119330, 128 bytes)

Leaf resolver — maps BSP leaf index to room, then dispatches to RenderRoom.

```
RenderLeaf(zone, leafIndex, rendvars)
├── roomIndex = zone.leafToRoom[leafIndex]
│   └── leafToRoom at zone+0x50, entries 8 bytes apart
├── room = zone.rooms[roomIndex]
│   └── rooms at zone+0x60, each 0x78 bytes
│
├── FRAME STAMP: room[0x20] == rendvars[0] → already visited, skip
│   └── Set room[0x20] = rendvars[0] (mark visited)
│
├── RENDER CONDITION:
│   ├── room.flags & 1 (outdoor) → always render
│   └── OR rendvars[0x2C] != 0 (frustum mode active) → render
│
└── RenderRoom(zone, roomIndex, rendvars)
```

### Indoor/Outdoor Path Convergence

Both rendering paths converge at VIZone::RenderRoom:

```
INDOOR:  RenderByPortals → FindLeaf → RenderRoom ←→ RenderThroughPortals (recursive)
OUTDOOR: RenderByFrustum → VIWorld BSP → VIZone BSP → RenderLeaf → RenderRoom
```

### Two-Level BSP Hierarchy

The outdoor renderer uses a two-level BSP:

```
VIWorld BSP (world+0x38, leaves via world+0x40)
  ├── Interior nodes: split world into regions
  └── Leaves (bit 30): map to VIZone cells
        └── VIZone BSP (zone+0x48)
              ├── Interior nodes: split cell into sub-regions
              └── Leaves (bit 30): RenderLeaf → room geometry + actors
```

### Traversal Order

Both levels use **back-to-front** (painter's algorithm): visit the far side of the splitting plane first, then the near side. This ensures correct draw order for transparency on PS2.

---

## VIHSprite::Raster (0x1060548, 632 bytes)

Character bone animation renderer. Doesn't draw geometry directly — coordinates bone transforms and dispatches body parts through RasterSprite.

```
Raster(sprite, camera, scene, raster, renderMode)
├── CalcLODLevelIndex(sprite, modelview)       ← LOD selection
├── Process(sprite, lodLevel, scene)           ← update animation
├── CalcTransAboutCenter(sprite, modelview, scene, centerMatrix)
├── SetBlendMatrices(sprite, raster)           ← upload bone matrices
│
└── for each attachment in VIPool<VIHSpriteAttachment> (sprite+0x60):
    ├── spriteIndex = attachment[0x00]
    ├── boneIndex   = attachment[0x04]
    │
    ├── boneIndex == -1 → SetModelView(centerMatrix), RasterSprite(spriteIndex)
    └── boneIndex != -1 → Mul(boneMatrix[bone*0x100+0x30]),
                           SetModelView(boneMatrix), RasterSprite(spriteIndex)
```

Each bone is 0x100 bytes (256 bytes), transform matrix at +0x30 within bone data. Body parts (head, torso, arms, legs, weapon, shield) are separate sprites attached to bones.

---

## CalcOutdoorsIntensity (0x1143940, 408 bytes)

Vertical ground-probe ray cast to detect indoor/outdoor status for lighting transitions.

```
CalcOutdoorsIntensity(scene, camera)
├── Ray: camera.pos → camera.pos with y-15  (15 units straight down)
├── Filter: VISceneOutdoorsFilter
├── Pick(scene, ray, filter)
└── if hit:
    ├── First time: scene[0x1AC0] = hitColor.alpha (outdoor intensity)
    └── Subsequent: smooth transition at 0.2/sec max rate
        delta = clamp(newAlpha - currentAlpha, ±timeDelta*0.0002)
```

Rate-limited to prevent jarring indoor↔outdoor lighting pops (~5 sec full transition).

---

## SetupTimeOfDay (0x1145948, 92 bytes)

Dispatcher for three Time-of-Day subsystems:

```
SetupTimeOfDay(scene, camera, terrainBlend, envFlags)
├── SetupTimeOfDayLights(scene, camera, terrainBlend)
├── SetupTimeOfDayFog(scene, terrainBlend, envFlags)
└── SetupTimeOfDaySky(scene, terrainBlend)
```

---

## Lighting System

### VIPointLight::Raster (0x10c3aa8, 256 bytes)

Renders the light's visual glow sprite — NOT the per-vertex lighting computation.

```
Raster(light, camera, scene, raster, flags)
├── sprite = GetLightUISprite(scene)
├── if (sprite == -1) return        ← no visual representation
├── Copy current model-view matrix
├── ClampScale(light, matrix)       ← scale to light radius
├── SetModelView(raster, matrix)
└── RasterUISprite(scene, camera, sprite, flags)  ← draw glow billboard
```

### VIColorBuffer::Lock / Color / Unlock — The Per-Vertex DMA Engine

The actual cave bottleneck. VIColorBuffer builds PS2 DMA packets that upload per-vertex colors to the GS via VIF→VU1→GIF.

#### Lock (0x10c0728, 152 bytes)

```
Lock(colorbuffer, raster)
├── Set locked = 1
├── pBuildSource = PrimBuffer(raster, format)
├── Calculate initial DMA tag position
└── Reset all build counters
```

#### Color (0x10bffa8, 1,220 bytes) — Called once per vertex

```
Color(colorbuffer, rgba)
├── BATCH MANAGEMENT:
│   Track mesh batches (M) and primitive groups (P)
│   Advance through source geometry vertex layout
│
├── DMA PACKET CONSTRUCTION:
│   ├── 0x30 = VIF DIRECT (send to GS)
│   ├── GIFtag: PACKED mode, RGBAQ register
│   ├── VIF MSCAL (kick VU1 microcode)
│   └── VIF end marker (0x60)
│
├── COLOR WRITE:
│   output[0] = R >> 1    ← game: 0-255, GS: 0-128
│   output[1] = G >> 1
│   output[2] = B >> 1
│   output[3] = A >> 1
│
└── PRIMITIVE COMPLETION (when group finishes):
    ├── Write RStrip2Offset (triangle strip kick)
    ├── Write VIF MSCAL (execute VU1 program)
    └── Pad to 16-byte alignment
```

**Critical**: Build state variables (`_13VIColorBuffer$Build*`) are **static/global**. Only one VIColorBuffer can build at a time — sequential lock-per-light is mandatory.

#### Unlock (0x10c07c0, 100 bytes)

```
Unlock(colorbuffer)
├── Set locked = 0
└── Zero all static build variables
```

### VIRaster::SetStaticLighting (0x11141a0, 48 bytes)

Writes lighting color to PS2 scratchpad RAM (single-cycle access):

```
SetStaticLighting(raster, color)
└── Write 16 bytes (VIColor32F) to scratchpad 0x70000200
```

### VIRaster::EnableAllLights (0x1114170, 48 bytes)

Controls 3 light slot enables in scratchpad:

```
EnableAllLights(raster, enable)
├── scratchpad[0x220] = enable   (light slot 0)
├── scratchpad[0x221] = enable   (light slot 1)
├── scratchpad[0x222] = enable   (light slot 2)
└── raster+0x45E0 = 1           (lights-changed flag)
```

### PS2 Scratchpad as VU1 Parameter Block

The 16KB scratchpad (0x70000000-0x70003FFF) stores render state read by VU1 microcode:

| Address | Size | Contents |
|---------|------|----------|
| 0x70000200 | 16 | Static lighting color (VIColor32F) |
| 0x70000220 | 1 | Light slot 0 enable |
| 0x70000221 | 1 | Light slot 1 enable |
| 0x70000222 | 1 | Light slot 2 enable |

---

## VIScene::RenderShadows (0x1144ac0, 108 bytes)

Iterates the shadow caster list collected during RasterActor:

```
RenderShadows(scene)
├── count = scene[0x1A88]    (max 128)
├── list = scene+0x1888
└── for each: RenderShadow(scene, actor)
```

---

## Cave Performance Bottleneck — Full Trace

The complete call path from scene to the bottleneck:

```
VIScene::Render
  └── RenderByPortals
        └── FindLeaf → locate camera cell/room
              └── RenderRoom
                    ├── RenderThroughPortals → recursive portal neighbors
                    ├── RasterSprite → room static geometry
                    └── Actor loop:
                          └── RasterActor
                                ├── SetStaticLighting(actor.color)  → scratchpad 0x70000200
                                └── vtable->Render()
                                      └── For each nearby VIPointLight:
                                            ├── VIColorBuffer::Lock (get DMA buffer)
                                            ├── VIColorBuffer::Color × N vertices
                                            │   └── Build DMA packets, write RGBA >> 1
                                            ├── VIColorBuffer::Unlock (finalize)
                                            └── Submit DMA → VIF → VU1 → GIF → GS
                                              └── Re-render geometry with light colors
```

In a cave with 10 torches:
- Each torch = VIParticleSprite (billboard particles) + VIPointLight
- Each VIPointLight triggers: Lock → Color×N_vertices → Unlock → DMA submit → re-render
- VIColorBuffer build state is GLOBAL — lights are processed sequentially
- 10 torches × (20 particles + per-vertex color build + geometry re-render) = 400+ draw ops
- Color() alone: 500 vertices × 10 lights = 5,000 calls, each building DMA command words

### Why It's Slow (PS2-Specific)

1. **Sequential**: Global static build state → one light at a time
2. **Per-vertex**: Color() called once per vertex per light, not batched
3. **DMA overhead**: Each light pass builds a full VIF→VU1→GIF DMA chain
4. **Geometry re-render**: Each light re-submits ALL affected geometry through the pipeline
5. **No accumulation**: Can't blend multiple lights in one pass (hardware limitation)

### Native Port Fix

Replace the entire VIColorBuffer mechanism:
- **Delete**: Lock/Color/Unlock/DMA packet building
- **Replace with**: Uniform buffer of light positions + colors
- **Per-pixel lighting**: Fragment shader evaluates all lights in one pass
- **Intercept point**: The vtable dispatch in RasterActor (vtable[0x1C])
- **Result**: 10 lights = 1 draw call with 10-light fragment shader, not 10 draw calls

---

## VISceneRendVars Structure

Passed through the render pipeline as the rendering context.

| Offset | Size | Field |
|--------|------|-------|
| +0x04 | 4 | scene ptr |
| +0x08 | 4 | world ptr |
| +0x0C | 4 | camera ptr |
| +0x10 | 4 | raster ptr |
| +0x14 | 4 | clipstack ptr |
| +0x18 | 4 | clip verts ptr |
| +0x1C | 4 | clip edges ptr |
| +0x20 | 4 | clip verts2 ptr |
| +0x24 | 4 | clip planes ptr |
| +0x28 | 4 | (flag/mode) |
| +0x30 | 4 | cellIndex |
| +0x34 | 4 | maxRenderDist (float) |

---

## VIZone::SetPretranslations (0x1115828, 204 bytes)

PS2 floating-point precision fix. Shifts coordinate system so geometry is near-origin relative to camera.

```
SetPretranslations(zone, raster, camera)
├── for each position in zone+0x58 (count at zone+0x54):
│   output = source - camera.pos
└── VIRaster::SetPreTranslations(raster, count, outputs, camera.pos)
```

---

## VIRaster::SetProjection (0x1112f60, 60 bytes)

Copies projection matrix to PS2 scratchpad and sets dirty flags.

```
SetProjection(raster, matrix)
├── sceVu0CopyMatrix(0x70000040, matrix)   ← scratchpad
├── raster+0x45E4 = 1                      ← projection dirty
└── raster+0x45E0 = 1                      ← state dirty
```

---

## VIAtmosphere::RenderSky (0x1067f38, 652 bytes)

Multi-layer sky dome rendering.

```
RenderSky(atmosphere, scene, camera)
├── Copy camera matrix, zero translation (sky at infinity)
├── Sky dome sprite: atm[0x4E0], render mode=3
├── Cloud layers (×3, if enabled):
│   ├── Cloud 1: transform atm+0x500, sprite atm[0x4EC]
│   ├── Cloud 2: transform atm+0x540, sprite atm[0x4F0]
│   └── Cloud 3: transform atm+0x580, sprite atm[0x4F4]
└── RenderStars (if not transitioning)
```

Render mode 3 = sky-specific (no depth write, alpha blending).

---

## VIAtmosphere::RenderWeather (0x10681c8, 1,464 bytes)

Billboard particle rain/snow system.

```
RenderWeather(atmosphere, scene, camera)
├── visibleCount = maxParticles × intensity, clamped
├── viewAngle = 1 - dot(frustumNormal, normalize(frustumNormal.xz))
├── for each particle (array at atm+0x0C, each 0x24 bytes):
│   ├── pos += windOffset
│   ├── size = baseSize × scale × viewAngleFactor
│   ├── near-plane cull: hide if behind camera
│   └── write to billboard batch
├── BeginBillboards / EndBillboards (batched rendering)
└── RenderSplashes (ground impacts)
```

Two material paths: single material for uniform weather, two-material split for heavy/light gradient. View angle factor makes rain look natural when looking up vs horizontal.

---

## VIRaster::SetModelView (0x1112f20, 56 bytes)

Copies model-view matrix to scratchpad and sets dirty flags.

```
SetModelView(raster, matrix)
└── sceVu0CopyMatrix(0x70000000, matrix)
```

---

## VIRaster::SetMaterial (0x1113888, 68 bytes)

Appends material setup commands to DMA chain.

```
SetMaterial(raster, materialId)
├── AddMaterial(raster, materialId, &dmaBufPtr)
└── FlushDMABufferIfFull(raster)
```

---

## VIHSprite::SetBlendMatrices (0x1062ee0, 368 bytes)

Computes and uploads bone skinning matrices.

```
SetBlendMatrices(sprite, raster)
├── Scan attachments for unboned parts (boneIndex == -1)
├── For each bone (count at sprite+0x40):
│   ├── bone = sprite+0x48 + i * 0x100
│   └── output[i] = bone.inverseBindPose × bone.currentTransform
└── SetObjectBlends(raster, boneCount, blendMatrices)
```

### Bone Data (0x100 = 256 bytes per bone)

| Offset | Size | Field |
|--------|------|-------|
| +0x30 | 64 | Current transform (animated) |
| +0xA0 | 64 | Inverse bind pose |

Output blend matrices at sprite+0x54, each 0x40 bytes (4x4 matrix). Standard `invBindPose × animTransform` skinning.

---

## VIRaster::BeginBillboards (0x110cb90, 1,616 bytes)

Sets up VU1 BillboardMicro program and builds DMA packet for batched billboard rendering (particles, weather, sprites).

```
BeginBillboards(raster, &outputBuffer, batchSize)
├── Clamp batchSize to 80 max
├── Upload BillboardMicro VU1 program if not loaded
│   (raster+0x4C4C: 0/1=RasterMicro, 2=BillboardMicro)
├── If matrices dirty:
│   ├── CalcMatrices(raster)
│   ├── Build 0x340-byte DMA packet:
│   │   ├── ModelView from scratchpad 0x70000000
│   │   ├── Clip/viewport from scratchpad 0x70000080-0x700000C0
│   │   ├── Projection × Viewport matrix
│   │   ├── GIFtags for GS register setup
│   │   ├── Billboard corner lookup (8 configs × 4 corners)
│   │   ├── Static lighting color
│   │   └── VIF MSCAL — kick VU1
│   └── FlushDMABufferIfFull, clear dirty flag
├── Write per-batch VIF header with billboard count
└── *outputBuffer = billboard data start
```

### VU1 Program Selection (raster+0x4C4C)

| Value | Program | Used For |
|-------|---------|----------|
| 0/1 | RasterMicro | Geometry, characters, world |
| 2 | BillboardMicro | Particles, weather, billboards |

---

## VU1 Microcode Upload

### UploadRasterMicro (0x1112460, 232 bytes)

Uploads geometry processing VU1 program via DMA ref to DVP overlay data.

```
UploadRasterMicro(raster, &dmaPtr)
├── DMA cnt: VIF STCYCL
├── DMA ref → &.dma.1 (VU1 microcode from DVP overlay section)
├── DMA cnt: VIF double-buffer setup
│   ├── VIF BASE = PrimBuffer1
│   └── VIF OFFSET = PrimBuffer2 - PrimBuffer1
└── raster+0x4C4C = 1 (RasterMicro active)
```

### UploadBillboardMicro (0x1112548, 196 bytes)

Uploads billboard VU1 program.

```
UploadBillboardMicro(raster, &dmaPtr)
├── DMA cnt: VIF STCYCL
├── DMA ref → &.dma.1 (billboard microcode)
├── DMA cnt: VIF double-buffer setup
│   ├── VIF BASE = 0x21A
│   └── VIF OFFSET = 0xF0 (240 bytes)
└── raster+0x4C4C = 2 (BillboardMicro active)
```

Both use DMA double-buffering: EE fills one VU1 data buffer while VU1 processes the other.

---

## CalcMatrices (0x1114388, 176 bytes)

Computes the complete matrix pipeline and stores in scratchpad.

```
CalcMatrices(raster)
├── scratchpad[0x080] = ModelView × Projection              (MVP)
├── scratchpad[0x140] = MVP × Viewport                      (clip-to-screen)
├── scratchpad[0x100] = Inverse(ModelView)                   (world→object)
├── scratchpad[0x180] = normalize(InvMV.subMul(0x1A0))      (direction)
└── if light2 enabled:
    └── scratchpad[0x190] = InvMV × scratchpad[0x1C0]       (light→object)
```

---

## VIRaster::EndBillboards (0x0110d1e0, 224 bytes)

Counterpart to BeginBillboards. Finalizes the billboard DMA packet and kicks VU1.

```
EndBillboards(raster):
    if billboardCount <= 0: return -1     // nothing to flush

    // Mark end-of-packet on last billboard DMA entry
    lastEntry = dmaPtr + billboardCount * 0x30
    lastEntry.flags |= 0x100              // EOP (end of packet)

    // Append MSCAL VIF command → kicks VU1 BillboardMicro at entry 0x14
    trailingQW = { 0, MSCAL(0x14), 0, 0 }  // VU1 instruction addr 20

    // Write DMA cnt tag with total quadword count
    totalQWs = (trailingQW + 0x30 - dmaDataStart) >> 4
    writeDMATag(CNT, totalQWs)
    advanceDMAPtr()

    FlushDMABufferIfFull()
    billboardCount = 0
    return 0
```

**VU1 entry points confirmed:**
- RasterMicro (general geometry): address = `RInitOffset` (kicked by UploadMatrices)
- BillboardMicro (particles/billboards): address = `0x14` (=20, kicked by EndBillboards)

---

## VIRaster::UploadMatrices (0x01111f50, 804 bytes)

Packs the complete VU1 parameter block into a 23-QW DMA packet. This is the bridge between scratchpad (EE) and VU1 data memory.

```
UploadMatrices(raster, dmaTagPtr):
    // DMA cnt, 23 QWs
    // VIF: STCYCL + UNPACK V4-32 × 21 vectors → VU1 addr 0

    // === Matrices (12 QWs) ===
    VU1[0..3]  = scratchpad[0x140]    // screen transform (MVP × Viewport)
    VU1[4..7]  = scratchpad[0x080]    // MVP
    VU1[8..11] = scratchpad[0x0C0]    // viewport

    // === Per-frame parameters (9 QWs) ===
    VU1[12] = { sp[0x180].x, -sp[0x188], sp[0x184], 0 }       // camera params
    VU1[13] = { sp[0x190..0x198],                                // range params
                specularEnabled ? 1.0/lightRadius : 1.0 }        // inv radius
    VU1[14] = { raster.fogNear, sp[0x22C], 0, sp[0x228] }      // fog + flags

    // === Lighting (3 QWs, conditional) ===
    VU1[15] = ambientEnabled  ? sp[0x1AC..0x1B8] : zeros       // ambient RGBA
    VU1[16] = specularEnabled ? sp[0x1D0..0x1D8] : zeros       // specular params
    VU1[17] = dirLightEnabled ? sp[0x1E0..0x1EC] : zeros       // directional dir+color

    // === Transform parameters (3 QWs) ===
    VU1[18] = sp[0x210..0x21C]        // pre-translation scale
    VU1[19] = sp[0x1F0..0x1FC]        // light attenuation params
    VU1[20] = sp[0x200..0x208]        // light color/intensity

    // === Trailing VIF command (QW 22) ===
    { 0, 0, 0, MSCAL(RInitOffset) }  // kick VU1 RasterMicro

    // Clear dirty flags
    raster.pendingUploads = 0
    sp[0x224] = { 0, 0, 0, 0 }       // light dirty flags
```

**VU1 Data Memory Map** (populated by UploadMatrices):

| VU1 Addr | QWs | Contents | Scratchpad Source |
|----------|-----|----------|-------------------|
| 0-3 | 4 | Screen transform (clip → GS pixel coords) | 0x70000140 |
| 4-7 | 4 | ModelViewProjection | 0x70000080 |
| 8-11 | 4 | Viewport transform | 0x700000C0 |
| 12 | 1 | Camera direction params | 0x70000180 |
| 13 | 1 | Range + specular inverse radius | 0x70000190 |
| 14 | 1 | Fog near distance + light flags | raster+0x45C8 |
| 15 | 1 | Ambient light RGBA | 0x700001AC |
| 16 | 1 | Specular/point light params | 0x700001D0 |
| 17 | 1 | Directional light dir + color | 0x700001E0 |
| 18 | 1 | Pre-translation scale | 0x70000210 |
| 19 | 1 | Light attenuation params | 0x700001F0 |
| 20 | 1 | Light color/intensity | 0x70000200 |

For the native port, VU1 addrs 0-20 → a single uniform buffer binding.

---

## VIRaster::DrawPrimBufferTessPackVUNCG (0x011107e8, 2520 bytes)

**The tessellated geometry submission path for dynamic point lights.** Only runs when specular/point lighting is enabled. Tests triangle-light intersections and uploads lit geometry to VU1.

```
DrawPrimBufferTessPackVUNCG(raster, primBufIndex, stripFlag, materialMask):
    primBuf = raster.materialArray[primBufIndex]
    if !specularEnabled || !raster.lightState: return 0

    // Transform light into object space via inverse model-view
    lightPosLocal = inverseModelView(sp[0x100]) × lightPosition(sp[0x1C0])
    lightRadius = sp[0x1CC]

    // Build axis-aligned bounding box around light volume
    lightBBox.min = lightPosLocal - lightRadius
    lightBBox.max = lightPosLocal + lightRadius

    // Early out: light volume doesn't touch this geometry
    if !lightBBox.Intersects(primBuf.bbox): return 0

    for each materialGroup in primBuf:
        material = lookupMaterial(group)
        if !(material.flags & materialMask): skip

        AddMaterial(raster, material, dmaPtr)

        for each triangleStrip in group:
            if !lightBBox.Intersects(strip.bbox): skip

            // Decode vertices: stored as shorts, scaled + offset
            //   pos = (short)rawPos × preTrans.scale + groupOrigin
            v0 = decodeVertex(strip, 0)
            v1 = decodeVertex(strip, 1)

            for triIdx = 2..strip.vertCount:
                v2 = decodeVertex(strip, triIdx)
                triBBox = BBox.Init(v0, v1, v2)

                if triBBox.Intersects(lightBBox):
                    // Triangle strip winding alternation
                    if triIdx & 1:
                        TessTriangle(v0, v2, v1, ...)
                    else:
                        TessTriangle(v1, v2, v0, ...)

                    // Upload tessellated vertices per bone group
                    for each boneGroup:
                        // VIF UNPACK V4-32, 4 QWs per vertex:
                        //   QW0: (pos.x,  pos.y,  pos.z,  1.0)
                        //   QW1: (norm.x, norm.y, 1.0,    0)
                        //   QW2: (u,      v,      extra,  0)
                        //   QW3: (color.r, color.g, color.b, color.a)

                        MSCAL(kickAddress)     // execute VU1
                        FlushDMABufferIfFull()

                // Rotate strip: v0←v1, v1←v2
                v0 = v1; v1 = v2
```

**Source vertex layout** (VUNCG format, 48 bytes per vertex):

| Offset | Size | Field |
|--------|------|-------|
| 0x00 | 12 | position (x, y, z) float |
| 0x0C | 8 | UV (u, v) float |
| 0x14 | 4 | extra/weight |
| 0x18 | 16 | color (r, g, b, a) float |
| 0x28 | 8 | normal (x, y) float |

**Performance note**: This is the hot path for the cave bottleneck. Every triangle that intersects a point light volume gets tessellated and re-uploaded. With 10 torches, most cave geometry gets processed 10 times through this function.

---

## VIColorBuffer::CalcDataSize (0x010c0470, 308 bytes)

Computes the DMA buffer size needed for per-vertex color overlay. This quantifies the per-light DMA cost.

```
CalcDataSize(colorBuf, primBuf):
    if primBuf.type != 2: return -1       // indexed strips only

    numGroups = primBuf.numGroups         // +0x40
    numStrips = primBuf.numStrips         // +0x48
    stripArray = primBuf.stripArray       // +0x5C, stride 28 bytes

    // Section 1: Group headers (8 bytes each, 16-aligned)
    headerSize = align16(numGroups × 8)
    colorBuf.headerOffset = headerSize    // +0x28

    // Section 2: Vertex color entries (16 bytes each)
    totalVertColors = numStrips × 2 + numGroups
    colorBuf.totalVertColors = totalVertColors    // +0x18
    totalSize = headerSize + totalVertColors × 16
    totalSize = align16(totalSize)

    // Section 3: Per-strip color data
    stripDataQWs = 0
    for i in 0..numStrips:
        vertCount = stripArray[i].vertexCount     // stride 28 bytes
        stripDataQWs += ceil((vertCount + 4) / 4)

    colorBuf.stripDataQWs = stripDataQWs          // +0x20
    colorBuf.stripDataOffset = totalSize           // +0x2C
    totalSize = align16(totalSize + stripDataQWs × 16)
    colorBuf.totalSize = totalSize                 // +0x30
```

**VIColorBuffer struct layout (partial):**

| Offset | Field |
|--------|-------|
| +0x18 | totalVertColors |
| +0x20 | stripDataQWs |
| +0x24 | (reset) |
| +0x28 | headerOffset |
| +0x2C | stripDataOffset |
| +0x30 | totalSize (DMA buffer bytes) |

**VIPrimBuffer strip entry** (28 bytes = 7 dwords):

| Offset | Field |
|--------|-------|
| +0x00 | vertexCount per strip |
| +0x04-0x18 | other strip metadata |

**Cave bottleneck cost formula:**
```
DMA_per_light = align16(numGroups × 8)
              + align16((numStrips × 2 + numGroups) × 16)
              + align16(Σ ceil((vertCount_i + 4) / 4) × 16)

Total_DMA_per_frame = DMA_per_light × numActiveLights
```

---

## VIPointLight::ClampScale (0x010c3790, 444 bytes)

Clamps point light billboard scale to prevent excessive overdraw.

```
ClampScale(light, matrix):
    MAX_SCALE = 4.0

    // Extract scale magnitude from each column of the 3×3 rotation sub-matrix
    scaleX = length(matrix.col0)    // sqrt(m00² + m01² + m02²)
    scaleY = length(matrix.col1)    // sqrt(m10² + m11² + m12²)
    scaleZ = length(matrix.col2)    // sqrt(m20² + m21² + m22²)

    // Clamp each axis to max scale of 4.0
    if scaleX > 4.0:  matrix.col0 *= 4.0 / scaleX
    if scaleY > 4.0:  matrix.col1 *= 4.0 / scaleY
    if scaleZ > 4.0:  matrix.col2 *= 4.0 / scaleZ
```

Called from `VIPointLight::Raster` before billboard rendering. Prevents light billboard quads from exceeding 4× reference size.

---

## VIScene::RenderShadow (0x0113bed8, 2300 bytes)

Renders a **planar projected shadow** for a single actor. Not a shadow map — the shadow texture is projected as a decal onto ground geometry.

```
RenderShadow(scene, actorIndex):
    if scene.shadowMaterialIndex == -1: return -1

    sprite = GetActorSpritePtr(scene, actorIndex)
    if !sprite: return -1

    // Get actor transform + inverse
    GetActorTransform(scene, actorIndex, worldMatrix)
    invWorldMatrix = Invert(worldMatrix)

    // 6 bone slots define shadow footprint (feet, torso, hands)
    slotIDs = static_table[6]    // from DAT_011db500
    for i in 0..5:
        CalcSlotWorldTransform(sprite, slotIDs[i], ...)
        localPos = invWorldMatrix × slotWorldPos
        if i > 3: localPos *= 0.5    // extremity bones at 50% influence
        bonePositions[i] = localPos

    // Build shadow bbox from bone positions
    shadowBBox = BBox(6, bonePositions)
    shadowBBox.min.xz -= 0.2         // pad XZ, no Y padding
    shadowBBox.max.xz += 0.2

    // World-space query volume
    worldBBox = shadowBBox.Transform(worldMatrix)
    actorY = GetActorLocation(scene, actorIndex).y
    worldBBox.min.y = actorY - 1.0   // 1 unit below
    worldBBox.max.y = actorY + 0.5   // 0.5 above

    // Find ground triangles under shadow
    VIQueryTriList.Reset(maxDist=80.0, worldBBox, dir=(0,1,0))
    QueryIntersection(scene, worldBBox, actorFilter, triList)

    SetMaterial(raster, scene.shadowMaterialIndex)
    SetZBias(raster, 15)              // avoid z-fighting with ground

    for each tri in triList:          // stride 40 bytes per triangle
        // Lift vertices 0.04 above ground
        v0.y += 0.04; v1.y += 0.04; v2.y += 0.04

        // Per-vertex opacity: fades with height distance from actor
        alpha_i = (1.0 - clamp(actorY - v_i.y, 0, 1)) × 0.65

        // Project UVs: world → actor local XZ, normalized to bbox
        u = (invMat × v.xz - bboxMin.xz) / (bboxMax.xz - bboxMin.xz)

        BeginTriFan(raster)
        Color({1,1,1, alpha0}); UV({u0,v0}); Vertex(v0)
        Color({1,1,1, alpha1}); UV({u1,v1}); Vertex(v1)
        Color({1,1,1, alpha2}); UV({u2,v2}); Vertex(v2)
        EndTriFan(raster)

    SetZBias(raster, 0)
```

**Shadow technique**: Planar projection decal. No shadow maps, no stencil — the shadow texture is UV-mapped onto ground triangles using the actor's inverse transform. Max opacity 65%, fading to transparent 1+ units below. Z-bias 15 prevents z-fighting. 6 bone slots define the shadow footprint shape.

**For native port**: Replace with shadow maps. The bone-based bbox is still useful as a shadow camera frustum hint.

---

## VIRaster::InitGSRegisters (0x011147b8, 236 bytes)

One-time GS hardware initialization. Sets depth test, color clamp, and dither matrix via GIF path.

```
InitGSRegisters(raster, dmaTagPtr):
    // DMA cnt, 5 QWs
    // VIF: FLUSHE + DIRECT 4 (send 4 QWs to GIF)
    // GIF tag: PACKED mode, 3 A+D register writes, EOP

    GS_COLCLAMP (0x46) = 1                       // enable color clamping [0,255]
    GS_TEST_1   (0x47) = 0x30000                  // ZTST = GEQUAL (3)
    GS_DIMX     (0x44) = 0x6071243571603524       // ordered 4×4 dither matrix

    raster.gsInitialized = 1                      // +0x459C
```

**GS → Vulkan mapping:**

| GS Register | Value | Vulkan Equivalent |
|-------------|-------|-------------------|
| COLCLAMP (0x46) | 1 | Default (always clamped in modern GPUs) |
| TEST_1 (0x47) | ZTST=GEQUAL | `VK_COMPARE_OP_GREATER_OR_EQUAL` |
| DIMX (0x44) | ordered dither | Skip (32-bit color depth makes dithering unnecessary) |

---

## VIRaster::SetFogRegisters (0x0110fbc8, 504 bytes)

Writes the GS fog color register.

```
SetFogRegisters(raster):
    // Convert float fog color → byte RGB
    fogR = byte(raster.fogColorR × 255 + 0.5)    // +0x4498
    fogG = byte(raster.fogColorG × 255 + 0.5)    // +0x449C
    fogB = byte(raster.fogColorB × 255 + 0.5)    // +0x44A0

    // DMA cnt, 3 QWs. VIF: FLUSHE + DIRECT 2
    // GIF: PACKED, 1 A+D write, EOP
    GS_FOGCOL (0x3D) = pack_rgb(fogR, fogG, fogB)
```

**VIRaster fog color** stored at offsets +0x4498/+0x449C/+0x44A0 as float RGB [0,1].

For native port: fragment shader `fragColor = mix(fragColor, fogColor, fogFactor)`.

---

## VIParticleDefinitionEx::BlendMotifs (0x010b3410, 2648 bytes)

Blends multiple particle motifs into a single set of attributes using weighted interpolation. This is how the engine smoothly transitions between particle styles (fire→smoke, snow→rain).

```
BlendMotifs(baseDef, output):
    // Phase 1: Full copy base → output (724 bytes / 181 floats)
    output = copy(baseDef)

    // Phase 2: Iterate motif pool and blend
    motifPool = baseDef.motifPool     // at +0xB5 (float offset)
    for each motif in motifPool:
        weight = motif.blendWeight    // offset 0xB2, range [0,1]
        if weight == 0: skip

        // Weighted additive blend:
        //   result += (motif - base) × weight
        // At weight=1.0, motif fully overrides. At 0.5, halfway.

        // Blend core params (14 floats at offset 0x00)
        for i in 0..13: output[i] += (motif[i] - base[i]) × weight

        // Blend keyframe data (128 floats at offset 0x0E)
        // 32 keyframes × 4 channels (RGBA or size/rotation curves)
        for i in 0..127: output[0x0E+i] += (motif[...] - base[...]) × weight

        // Blend extended params (29 floats at offset 0x8E)
        // Blend misc param at offset 0xB4

    // Phase 3: Post-blend validation
    // Set boolean "has gradient" flags for 5 color gradient triplets
    // Stored as float: 0.0 = false, 1e-45 (0x00000001 bits) = true
    for triplets at 0x99..0xAA:
        if any channel != 0: set flag = 1e-45
        else: flag = 0.0
```

**VIParticleAttributes struct** (~724 bytes, 181 floats):

| Offset | Count | Contents |
|--------|-------|----------|
| 0x00-0x0D | 14 | Core: birthrate, lifespan, velocity, gravity, friction, nozzle |
| 0x0E-0x8D | 128 | 32 lifetime keyframes × 4 channels (color/size/rotation curves) |
| 0x8E-0x95 | 8 | Extended params (spread, turbulence?) |
| 0x96-0x98 | 3 | Additional params |
| 0x99-0xAA | 18 | Color gradient channels (6 RGB triplets: birth→death colors) |
| 0xAB-0xAF | 5 | Gradient enable flags (boolean as float) |
| 0xB0-0xB2 | 3 | Blend params (0xB2 = blend weight) |
| 0xB3-0xB4 | 2 | Final params |

**Blend formula**: `result = base + Σ (motif_i - base) × weight_i`

---

## VIRaster::StretchBlit (0x0110bf08, 2680 bytes)

Screen-space textured quad blit with UV rotation. Used for all 2D overlays (UI, health bars, inventory, loading screens).

```
StretchBlit(alpha, raster, texIndex, flags, screenPos, screenSize,
            srcUV, srcUVSize, blendMode):
    texture = raster.textureArray[texIndex]
    invTexW = 1.0 / texture.width      // +0x0C
    invTexH = 1.0 / texture.height     // +0x08

    if currentProgram != RasterMicro: UploadRasterMicro()

    // Material: dither on unless flags & 4
    SetDither(material, !(flags & 4))
    AddMaterial(raster, material, dmaPtr)
    BlitBegin(raster, dmaPtr)

    // Build screen quad (4 vertices, 64 bytes each)
    // Screen transform: sx = ((px - offset) + 0.5) × scale
    //                   sy = ((py - offset) + 0.5) × -scale  (Y flipped)
    v0 = screenPos                     // top-left
    v1 = (x+w, y)                      // top-right
    v2 = (x+w, y+h)                    // bottom-right
    v3 = (x, y+h)                      // bottom-left

    // Per-vertex: color = (1.0, 1.0, 1.0, alpha)
    //             normal = (0, 0, 0, 0)

    // UV rotation (flags & 3):
    //   0 = normal    1 = H-flip    2 = V-flip    3 = 180° rotate
    // UVs normalized: u = texel × invTexW, v = texel × invTexH

    BlitEnd(raster, dmaPtr)
    FlushDMABufferIfFull()
```

**Blit vertex layout** (64 bytes per vertex):

| Offset | Size | Contents |
|--------|------|----------|
| +0x00 | 16 | position (screenX, screenY, 0, 1.0) |
| +0x10 | 16 | UV (u, v, 1.0, 0) |
| +0x20 | 16 | normal (0, 0, 0, 0) |
| +0x30 | 16 | color (1.0, 1.0, 1.0, alpha) |

---

## PS2 Scratchpad Memory Map (0x70000000-0x70003FFF)

Complete VU1 parameter block. For the native port, this becomes uniform buffer bindings.

| Address | Size | Contents | Writer |
|---------|------|----------|--------|
| 0x70000000 | 64 | ModelView matrix | SetModelView |
| 0x70000040 | 64 | Projection matrix | SetProjection |
| 0x70000080 | 64 | MVP (ModelView × Projection) | CalcMatrices |
| 0x700000C0 | 64 | Viewport transform | (external) |
| 0x70000100 | 64 | Inverse ModelView | CalcMatrices |
| 0x70000140 | 64 | MVP × Viewport (screen transform) | CalcMatrices |
| 0x70000180 | 16 | Camera direction params | CalcMatrices |
| 0x70000188 | 4 | Camera Z param (negated for VU1) | CalcMatrices |
| 0x70000190 | 12 | Range/distance params | CalcMatrices |
| 0x700001A0 | 16 | Direction source vector | (external) |
| 0x700001AC | 16 | Ambient light RGBA | (external) |
| 0x700001C0 | 16 | Light position/direction | (external) |
| 0x700001CC | 4 | Light radius (specular) | (external) |
| 0x700001D0 | 12 | Specular light params | (external) |
| 0x700001E0 | 16 | Directional light dir + color | (external) |
| 0x700001F0 | 16 | Light attenuation params | (external) |
| 0x70000200 | 16 | Light color/intensity | SetStaticLighting |
| 0x70000210 | 16 | Pre-translation scale | (external) |
| 0x70000220 | 1 | Directional light enable flag | EnableAllLights |
| 0x70000221 | 1 | Ambient light enable flag | EnableAllLights |
| 0x70000222 | 1 | Specular/point light enable flag | EnableAllLights |
| 0x70000224 | 4 | Light dirty flags (cleared by UploadMatrices) | various |
| 0x70000228 | 4 | Unknown light param | (external) |
| 0x7000022C | 4 | Unknown light param | (external) |

---

## Cross-Reference: Demon Stone Types

These decompiled structures can be mapped to Demon Stone DWARF1 types:

| Decompiled | Demon Stone Equivalent | Notes |
|------------|----------------------|-------|
| Room (0x78 bytes) | ClRoom / part of ClWorld | Portal + geometry refs |
| Portal (0x20 bytes) | ClPortal | Plane + vertex + target |
| Actor (partial) | ClActor (160 bytes, 6 members) | Base class, game entities extend |
| VISceneRendVars | ClSceneRendVars | Render context |
| Cell (0x250 bytes) | Part of ClWorld | BSP cell with rooms |
