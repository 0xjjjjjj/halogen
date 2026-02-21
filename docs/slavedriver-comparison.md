# Slavedriver → Snowblind Engine Lineage

Comparison of Slavedriver Engine (Saturn, 1997, GPLv3) with Snowblind Engine (PS2, 2001-2006).
Source: https://github.com/Lobotomy-Software/SlaveDriver-Engine

Both engines created by Ezra Dreisbach.

## Architecture Mapping

| Subsystem | Slavedriver (Saturn) | Snowblind (PS2) | Evolution |
|-----------|---------------------|-----------------|-----------|
| **Renderer** | `WALLS.C` (2,687 lines) — sector-based BSP with VDP2 sprites | `VIRaster` (168 methods, 53.7 KB) — GS-native rasterizer | Sector renderer → full 3D polygon renderer with RTT |
| **Sprites** | `SPRITE.C` — flat `Sprite` struct, free list allocator | `VIHSprite` hierarchy (76+ methods) — deep OOP tree | C struct → C++ class hierarchy |
| **Scene** | Sectors/walls/faces in `SLEVEL.H` structs | `VIScene` (140 methods) — scene graph | Flat sector array → scene graph with spatial trees |
| **Zones/World** | `level_sector[]` array, `level_wall[]` | `VIZone` (63), `VIWorld` (39) — streaming zones | Static level → zone streaming architecture |
| **Objects/Entities** | `Object` + `messHandler` function pointer (C OOP) | `Base` → `Creature` → `Player` (C++ virtual dispatch) | C message passing → C++ inheritance |
| **AI** | `AI.C` (6,335 lines!) — monster-specific `*_func()` handlers | Per-class `msg_run()` methods (Player::msg_run = 27.5 KB) | Monolithic AI → per-class message handlers |
| **File I/O** | `FILE.C` (375 lines) — raw Saturn CD reads | `VIFile` (37 methods) — abstracted I/O | Direct hardware → abstract file layer |
| **DMA** | `DMA.C` (110 lines) — Saturn DMA queue | `DMA/GIF Pipeline` (107 functions) — PS2 DMA tags/GIF/VIF | Simple DMA → full GS command pipeline |
| **Audio** | `SOUND.C` (468 lines) — Saturn sound driver | `VISoundDevice` (59 methods), `VIWave`, `VISoundSprite` | Hardware driver → spatial audio sprites |
| **Map/Minimap** | `MAP.C` (263 lines) — 2D automap | `map` class (11 methods) — minimap system | Minimal change — automap concept preserved |
| **Hitscan** | `HITSCAN.C` (373 lines) — ray-sector intersection | `VICollide` (42 methods), `VICollRay`, `VICollSphere` | Ray cast → full collision system |
| **Route/Pathfinding** | `ROUTE.C` (118 lines) — sector adjacency routing | `routePlot` (19.8 KB!) — A* pathfinding | Simple adjacency → full A* |
| **Water** | `WaveVert`/`WaveFace` structs, `initWater()`/`stepWater()` | VU1 water vertex deformation microcode | CPU vertex simulation → VU1 microcode |
| **Sequence/Animation** | `SEQUENCE.C` — frame-based sprite animation | `VIHSpriteAnim`, `VIHSpriteFrame` | Tile-based → skeletal/hierarchical |
| **Menu** | `MENU.C` (1,499 lines) | `VIUI` (42), `VIWnd*`, `VIGUIObject` (47) | Hardcoded menus → widget framework |
| **Memory** | Static arrays (`sprites[450]`, `level_wall[]`) | `VIPool` (145), `VIArray` (101), custom STL containers | Static allocation → pool allocators |

## Key Patterns Preserved

### 1. Message-Passing Entity System

**Slavedriver:**
```c
typedef void (*messHandler)(struct __object *this, int message, int param1, int param2);
// Signals: SIGNAL_MOVE, SIGNAL_ENTER, SIGNAL_HURT, SIGNAL_OBJECTDESTROYED
void signalObject(Object *object, int message, int param1, int param2);
```

**Snowblind (from symbols):**
```
Player::msg_run (27.5 KB)
Creature::msg_run, msg_draw, msg_collision
Innoruuk::msg_run (11.7 KB)
AutoObject::msg_run, msg_draw, msg_save, msg_load
```

