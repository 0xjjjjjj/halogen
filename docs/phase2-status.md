# Phase 2 Status — Static Analysis Complete

As of 2026-02-20. All analysis from PS2Recomp C++ output is exhausted. Next steps require runtime tools (Ghidra, PCSX2) or implementation work.

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

## What's Left — Ranked by Value

### Tier 1: High value, do next

#### 1. Ghidra Session
**Why**: PS2Recomp missed some functions (e.g., VIScene::Render at 0x0113bb48). Ghidra + ghidra-emotionengine-reloaded can decompile these AND leverage .mdebug debug symbols for struct layouts and local variable names.

**Concrete steps**:
- Load SLUS-20565 ELF into Ghidra with EE-Reloaded extension
- Auto-analyze with .mdebug symbol recovery
- Cross-reference our 4,701-symbol map against Ghidra's analysis
- Decompile VIScene::Render (912 bytes) — the main rendering orchestrator
- Export struct definitions for VI* classes

**Effort**: 2-3 hours setup + ongoing exploration

#### 2. PCSX2 Runtime Tracing
**Why**: VU1 microcode and GS register writes are invisible to static analysis. Need to see what actually happens at runtime.

**Concrete steps**:
- Run Champions of Norrath in PCSX2 debug build
- Enable GS dump capture (Tools → GS Dump)
- Capture a cave scene (torches + particles) and an outdoor scene (weather)
- Trace VIF DMA packets to catalogue VU1 program uploads
- Record GS register writes per frame to understand draw call patterns

**Effort**: 1-2 hours per scene capture

### Tier 2: Medium value, do when needed

#### 3. VU1 Microcode Extraction
**Why**: Need to build a VU1 interpreter for the native port. But only matters when we're actually implementing the interpreter layer.

**Concrete steps**:
- Extract .vudata section from ELF: `readelf -x .vudata SLUS-20565.ELF`
- Write a VU1 disassembler (VU1 instruction set is documented in ps2tek)
- OR: capture VU1 uploads via PCSX2 VIF tracing (more complete — catches runtime-loaded programs)
- Catalogue all unique VU1 programs and their vertex format signatures

**Depends on**: PCSX2 runtime tracing (#2)
**Effort**: Days to weeks (VU1 instruction set is complex)

#### 4. paraLLEl-GS Evaluation
**Why**: Need to verify paraLLEl-GS can actually consume the GS command stream Champions of Norrath generates.

**Concrete steps**:
- Build paraLLEl-GS from source
- Feed it a PCSX2 GS dump from step #2
- Check rendering accuracy vs PCSX2 software renderer
- Identify any unsupported GS features

**Depends on**: PCSX2 GS dump capture (#2)
**Effort**: Half day build + test

### Tier 3: Low value until implementation

#### 5. AMX/Pawn Script Extraction
**Why**: Need to understand what scripts do and whether JIT recompilation is needed.

**Concrete steps**:
- Find .pawn or script data in ESF files
- Use existing Pawn tools to decompile scripts
- Assess whether scripts can run interpreted (no JIT) at acceptable speed

**Effort**: Hours to find scripts, then standard Pawn tooling

#### 6. ESF File Format Reversing
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
| `docs/TOOLCHAIN.md` | Environment setup guide |
