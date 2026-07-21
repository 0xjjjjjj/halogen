# Phase 2 Status — Static Analysis Complete, Types Applied

As of 2026-02-21. All 6,446 functions batch-decompiled via Ghidra headless mode. 34 struct types applied from Demon Stone DWARF1 debug info, 700 function `this` pointers retyped — producing 2,276 named struct member accesses in decompiled output. 42 rendering functions manually analyzed in docs/render-pipeline.md (1,492 lines).

## What We Know

### Engine Architecture (fully mapped)

17 subsystems documented in `docs/subsystem-analysis.md`:

| Subsystem | Files | Status | Key Finding |
|-----------|-------|--------|-------------|
| VIRaster | rendering | complete | 5 vertex formats, material LRU, DMA double buffer |
| VIZone | spatial | complete | BSP traversal, pre-translation, recursive queries |
| VIParticle | effects | complete | Motif blending, billboard rendering |
| ESF/CSF | assets | complete | 117 parse methods, compressed scene format |
| VIPointLight | lighting | complete | Per-vertex VIColorBuffer overlay = cave bottleneck |
| VIScene | orchestrator | complete | 140 methods, actor/streaming/rendering/ToD |
| VIAtmosphere | weather | complete | Raycasting rain, billboard layers, audio transitions |
| VILoader | I/O | complete | Async DMA reads, 16-byte alignment, ESF on complete |
| VICollide | physics | complete | 3 buffer formats, per-sprite dispatch |
| AMX/Pawn | scripting | complete | Standard Pawn VM with JIT (critical for native port) |
| Game entities | gameplay | complete | createByName factory, Player::msg_run, Creature base |
| VISoundDevice | audio | complete | IOP bridge, SPU2 channels, priority eviction |
| VIWorld | terrain | complete | Grid cells, profile blending, dual streaming |
| VIHSprite/VICSprite | characters | complete | 156 methods, bone animation, customization |
| Boot sequence | init | complete | 22 subsystems in dependency order |
| Game loop | frame | complete | Sequential sim+render, threading opportunity |
| VIWnd | UI | complete | 14+ window types, retained-mode widget tree |
| Networking | multiplayer | complete | 344 files, DRDP protocol, peer-to-peer |

### The Cave Performance Bottleneck — Traced

```
Each torch = VIParticleSprite (billboard particles)
           + VIPointLight (VIColorBuffer per-vertex overlay)

VIColorBuffer.Lock → compute per-vertex colors → VIColorBuffer.Unlock
→ re-render geometry with new colors → repeat for next light

10 torches × (20 particles + light pass with geometry re-render) = 400+ draw ops

Fix: Replace VIPointLight/VIColorBuffer with per-pixel lighting (trivial on modern GPU)
```

### Engine vs Game Code Boundary

| Engine (VI*) | Game Layer |
|-------------|------------|
| C++ OOP, VIVect3/VIMatrix44 | C-style free functions, Point3/Matrix34 |
| VIPool/VIArray containers | ListHead linked lists |
| PascalCase methods | camelCase free functions |
| PS2 hardware-coupled | Gameplay logic, portable |

**Strategy**: Replace engine layer (VI*), keep game layer intact.

### Demon Stone Prototype — The Rosetta Stone (2026-02-21)

The Demon Stone Jun 2004 prototype (Stormfront Studios, `SLUS_208.04`, 14.7MB) has 9.3MB of Metrowerks CodeWarrior DWARF1 debug info. This is the same Snowblind Engine with a different studio's naming conventions (`Cl*` prefix = Snowblind's `VI*` prefix).

