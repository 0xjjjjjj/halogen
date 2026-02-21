# halogen - Snowblind Engine Reverse Engineering

## Project Overview

Reverse engineer the Snowblind Engine (PS2) to enable native ports and optimization patches for Champions of Norrath and related titles. Uses PS2Recomp + Ghidra + paraLLEl-GS as the toolchain.

## Current State

**Phase 2: Engine Understanding — static analysis complete, need runtime analysis.**

Phase 1 done. Phase 2 static analysis done (2026-02-21). ELF acquired, PS2Recomp run (9,395 C++ files), complete engine architecture mapped from symbol table + recomp output. Every major subsystem traced via ast-grep call graph extraction. Demon Stone prototype provides full struct layouts with byte offsets (1,211 types, 7,595 members).

### What's done
- ELF extracted and analyzed (SLUS-20565, 5.6MB, .mdebug confirmed empty across all builds)
- PS2Recomp recompilation: 9,395 C++ files generated
- ELF symbol table mapped: 4,701 functions classified by subsystem
- Demon Stone prototype: 9.3MB Metrowerks DWARF1 debug info → 1,211 struct layouts recovered
- Cl* (Stormfront) → VI* (Snowblind) class mapping established (same engine, different naming)
- VU1 microcode found in DVP overlay sections (16 overlays, 2 programs: RasterMicro, BillboardMicro)
- Complete engine architecture documented (17 subsystems, 1,262 lines)
- VIRaster rendering pipeline: call graph, 5 vertex formats, material LRU, DMA double buffering
- VIZone: BSP traversal, pre-translation, collision integration
- VIParticle: motif blending, billboard rendering, lighting bottleneck traced
- ESF/CSF: asset format pipeline, 117 parse methods covering all asset types
- VIPointLight/VIColorBuffer: per-vertex dynamic lighting (the cave bottleneck)
- VISoundDevice: IOP bridge, SPU2 channel management, VAG/XM formats
- VIWorld: grid terrain, profile blending, dual streaming modes
- VIHSprite/VICSprite: 156 methods, bone animation, character customization
- VIAtmosphere: weather raycasting, billboard layers, audio transitions
- VILoader: async I/O with DMA alignment, ESF parsing on complete
- VICollide: 3 buffer formats, per-sprite collision dispatch
- AMX/Pawn scripting VM with JIT compilation
- Game entity layer: createByName factory (100+ types), Player::msg_run, Creature base class
- Engine boot sequence (engineInit → 22 subsystems in dependency order)
- Game loop (gameLoop: sequential sim + render)
- UI system (VIWnd: 14+ window types, retained-mode widget tree)
- Networking (344 files, custom DRDP protocol, peer-to-peer)
- Slavedriver Engine source comparison (docs/slavedriver-comparison.md)
- Demon Stone prototype analysis: source tree, class members, struct layouts (docs/demon-stone-*.md/json)
- Python DWARF1 type parser (tools/parse-dwarf1-types.py)
- Scuffed ETL pipeline for video analysis (configs/scuffed-re-profile.yaml)
- ast-grep call graph extraction tool (tools/extract-callgraph.sh)
- Ghidra 11.4.2 + ghidra-emotionengine-reloaded v2.1.33 set up on sleeper5

### What's next
See docs/phase2-status.md for concrete next steps. Summary:
1. **Ghidra session** — load ELF, import Demon Stone struct layouts, decompile VIScene::Render
2. **Cl* → VI* type mapping** — script to match Demon Stone structs to CoN symbols
3. **PCSX2 runtime tracing** — trace VU1 uploads, DMA packets, GS register writes
4. **VU1 microcode extraction** — DVP overlay sections, defer until interpreter layer
5. **paraLLEl-GS evaluation** — test with captured GS command streams

## Key Research Findings (Phase 1)

### paraLLEl-GS solves the GS problem
- `github.com/Arntzen-Software/parallel-gs` — Vulkan compute-shader GS emulator
- Same author as paraLLEl-RDP (shipped in N64 Recompiled, production quality)
- We integrate this as the rendering backend instead of writing a GPU driver
- This was the biggest risk; it's now a paper tiger

