# Snowblind Engine Architecture Map

Generated from ELF symbol table analysis of Champions of Norrath (SLUS-20565).

**14,370 functions | 646 classes | ~3.9 MB code**

## Engine Overview

The Snowblind Engine uses a `VI*` prefix convention for all engine classes (likely "Visual Interactive" or the studio's internal name). Game-specific code uses unprefixed classes. The engine is a classic PS2-era architecture: scene graph, sprite hierarchy, zone/world streaming, GS-native rendering pipeline, and a Pawn/AMX scripting VM for gameplay logic.

## Subsystem Map

### Core Engine (by code size)

| Subsystem | Functions | Size (KB) | Key Classes |
|-----------|-----------|-----------|-------------|
| Renderer | 431 | 202.5 | VIRaster (168 methods, 53.7 KB), VIRasterTess, VIPrimBuffer, VIClipStack |
| Scene | 140 | 44.1 | VIScene (140 methods, 44.1 KB), VISceneQuery, VISceneFilter |
| Particles | 194 | 44.2 | VIParticleEmitter, VIParticleSprite, VIParticleSystem, VIParticleDefinitionEx |
| Camera | 77 | 42.7 | Camera (41 methods), VICamera (8), VICameraEffect (11), VIFlyCamera, VIWalkCamera |
| Audio | 146 | 40.1 | VISoundDevice (59 methods), VIWave, VISoundSprite, VIStreamAudioSprite, VIBattleMusic |
| Lighting | 135 | 32.5 | VIPointLight, VIColorBuffer, VIStaticLighting, VITimeOfDay |
| UI | 97 | 28.8 | VIUI (42 methods), VIWnd*, VIWidget, VIGUIObject (47), VIGUIPage, VIGUIDialog |
| AMX Scripting | 142 | 25.2 | amx_Exec, amx_Register, amx_Push, etc. (Pawn VM) |
| Sprites | 76 | 19.1 | VIHSprite (76 methods), VICSprite (51), VISimpleSprite, VISkinSprite, VILODSprite |
| Collision | 42 | 19.0 | VICollide (42 methods), VICollBuffer, VICollRay, VICollSphere |
| DMA/GIF Pipeline | 107 | 18.9 | Low-level PS2 hardware: DMA tags, GIF tags, VIF commands |
| Zone/World | 102 | 34.2 | VIZone (63 methods), VIWorld (39), VIZoneRoom, VIZoneTree, VIWorldTree |
| Asset Loading | 85 | 14.3 | VIObjFile (62 methods), VILoader (23), VIWadFile, VIFlatFile |
| File I/O | 37 | 7.3 | VIFile (37 methods) |
| Math | 413 | 236.8 | VIMatrix44D, VIMatrix44, VIMatrix33, VIQuatD, VIQuat, VIVect3D, VIVect4D |
| Setup/Config | 16 | 6.3 | VISetup (16 methods) |
| Font | 27 | 6.6 | VIRFont (27 methods), VIFont (13) |
| String Utils | 46 | 4.8 | VIString (46 methods), VIStringTable |

### Game-Specific Code

| Subsystem | Functions | Size (KB) | Key Classes |
|-----------|-----------|-----------|-------------|
| Game Entities | 246 | 199.2 | Player (45/66.5KB), Creature (77/42.6KB), item (38/32.5KB), Orc, Goblin, Skeleton, NPC, Mummy, Soul |
| Networking | 889 | 192.0 | RealmService::RealmGatewayAPI (111 methods), VIRealmInterface, VIStation, VIUDPSocket, VITCPSocket2 |
| Physics | 143 | 62.5 | Vehicle (66 methods/30KB), collision/steering functions |
| ESF Parser | 117 | 55.6 | VIESFParse (117 methods) — likely level/asset format parser |
| Spell System | ~85 | ~50.0 | VISpellEventDriver (34/22.4KB), VISpellEffectSystem (24), VISpellEffect, VIBolt, VIBoltHarmonic, VITrailFx |
| Atmosphere | 28 | 21.1 | VIAtmosphere — weather/environmental effects |
| Flora | ~17 | ~7.2 | VIRadialFloraSystem, VIFloraSprite, VIZoneRadialFlora |

### External/Runtime

| Subsystem | Functions | Size (KB) | Notes |
|-----------|-----------|-----------|-------|
| C++ Runtime | 1,091 | 280.3 | Compiler runtime, exception handling |
| Sony SDK | 484 | 96.0 | sce* functions — GS, DMA, pad, network |
| C++ Stdlib | 223 | 15.0 | iostream, string |
| Other | 7,138 | 2,205.4 | Unclassified — free functions, templates, XML (libxml2) |

## Class Hierarchy

### Sprite Inheritance Tree

The engine uses a deep sprite hierarchy for all renderable objects:

```
VISprite (base, 15 methods)
├── VISimpleSprite (12)
├── VIHSprite (76) — main hierarchical sprite
│   ├── VICSprite (51) — "complex" sprite
│   │   └── VICSpriteCust (8)
│   ├── VINameSprite (14)
│   ├── VIPointSprite (12)
│   ├── VILODSprite (14)
│   ├── VISkinSprite (11)
│   ├── VIFloraSprite (11)
│   ├── VIGroupSprite (14)
│   ├── VISoundSprite (11)
│   ├── VIStreamAudioSprite (12)
│   ├── VIEffectVolumeSprite (11)
│   └── VIParticleSprite (12)
└── VIIconDefinition (6)
```

### Game Entity Hierarchy

```
Base (40 methods, 9.5 KB)
├── Creature (77 methods, 42.6 KB)
│   ├── Player (45 methods, 66.5 KB) ← LARGEST game class
│   ├── NPC (14 methods, 7.0 KB)
│   ├── Orc (22 methods, 16.7 KB)
│   ├── Goblin (18 methods, 14.3 KB)
│   ├── Skeleton (17 methods, 13.3 KB)
│   ├── Mummy (14 methods, 12.4 KB)
│   └── Soul (12 methods, 8.3 KB)
└── item (38 methods, 32.5 KB)
```

### Scene Graph

```
VIScene (140 methods, 44.1 KB) — root scene manager
├── VIWorld (39 methods) — world geometry
│   └── VIWorldTree (4) — spatial partitioning
├── VIZone (63 methods) — streaming zones
│   ├── VIZoneRoom (11)
│   ├── VIZoneTree (4) — zone spatial tree
│   └── VIZoneRadialFlora (3)
├── VISceneFilter (8) — render passes
│   ├── VISceneOutdoorsFilter (2)
│   └── VIRadialFloraFilter (2)
└── VISceneDisplayElem (1) — display list entries
```

## Performance-Critical Functions

The top 10 largest functions reveal where the engine spends most CPU time:

| Function | Size | Address | Analysis |
|----------|------|---------|----------|
| `Player::msg_run` | 27.5 KB | 0x197878 | Main player update loop — handles all player state, input, combat |
| `routePlot` | 19.8 KB | 0x2c0a10 | Pathfinding — A* or similar route planning |
| `megatileGenerate` | 19.7 KB | 0x25e3a8 | World generation — terrain/tile creation |
| `createByName` | 15.6 KB | 0x14c410 | Entity factory — creates game objects by name string |
| `setCamera` | 14.9 KB | 0x1884f0 | Camera setup — complex camera positioning |
| `VIWndGenericRenderer::ActionOccured` | 13.0 KB | 0x10ba0c8 | UI event handler |
| `playerSelectionTask` | 12.2 KB | 0x27a658 | Character selection screen |
| `setupDefaultEquipment` | 11.9 KB | 0x19e780 | Equipment initialization |
| `Innoruuk::msg_run` | 11.7 KB | 0x1f9150 | Boss AI — Innoruuk (EverQuest reference!) |
| `fxRunWeapon` | 10.4 KB | 0x1dc2c0 | Weapon effects execution |

### Known Performance Bottlenecks

Based on PCSX2 reports of 10 FPS in caves/underground:

| Suspect | Reason | Classes/Functions |
|---------|--------|-------------------|
| Particle rendering | Fire/torch effects in caves | VIParticleEmitter, VIParticleSprite, drawDistortionParticles |
| Render-to-texture | PCSX2 hacks confirm RTT issues | VIRaster::BeginScene, textureInsideRT hack |
| Zone streaming | Underground zones = more rooms | VIZone, VIZoneRoom, VISceneOutdoorsFilter |
| Lighting | Indoor = many point lights | VIPointLight, VIStaticLighting, VIColorBuffer |
| Atmosphere | Cave fog/atmosphere effects | VIAtmosphere (28 methods, 21.1 KB) |

## Networking Architecture

Surprisingly large networking subsystem (889 functions, 192 KB):

- **RealmService::RealmGatewayAPI** — 111 methods, SOE (Sony Online Entertainment) realm server protocol
- **VIRealmInterface** — 34 methods, game-side realm client
- **VIStation** — 14 methods, Station.com integration (SOE's platform)
- **VIUDPSocket / VITCPSocket2** — custom socket wrappers
- **RC2 encryption** — `RC2_encrypt` (7.7 KB) + `RC2_decrypt` (7.2 KB) — network security

This confirms Champions of Norrath used SOE's online infrastructure for multiplayer.

## Spell/Effect System

The spell system is data-driven via VISpellEvent:

```
VISpellEventDriver (34 methods, 22.4 KB) — drives spell execution
├── VISpellEffectSystem (24 methods) — manages active effects
├── VISpellEffectDriver (14 methods) — per-effect driver
├── VISpellEffect (5 methods) — effect definition
├── VISpellActiveEvent (2 methods) — active spell instance
└── VISpellEventList (4 methods) — event queue

Visual effects:
├── VIBolt (3 methods, 2.5 KB) — lightning bolt rendering
├── VIBoltHarmonic (4 methods) — harmonic bolt variation
├── VITrailFx (9 methods) — weapon/spell trails
└── VIParticleSystem → particle-based spell effects
```

## Asset Format: ESF

`VIESFParse` is the 3rd largest class (117 methods, 55.6 KB). ESF likely stands for "Engine Scene File" or similar. This is the primary asset/level format with its own parser. Key for Phase 2 asset pipeline reverse engineering.

## Key Observations

1. **VIRaster is the heart** — 168 methods, manages all GS interaction. BeginScene/EndScene, DMA submission, scissoring, double-buffering.

2. **The "Other" bucket is huge** — 7,138 functions (49.6%) are unclassified. Many are likely free functions, templates, or game logic not attached to VI* classes. Improving classification will require Ghidra analysis.

3. **Sprite hierarchy = entity system** — Everything renderable inherits from VISprite. This is the entity-component pattern of its era.

4. **AMX/Pawn scripting** — 142 functions for the scripting VM. Game logic is data-driven, which is good news for modding/porting.

5. **SOE online integration** — The networking code (889 functions) is disproportionately large for a couch co-op game. This was Sony Online's infrastructure.

6. **XML parsing embedded** — xmlParseTryOrFinish, xmlXPathCompOpEval — full libxml2 linked. Used for config/data files.

7. **EverQuest DNA** — Boss named "Innoruuk" (EQ deity), "Realm" networking, SOE Station integration. The Snowblind Engine was deeply tied to the EverQuest franchise.

## Subsystem Size Distribution

```
Renderer + DMA/GIF + Lighting + Particles:  298.1 KB (23.2%)  ← GRAPHICS
Scene + Zone/World + Camera:                121.0 KB  (9.4%)  ← WORLD
Game Entities + Physics + Spells:           311.7 KB (24.3%)  ← GAMEPLAY
Networking:                                 192.0 KB (15.0%)  ← NETWORK
Audio:                                       40.1 KB  (3.1%)  ← AUDIO
UI + Font:                                   35.4 KB  (2.8%)  ← UI
AMX Scripting:                               25.2 KB  (2.0%)  ← SCRIPTING
Math + String + I/O + Setup:                255.2 KB (19.9%)  ← FOUNDATION
C++/Sony Runtime:                           391.3 KB           ← RUNTIME (not engine)
```

Graphics subsystem (renderer + particles + lighting + DMA) makes up ~23% of engine code — the primary target for native port optimization.