**What we recovered**:
- 1,211 unique struct/class/union definitions with full member layouts (byte offsets, types, sizes)
- 7,595 total member fields across all structs
- 129 enums with 1,344 named constants
- 618 source file paths revealing complete engine source tree at `C:\Projects\Phoenix\Game\`
- 655 classes with 6,041 member names from C++ name mangling
- Engine internal codename: "Phoenix". Animation system codename: "Noam"

**Key class mapping** (Demon Stone `Cl*` → CoN `VI*`):

| Demon Stone | Champions of Norrath | Size | Members |
|-------------|---------------------|------|---------|
| ClGfx | VIRaster | varies | rendering pipeline |
| ClWorld | VIZone | varies | world/BSP management |
| ClNoamActor | VIHSprite | 2,624 bytes | 64 members + 2 bases |
| ClDynamicLightManager | VIColorBuffer | — | per-vertex lighting |
| ClPfxSystem | VIParticle | varies | particle effects |
| ClScript | AMX/Pawn VM | varies | scripting engine |
| ClAudio | VISoundDevice | — | audio system |
| ClCharacterObj | game entity base | 1,568 bytes | 126 members |
| ClCamera | camera system | 1,984 bytes | 23 members |
| ClShaderPass | shader/material | 40 bytes | 12 members |
| ClActor | actor base | 160 bytes | 6 members |

**Parser tool**: `tools/parse-dwarf1-types.py` — 250-line Python DWARF1 parser. Outputs JSON.
**Output**: `docs/demon-stone-types.json` (deduplicated, 1,211 structs)

### .mdebug Status — Confirmed Empty Across All Builds

Checked 3 Snowblind-built ELFs — `.mdebug.eabi64` is 0 bytes in ALL of them:
- Retail CoN (`SLUS_205.65`) — 0 bytes
- CoN demo disc (`CORE_DEMO.ELF`) — 0 bytes
- CoN Aug 2003 prototype (`SLPS_251.39`) — 0 bytes, no `.symtab` either

This was a toolchain/Makefile decision, not per-build stripping. Snowblind's build pipeline zeroed `.mdebug` unconditionally.

### VU1 Microcode — Found in DVP Overlay Sections

The "VU1 microcode gap" from Phase 1 was based on `.vudata`/`.vubss` being zeroed. The actual VU1 programs live in **DVP overlay sections** (`.DVP.overlay.*`):
- Retail CoN: 16 DVP overlays (2 VU1 programs)
- Demo/prototype: 8 DVP overlays (1 VU1 program)
- The 2 programs match our earlier analysis: RasterMicro (general geometry) and BillboardMicro (billboards)

## What's Left — Ranked by Value

### Tier 1: High value, do next

#### 1. Ghidra Session — COMPLETE
6,446/6,447 functions batch-decompiled via headless mode. 42 rendering functions manually analyzed with full pseudocode, struct layouts, and call graphs in `docs/render-pipeline.md` (1,492 lines). VU1 data memory map, scratchpad map, bottleneck cost formula all documented.

**Output**: `output/decompiled/` (6,447 .c files, 30MB) + `output/decompiled/all_decompiled.txt` (12MB combined)
**Tools**: `tools/ghidra-batch-decompile.py`, `tools/run-batch-decompile.bat`

#### 2. Cl* → VI* Type Mapping — COMPLETE
34 VI* classes mapped to Demon Stone Cl* equivalents. 942 named struct members from DWARF1 debug info. 700 function `this` pointers retyped via decompiler-assisted param discovery. Batch re-decompilation produces **2,276 named struct member accesses** (e.g. `this->mWalkableHeading` instead of `*(float *)(param_1 + 0xe0)`).

Best coverage: VIHSprite 67%, VIZone 65%, VIPointLight 56%, VICollide 54%, VIWnd 100%.

**Output**: `output/type-mapping.json`, `output/snowblind-types.h` (1,023 lines), `output/offset-xref.md` (2,091 lines)
**Tools**: `tools/map-types.py`, `tools/ghidra-apply-types.py`, `tools/ghidra-retype-params.py`

#### 3. PCSX2 Runtime Tracing
**Why**: VU1 microcode and GS register writes are invisible to static analysis. Need to see what actually happens at runtime.

**Concrete steps**:
- Run Champions of Norrath in PCSX2 debug build
- Enable GS dump capture (Tools → GS Dump)
- Capture a cave scene (torches + particles) and an outdoor scene (weather)
- Trace VIF DMA packets to catalogue VU1 program uploads
- Record GS register writes per frame to understand draw call patterns

**Effort**: 1-2 hours per scene capture

### Tier 2: Medium value, do when needed

#### 4. VU1 Microcode Extraction
**Why**: Need to build a VU1 interpreter for the native port. Programs now confirmed in DVP overlay sections.

**Concrete steps**:
- Extract DVP overlay sections from ELF (16 overlays, 2 VU1 programs: RasterMicro, BillboardMicro)
- Write a VU1 disassembler (VU1 instruction set is documented in ps2tek)
- OR: capture VU1 uploads via PCSX2 VIF tracing (more complete — catches runtime-loaded programs)
- Catalogue all unique VU1 programs and their vertex format signatures

**Depends on**: PCSX2 runtime tracing (#3)
**Effort**: Days to weeks (VU1 instruction set is complex)

#### 5. paraLLEl-GS Evaluation — COMPLETE
Built parallel-gs-replayer on the Windows build machine (MSVC, VS2022, RTX 4090 Vulkan 1.4). Fed all 3 GS dumps through it — zero crashes, zero errors, zero unsupported GS features. Handles 102K draw calls/frame (worst-case caves) in <1 GB VRAM. BG:DA freeze bug confirmed as EE/VU emulation issue, not GS — irrelevant to native port.

**Verdict**: GO for Phase 3. paraLLEl-GS is the rendering backend.

**Output**: `docs/parallel-gs-eval.md`, `C:\parallel-gs\` on the build machine

### Tier 3: Low value until implementation

#### 6. AMX/Pawn Script Extraction
**Why**: Need to understand what scripts do and whether JIT recompilation is needed.

**Concrete steps**:
- Find .pawn or script data in ESF files
- Use existing Pawn tools to decompile scripts
- Assess whether scripts can run interpreted (no JIT) at acceptable speed

**Effort**: Hours to find scripts, then standard Pawn tooling

#### 7. ESF File Format Reversing
**Why**: Need to read/write ESF files for modding and to understand asset structure.

**Concrete steps**:
- Use VIESFParse call graph (117 methods already documented) as a roadmap
- Write a Python ESF parser using the method signatures as field guide
- Start with VICSFFile decompression, then individual parse methods

**Depends on**: Ghidra struct definitions (#1)
**Effort**: Weeks (117 parse methods)

## What We Can Skip

| Item | Why Skip |
|------|----------|
| Memory card system (MC_*) | PS2-specific, replaced with file I/O |
| DNAS/Station login (VIWndDnas, VIWndStationLogin) | Dead online service |
| IOP module loading (VIEELoadIrx) | PS2-specific, audio replaced entirely |
| VIDictionary internals | Works via reference counting, well-understood pattern |
| Camera system | Small (~10 methods), straightforward, can read when needed |
| Individual game entity types | 100+ types in createByName, reverse only as-needed |

## Documents Reference

| Document | Contents |
|----------|----------|
| `docs/subsystem-analysis.md` | Deep subsystem analysis (17 systems, 1,262 lines) |
| `docs/viraster-call-graph.md` | VIRaster rendering pipeline call graph |
| `docs/engine-architecture.md` | Engine structure from ELF symbol table |
| `docs/engine-map.json` | Machine-readable engine map (4,701 functions) |
| `docs/slavedriver-comparison.md` | Slavedriver→Snowblind evolution mapping |
| `docs/elf-analysis-2026-02-20.md` | ELF binary analysis results |
| `docs/research-2026-02-20.md` | Phase 1 research + risk pre-mortem |
| `docs/demon-stone-source-map.md` | Demon Stone source tree, class mapping (618 files, 655 classes) |
| `docs/demon-stone-class-members.md` | All class members from symbol mangling (6,041 members) |
| `docs/demon-stone-types.json` | Deduplicated struct layouts with byte offsets (1,211 types) |
| `docs/TOOLCHAIN.md` | Environment setup guide |
| `output/type-mapping.json` | Cross-referenced Cl*→VI* type mapping (34 classes, 942 members) |
| `output/snowblind-types.h` | Ghidra-importable C header (1,023 lines) |
| `output/offset-xref.md` | Decompiled offset vs struct member cross-reference (2,091 lines) |