### Debug symbols — .mdebug empty, Demon Stone has DWARF1 instead
- `.mdebug.eabi64` is 0 bytes in ALL Snowblind builds (retail, demo, prototype) — toolchain decision
- Demon Stone prototype (Stormfront Studios, same engine) has 9.3MB of Metrowerks DWARF1 in `.debug`
- Recovered 1,211 struct layouts, 7,595 members, 129 enums — the complete engine type system
- Cl* prefix (Stormfront) = VI* prefix (Snowblind), direct mapping established
- Engine internal codename: "Phoenix", animation system: "Noam"
- Parser: `tools/parse-dwarf1-types.py`, output: `docs/demon-stone-types.json`

### Cave performance bottleneck — SOLVED
- Each torch = VIParticleSprite (billboard particles) + VIPointLight (VIColorBuffer per-vertex overlay)
- VIColorBuffer lock/unlock cycle re-renders geometry per light — N lights = N× overdraw
- 10 torches × 20 particles + 10 light passes = 400+ draw operations
- This is architectural, not a bug — it's how the engine does dynamic lighting without pixel shaders
- PCSX2's "Fast Texture Invalidation" partially helps by reducing VIColorBuffer invalidation overhead
- Native port fix: replace VIPointLight/VIColorBuffer with modern per-pixel lighting

### VU1 microcode — found in DVP overlays (defer until needed)
- PS2Recomp can't handle VU1 programs (geometry processing)
- `.vudata`/`.vubss` are zeroed, but actual VU1 code lives in `.DVP.overlay.*` ELF sections
- Retail CoN: 16 DVP overlays (2 VU1 programs), demo/prototype: 8 overlays (1 program)
- 2 programs confirmed: RasterMicro (general geometry) and BillboardMicro (billboards)
- Upload boundary fully traced: UploadRasterMicro, UploadBillboardMicro, UploadMatrices, UploadPreTrans
- Mitigation: extract DVP overlay sections, build VU1 interpreter layer
- Don't dig in until actively building the interpreter — need runtime tracing first

### Self-modifying code (mitigated)
- PS2 loads VU programs via DMA at runtime (invisible to static recompiler)
- Mitigation: N64Recomp's LOOKUP_FUNC pattern for dynamic jumps
- VIF packet parser to catalogue all VU programs loaded during gameplay

## The Snowblind Engine

Used by Snowblind Studios (later acquired by WB Games → shut down). Powers:
- Champions of Norrath (2004) — primary target, SLUS-20565
- Champions: Return to Arms (2005)
- Baldur's Gate: Dark Alliance (2001)
- Baldur's Gate: Dark Alliance II (2004)
- Everquest Online Adventures (2003)
- Justice League Heroes (2006)

Also called the "Dark Alliance engine." Created by Ezra Dreisbach. Zero public technical documentation exists — everything we learn is original.

## Toolchain

| Tool | Purpose | Status |
|------|---------|--------|
| PS2Recomp | MIPS R5900 → C++ static recompilation | Done — 9,395 files generated |
| Ghidra + ghidra-emotionengine-reloaded | Manual RE, decompilation | Ready on sleeper5 (Ghidra 11.4.2, EE-Reloaded v2.1.33) |
| paraLLEl-GS | Vulkan GS emulator (rendering backend) | Phase 3 integration |
| PCSX2 debugger | Runtime analysis, pointer tracking | Available |
| ast-grep | C++ AST-based call graph extraction | Working — tools/extract-callgraph.sh |
| scuffed | Video analysis ETL pipeline | Working — configs/scuffed-re-profile.yaml |
| Python (lief, capstone, pyelftools) | ELF analysis scripts | Used for initial ELF analysis |

Setup instructions: `docs/TOOLCHAIN.md`

## Repo Structure

