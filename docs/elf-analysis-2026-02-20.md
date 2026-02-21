# Champions of Norrath ELF Analysis

**Date:** 2026-02-20
**Binary:** SLUS_205.65 (8.9 MB, NTSC-U v1.02)
**Entry point:** 0x100008

---

## Summary

The retail ELF contains **14,381 named C++ functions** via `.symtab`/`.strtab` sections.
The `.mdebug.eabi64` section exists but is empty (0 bytes) — symbols come from the
standard ELF symbol table instead. This gives us the full function map of the
Snowblind Engine without any manual reverse engineering.

The engine uses a `VI` prefix for all core classes (likely "Visual Imagination" or
similar internal name). Game-specific entities (Orc, Goblin, Mummy, etc.) are plain
class names.

---

## ELF Structure

| Section | Address | Size | Purpose |
|---------|---------|------|---------|
| `.text` | 0x00100000 | 2.2 MB | Main code (EE) |
| `.vutext` | 0x0031B510 | 15.7 KB | VU microcode |
| `.data` | 0x0031F480 | 1.3 MB | Initialized data |
| `.rodata` | 0x00454300 | 173 KB | Read-only data |
| `.vudata` | 0x004542E4 | 0 bytes | VU data (empty - loaded at runtime) |
| `.srs` | 0x01000000 | 3.5 MB | **Secondary code section** (large!) |
| `.loadScreenS...` | 0x01E00000 | 1.1 MB | Loading screen assets |
| `.DVP.overlay*` | — | ~32 KB | 17 VU1 overlay programs |
| `.symtab` | — | 341 KB | **14,381 function symbols** |
| `.strtab` | — | 501 KB | Symbol name strings |

### Two Code Sections

The binary has **two code regions**:
1. `.text` at 0x00100000 (2.2 MB) — Main engine and game code
2. `.srs` at 0x01000000 (3.5 MB) — Unknown purpose, possibly overlay/resource system

The `.srs` section is larger than `.text` and contains functions with the `setLoadImageTagsYX`,
`setDMAscTag`, `setGIFtag`, `dmaIOP`, `dmaRefImage` — **this is the DMA/GIF rendering pipeline**.

### VU1 Programs

17 `.DVP.overlay` sections contain the VU1 geometry processing programs. The `.DVP.ovlytab`
section contains an overlay table (0xD8 bytes, 12-byte entries = 18 entries), and
`.DVP.ovlystrtab` has the overlay names.

---

## Engine Subsystems (by symbol count)

| Subsystem | Functions | Key Symbols |
|-----------|-----------|-------------|
| UI/HUD | 383 | VIWnd, VIWndEdit, VIUI, drawAutoMap, drawGold |
| Network | 312 | sendControlPackets, receivePackets, advanceRealState |
| C++ stdlib | 1,759 | iostream, streambuf, filebuf (statically linked!) |
| Sony SDK (sce*) | 448 | scePad*, sceFsSigSema, _GetGsDxDyOffset |
| DMA/VIF/GIF | 173 | reloadDMA, initVIF, setGIFtag, setDMAscTag, WaitDma |
| Audio | 154 | VIWave (7 methods) |
| AMX Scripting | 148 | amxStartDialog, amxHitPlayers, amxNewWorld |
| Lighting | 111 | setDirLight, findLightsAtPoint, findLightsInBox, initLightInfo |
| Physics/Collision | 74 | wallAndObjectSteering, VICollide (8 methods) |
| Particles | 73 | initParticleSystem, drawDistortionParticles, drawSingleParticle |
| Renderer (draw*) | 46 | drawObjectsTask, drawWorldObject, drawWorldPolyset, drawTexture |

---

## Engine Class Hierarchy (VI prefix)

These are the Snowblind Engine core classes:

### Rendering
| Class | Methods | Purpose |
|-------|---------|---------|
| VIRaster | 33 | Rasterizer — the core renderer |
| VIHSprite | 15 | Hardware sprite rendering |
| VIRFont | 12 | Font rendering |
| VIScene | 14 | Scene graph / management |

### World/Level
| Class | Methods | Purpose |
|-------|---------|---------|
| VIWorld | 10 | World representation |
| VIZone | 16 | Zone/area management (caves, outdoors) |
| VIObjFile | 36 | Object file format loading |
| VILoader | 11 | Asset loading pipeline |

### I/O
| Class | Methods | Purpose |
|-------|---------|---------|
| VIFile | 15 | File system abstraction |
| VIString | 18 | String utilities |