The `messHandler` function pointer became virtual `msg_*` methods. Same pattern, C → C++.

### 2. Object Class Hierarchy

**Slavedriver:**
```
Object (base, has type + class + messHandler)
├── SpriteObject (has Sprite*, sequenceMap)
│   ├── ProjectileObject (+owner, age)
│   └── MonsterObject (+health, aiSlot, enemy, route)
│       ├── SpiderObject (= MonsterObject)
│       ├── PlayerObject (= MonsterObject)
│       └── AnubisObject (+stunCounter)
├── WallObject (+wallNm)
├── SectorObject (+sectorNm)
└── PushBlockObject (+pbNum)
```

**Snowblind:**
```
Base (40 methods)
├── Creature (77 methods)
│   ├── Player (45 methods) — LARGEST
│   ├── Orc, Goblin, Skeleton, Mummy...
│   └── NPC
└── item (38 methods)
```

Identical pattern — base object with sprite, specialized for monsters/players/items.

### 3. Sector-Based World

**Slavedriver:** `sSectorType` with walls, floors, lighting, objects.
**Snowblind:** `VIZone` with rooms, trees, streaming. Same concept, scaled for 3D streaming.

### 4. Dynamic Lighting via Sprites

**Slavedriver:**
```c
void addLight(Sprite *s, int r, int g, int b);
void removeLight(Sprite *s);
void changeLightColor(Sprite *s, int r, int g, int b);
```

**Snowblind:** `VIPointLight`, `VIStaticLighting`, `VIColorBuffer` — sprite-attached point lights.

This explains the cave performance issue: the Snowblind Engine inherited the pattern of attaching lights to sprites (torches, fire effects), but on PS2 each dynamic light requires additional render passes.

### 5. Water Vertex Simulation

**Slavedriver:** `WaveVert` struct with `pos`, `vel`, `connect[4]` — spring-connected vertex mesh for water physics.
**Snowblind:** VU1 microcode for water vertex deformation.

The spring-mesh water simulation from Saturn was ported to VU1 vector microcode on PS2.

## What's New in Snowblind (Not in Slavedriver)

| Feature | Snowblind | Notes |
|---------|-----------|-------|
| VU1 geometry | VU1 microcode | Saturn had no vector processor |
| AMX/Pawn scripting | 142 functions | Saturn had no scripting VM |
| Particle system | 194 functions | Saturn was too weak for particle effects |
| SOE networking | 889 functions | Saturn had no online |
| Spell/effect system | VISpellEventDriver (34 methods) | New for RPG genre |
| ESF asset format | VIESFParse (117 methods) | New structured format |
| Scene graph | VIScene, VISceneFilter | Saturn used flat sector lists |
| Widget UI | VIUI, VIWnd*, VIGUIObject | Saturn had hardcoded menus |
| Custom STL | VIPool, VIArray, VIMap, VIList | Saturn used static arrays |
| Render-to-texture | VIRaster + GS registers | Saturn VDP2 had no RTT |
| SSAA (1280x448) | GS double-width back buffer | Saturn was 320x224 |

## Insights for RE

1. **Entity naming**: Slavedriver uses `*Object` suffix (SpiderObject, PlayerObject). Snowblind dropped it but preserved the pattern. When we see unnamed classes with `msg_run`/`msg_draw`, they follow this pattern.

2. **Constructor pattern**: Slavedriver has explicit `construct*()` functions. Snowblind has `createByName` (15.6 KB) — evolved into a factory pattern, same concept.

3. **Route → routePlot**: The 118-line sector adjacency router became 19.8 KB A* pathfinder. The function name `routePlot` persists from Slavedriver's `ROUTE.C`.

4. **Light attachment to sprites**: Understanding this Slavedriver pattern explains why Snowblind's cave performance suffers — each torch/fire sprite carries a dynamic point light, requiring additional render passes.

5. **Water vertex mesh**: The `WaveVert` struct with spring connections is the CPU-side data structure that feeds VU1. Understanding the Saturn implementation helps reverse the VU1 microcode.

6. **Level format**: Slavedriver's `sLevelHeader` with sectors/walls/vertices/faces/textures/objects is the precursor to Snowblind's ESF format. Similar structure, more complex.