```
halogen/
├── CLAUDE.md                          # This file
├── README.md                          # Project overview
├── docs/
│   ├── research-2026-02-20.md         # Phase 1 research + risk mitigations
│   ├── elf-analysis-2026-02-20.md     # ELF binary analysis results
│   ├── engine-architecture.md         # Engine structure from symbol table
│   ├── engine-map.json                # Machine-readable engine map
│   ├── slavedriver-comparison.md      # Slavedriver→Snowblind evolution
│   ├── subsystem-analysis.md          # Deep subsystem analysis (1,262 lines)
│   ├── viraster-call-graph.md         # VIRaster rendering pipeline
│   ├── phase2-status.md               # Current status + next steps
│   ├── demon-stone-source-map.md      # Demon Stone source tree + class mapping
│   ├── demon-stone-class-members.md   # Class members from symbol mangling
│   ├── demon-stone-types.json         # Struct layouts with byte offsets (1,211 types)
│   └── TOOLCHAIN.md                   # Environment setup guide
├── configs/
│   ├── champions-of-norrath.toml      # PS2Recomp config
│   └── scuffed-re-profile.yaml        # Video analysis ETL config
├── tools/
│   ├── extract-callgraph.sh           # ast-grep call graph extraction
│   └── parse-dwarf1-types.py          # DWARF1 struct layout parser (Python)
├── output/
│   ├── champions-of-norrath/          # PS2Recomp C++ output (9,395 files)
│   ├── ps2-gpu-graphics-synthesizer.{md,json}  # Scuffed: GS hardware analysis
│   └── baldurs-gate-legacy/           # Scuffed: DA video analysis
└── notes/                             # RE notes, function annotations (future)
```

## Approach (3 phases)

### Phase 1: Reconnaissance — COMPLETE
- ~~Research toolchain and engine~~ done
- ~~Get Champions of Norrath ELF extracted~~ done (SLUS-20565)
- ~~Run through PS2Recomp, assess output quality~~ done (9,395 files)
- ~~Identify Snowblind Engine structures~~ done (17 subsystems mapped)
- ~~Map the binary: engine vs game-specific code~~ done (engine=VI* C++ OOP, game=C-style)

### Phase 2: Engine Understanding — STATIC ANALYSIS COMPLETE
- ~~Reverse the renderer~~ done (VIRaster pipeline, VIColorBuffer lighting, bottleneck traced)
- ~~Reverse the asset pipeline~~ done (ESF/CSF format, 117 parse methods, VILoader async I/O)
- ~~Identify the scripting/gameplay layer~~ done (AMX/Pawn VM with JIT, createByName factory)
- ~~Document engine architecture~~ done (1,262 lines, 17 subsystems, 17 insights)
- ~~Recover struct layouts~~ done (Demon Stone prototype: 1,211 types, 7,595 members)
- ~~Locate VU1 microcode~~ done (DVP overlay sections, 2 programs confirmed)
- Ghidra decompilation + Demon Stone type import — **NEXT**
- Runtime validation via PCSX2 — **NEXT**

### Phase 3: Native Port
- PS2Recomp C++ output as EE code base
- VU1 interpreter layer for geometry
- paraLLEl-GS as Vulkan rendering backend
- Fix performance issues at source
- Native PC build, then ARM

## Connections to Other Projects

- **ogx** (~/git/ogx) — Sister project, OG Xbox emulation on ARM handhelds
- Both stem from same conversation about emulation gaps
- Halogen is higher community impact (25K petition, 6 games, no existing work)

## References

- PS2Recomp: https://github.com/ran-j/PS2Recomp
- ghidra-emotionengine-reloaded: https://github.com/chaoticgd/ghidra-emotionengine-reloaded
- paraLLEl-GS: https://github.com/Arntzen-Software/parallel-gs
- ps2tek (HW docs): https://psi-rockin.github.io/ps2tek/
- N64Recomp (playbook): https://github.com/N64Recomp
- retroreversing.com/ps2: https://www.retroreversing.com/ps2
- RE:CVX decompilation: https://residentevil.org/threads/re-cvx-decompilation-project-ps2-ver.13514/

## Context

- Repo: https://github.com/0xjjjjjj/halogen (private)
- Back burner behind freelance cash flow
- Flex/reach project — sustained by curiosity
- Learnings stored in claude memory under tags: halogen, snowblind, ps2, decomp, reverse-engineering