### UI
| Class | Methods | Purpose |
|-------|---------|---------|
| VIUI | 24 | UI system root |
| VIWnd | 12 | Window/widget base class |
| VIWndEdit | 10 | Editable text widget |

### Physics
| Class | Methods | Purpose |
|-------|---------|---------|
| VICollide | 8 | Collision detection |

### Audio
| Class | Methods | Purpose |
|-------|---------|---------|
| VIWave | 7 | Audio playback |
| VISetup | 9 | Audio/config setup |

---

## Game Entity Classes

Plain class names (no VI prefix) — game-specific code:

| Class | Methods | Type |
|-------|---------|------|
| Creature | 17 | Base enemy class |
| Orc | 19 | Enemy |
| Goblin | 11 | Enemy |
| Skeleton | 9 | Enemy |
| Mummy | 9 | Enemy |
| Soul | 9 | Enemy/collectible |
| Player | 8 | Player character |
| NPC | 10 | Non-player character |
| Camera | 21 | Camera system |
| Vehicle | 19 | Vehicle system |
| item | 16 | Item/inventory |

---

## Key Renderer Functions (Performance Target)

These are the functions responsible for the cave/particle performance issues:

```
# Core rendering pipeline
drawObjectsTask__Fv          — Main draw loop (task-based)
drawWorldObject__F[...]      — Individual object rendering
drawWorldPolyset__F[...]     — Polygon set rendering
drawTexture__FR6[...]        — Texture drawing (multiple overloads)

# Particle system (fire = slowdown)
initParticleSystem__Fv       — Particle system init
drawDistortionParticles      — Distortion effects (heat haze?)
drawSingleParticle__F[...]   — Per-particle rendering
drawPS__FR6Packet[...]       — Particle system batch draw
setParticleDef__F[...]       — Particle definition setup

# Lighting (caves = slowdown)
setDirLight__Fsssssfb        — Directional light setup
findLightsAtPoint__F[...]    — Light query at position
findLightsInBox__F[...]      — Light query in volume
initLightInfo__Fv            — Light system init
amxLightEffect__F[...]       — Scripted light effects

# DMA/GIF pipeline (GPU submission)
reloadDMA__Fi                — DMA reload (large: 2488 bytes)
initVIF__Fv                  — VIF initialization
setGIFtag                    — GIF tag construction
setDMAscTag                  — DMA source chain tag
WaitDma                      — DMA synchronization
dmaRefImage                  — DMA reference image transfer
setLoadImageTagsYX           — Texture upload to GS VRAM

# Water (another performance-sensitive area)
drawWaterPatch__F[...]       — Water surface rendering
```

---

## AMX Scripting Engine

The game uses an AMX-based scripting engine (similar to Pawn/Small) for gameplay logic.
148 `amx*` functions handle:

- Dialog/conversation: `amxStartDialog`
- NPC behavior: `amxStartNPCAnim`, `amxSetAnimation`
- World transitions: `amxNewWorld`
- Combat: `amxHitPlayers`, `amxClosestPlayer`
- Effects: `amxAddParticleOn`, `amxLightEffect`, `amxParticleMorph`
- Props: `amxStartPropAnim`, `amxAutoPropSetState`
- Vehicles: `amxEntityRideVehicle`

This means game logic is largely data-driven through scripts, not hardcoded in C++.

---

## Networking

Substantial networking code (312 functions):
- `sendControlPackets` (5,532 bytes — large function)
- `receiveControlPackets` (2,596 bytes)
- `advanceRealState` (5,488 bytes — game state sync)
- `receivePackets` (804 bytes)
- `compareStatePack` — state comparison for sync

The online multiplayer was a significant part of the engine.

---

## Next Steps

1. **Run PS2Recomp** against this ELF to get C++ output
2. **Load into Ghidra** with ghidra-emotionengine-reloaded for decompilation
3. **Focus analysis on**:
   - `VIRaster` class (33 methods — the core renderer)
   - `drawObjectsTask` (the main draw loop)
   - `drawDistortionParticles` + `drawSingleParticle` (particle performance)
   - `findLightsAtPoint` + `findLightsInBox` (lighting performance)
   - `reloadDMA` + `setGIFtag` (GS submission pipeline)
4. **Extract VU1 programs** from `.DVP.overlay` sections
5. **Demangle all C++ symbols** for readable function signatures

---

## Correct Serial / File Info

```
Game:    Champions of Norrath (NTSC-U)
Serial:  SLUS-20565
ELF:     SLUS_205.65 (8.9 MB)
Entry:   0x100008
Boot:    BOOT2 = cdrom0:\SLUS_205.65;1
Version: 1.02
```
