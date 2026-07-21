# halogen

> Reverse engineering the Snowblind Engine (PS2) to build native ports and fix what emulators can't.

## The Problem

Six PS2 games share a common engine. All six run poorly on PCSX2 — 10 FPS in caves, particle effects that destroy framerates, performance problems that no amount of emulator tuning fully fixes. A remaster will never come. The source code is gone.

The fix is to understand the engine well enough to run it natively.

## Target Games (Snowblind Engine)

| Game | Year | Notes |
|------|------|-------|
| Baldur's Gate: Dark Alliance | 2001 | Engine v1 |
| Everquest Online Adventures | 2003 | Network adapter support |
| Baldur's Gate: Dark Alliance II | 2004 | Engine v2 |
| Champions of Norrath | 2004 | Primary target (SLUS-20565) |
| Champions: Return to Arms | 2005 | Engine v3 |
| Justice League Heroes | 2006 | Final Snowblind game |

## Approach

```
PS2 Game Disc (ISO)
        │
        ▼
   ELF Extraction (isoinfo)
        │
        ▼
   PS2Recomp ──────────────────────── Ghidra (manual RE)
   (MIPS R5900 → C++)                 (ghidra-emotionengine-reloaded)
        │                                       │
        ├───────────────────────────────────────┤
        │
        ▼
   Engine analysis: renderer, audio, physics, scripting
        │
        ▼
   Native build
   EE code: recompiled C++
   VU1: interpreter layer
   GS:  paraLLEl-GS (Vulkan)
        │
        ▼
   Native PC binary (then ARM, wherever)
```

## Status (2026-07-20)

**Phase 1: Reconnaissance — DONE.** Toolchain validated, engine identified, risks mitigated.

**Phase 2: Engine Understanding — DONE.**
- ELF extracted (SLUS-20565, 5.6 MB) + fully classified (4,701 functions across 17 subsystems).
- PS2Recomp regenerated 9,395 C++ files that compile clean.
- Demon Stone prototype (same engine, DWARF1 debug info retained) → 1,211 struct layouts, 7,595 members, complete type recovery.
- Full renderer, asset pipeline, scripting VM, boot sequence, and networking all mapped.

**Phase 3: Native Port — IN PROGRESS.**

Where we are:
- `halogen-headless` binary boots the recompiled C++ successfully.  Engine reaches steady state at ~55 FPS with all subsystems running (renderer task list, sound, world logic, memory-card, network).
- Game progresses through boot → engineInit → gameInit → gameLoop → runFrontEnd (main menu).  Live pad input drives menus (mash mode injects X+Down+Start+Up).
- GS dump pipeline: `HALOGEN_GS_DUMP=/path/to/file.gs` writes a PCSX2-format dump of every GIF DMA the recompiled engine emits.
- paraLLEl-GS integration validated end-to-end: a patched `parallel-gs-replayer` reads our dumps and produces real 640×448 PNG scanout frames.  Proven with the town.gs dump captured from PCSX2 (`docs/pcsx2-town-frame.png` = wooden bridge with HUD).
- 12+ commits landed this session across the halogen main repo and our PS2Recomp fork fixing a chain of deadlocks: cooperative-yield discipline for the guest-exec mutex, ReferThreadStatus semantics, KbmReader IOP spin, textureSmoothBorder infinite loop on missing textures.

What's blocking real gameplay screenshots from halogen's own emission:
- The game hangs at menu screens (character-select, item-generation) because the asset system (`lumpFind`) returns garbage/empty for missing textures, and many game loops assume the data is valid and spin forever.  Each surface patch reveals the next one; the real fix is upstream in `lumpFind` itself.
- Once the game reaches actual gameplay, `gameDrawWorld` emits thousands of draws per frame → paraLLEl-GS → real pixels.  Blocked, not architected-away.

Why still headless?  Not for long.  The `-headless` build was a debugging convenience — the original halogen binary linked raylib for a display window; the headless variant strips that so we can iterate on boot bugs without display friction.  Now that boot works, next architectural move is **live paraLLEl-GS integration** (task #3320): link paraLLEl-GS as a library in-process, feed GIF DMA in real time, present via a Vulkan window.  That kills the need for both the headless dispatch loop AND the dump→replay two-step, and gives us `./halogen → see game`.

What's next, in order:
1. **Live paraLLEl-GS integration** — real-time visible output, kills headless.
2. **Fix asset system root cause** so game-loading paths don't cascade into infinite loops.
3. **VU1 interpreter layer** for the two extracted microcode programs (`RasterMicro`, `BillboardMicro`).
4. **Cave-bottleneck fix** — replace VIColorBuffer per-vertex lighting with per-pixel.
5. **Native ARM build** for handheld/mobile.

## Key Research Findings

### paraLLEl-GS solves the GS problem
`github.com/Arntzen-Software/parallel-gs` — Vulkan compute-shader GS emulator.  Same author as paraLLEl-RDP (shipped in N64 Recompiled, production quality).  We integrate this as the rendering backend instead of writing a GPU driver.  Validated in-session: 100+ replay iterations on our own emitted dumps, clean, no errors, ~384 MiB stable GPU memory.

### Debug symbols recovered from a sibling game
`.mdebug.eabi64` is 0 bytes in every Snowblind retail build — Metrowerks toolchain decision.  BUT Demon Stone (Stormfront Studios, same engine) shipped with 9.3 MB of Metrowerks DWARF1 debug info.  Parser: `tools/parse-dwarf1-types.py`, output: `docs/demon-stone-types.json`.  Cl* (Stormfront) → VI* (Snowblind) class-name mapping established.  Engine internal codename: "Phoenix", animation system: "Noam".

### Cave performance bottleneck — SOLVED
Each torch = VIParticleSprite (billboard particles) + VIPointLight (VIColorBuffer per-vertex overlay).  VIColorBuffer lock/unlock cycle re-renders geometry per light — N lights = N× overdraw.  10 torches × 20 particles + 10 light passes = 400+ draw operations per frame per torch.  Architectural, not a bug.  Native port fix: replace with modern per-pixel lighting.  Runtime trace confirms: goblin caves at 102,658 draws/frame vs town at 73,720.

### VU1 microcode extracted
`.vudata`/`.vubss` are zeroed but real code lives in `.DVP.overlay.*` ELF sections.  Retail has 16 DVP overlays, 2 VU1 programs: `RasterMicro` (1,868 instr, general geometry) and `BillboardMicro` (2,029 instr, particles).  Extracted to `output/vu1/`.

## Env vars (runtime knobs on `halogen-headless`)

| Var | Effect |
|---|---|
| `HALOGEN_GS_DUMP=path` | Write a PCSX2-compatible `.gs` of every GIF DMA the recompiled engine emits.  Feed to paraLLEl-GS replayer for pixel-level inspection. |
| `HALOGEN_PAD_MASH=1` | Cycle X / Down / Start / Up through scePadRead for automated menu advance. |
| `HALOGEN_PAD_MASH=debug` | Hold L2+R2+Start (the debug-menu chord from the pnach). |
| `HALOGEN_DEBUG_MENU=1` | Apply the pnach debug-menu enable patch at 0x17FA04 during ELF load. |
| `HALOGEN_FORCE_LEVEL=name` | Override the world-name string passed to `gameLoadWorld`.  Names: `intro`, `kelsel`, `kelethin`, `faydark1`, `goblin1`, `anthill1`, `battle1`, `lava1`, `orccave1`, etc. (see `bin/disc/BG/DATA/*.GOB`). |
| `HALOGEN_SKIP_TASKS=runFrontEnd` | Bypass task entries in the engineRunTasks blacklist (current hardcode: `runFrontEnd` at 0x1c8098). |
| `--cd-root DIR` | CLI arg. Filesystem root for CD ops.  Auto-detects via `SYSTEM.CNF` if unset. |

## Repo Structure

```
halogen/
├── README.md
├── CLAUDE.md                       # Full project state for agents
├── CMakeLists.txt                  # Root build
├── src/main_headless.cpp           # Headless dispatch loop (transitional; will merge with Vulkan build)
├── configs/
│   └── champions-of-norrath.toml   # PS2Recomp config
├── vendor/PS2Recomp/               # Nested clone of our fork (0xjjjjjj/PS2Recomp)
├── output/champions-of-norrath/    # 9,395 recompiled C++ files (gitignored)
├── docs/                           # Research + reverse-engineering findings
│   ├── engine-architecture.md      # 17 subsystems, 1,262 lines
│   ├── engine-map.json             # 6,447 functions with addresses/sizes
│   ├── demon-stone-types.json      # 1,211 struct layouts from DWARF1
│   ├── phase2-status.md            # Detailed Phase 2 completion state
│   ├── subsystem-analysis.md       # Deep per-subsystem analysis
│   ├── render-pipeline.md          # Ghidra manual analysis (42 fns, VU1 maps, scratchpad)
│   ├── viraster-call-graph.md      # Renderer call graph
│   ├── runtime-trace.md            # PCSX2 GS-dump analysis
│   ├── parallel-gs-eval.md         # paraLLEl-GS evaluation (GO for Phase 3)
│   ├── slavedriver-comparison.md   # Slavedriver → Snowblind evolution
│   ├── pcsx2-town-frame.png        # Proof of pipeline (town.gs → PNG)
│   └── vram-natural.png            # halogen's own VRAM dump (honest sample)
├── tools/
│   ├── parse-gs-dump.py            # PCSX2 GS dump parser (40 tests)
│   ├── extract-vu1.py              # VU1 microcode extractor from DVP overlays
│   ├── parse-dwarf1-types.py       # DWARF1 struct layout parser
│   ├── patch-recompiled.py         # Post-regen patches for recompiled C++
│   ├── parallel-gs-replayer-png-patch.cpp  # PNG-dump patch for paraLLEl-GS replayer
│   ├── parallel-gs-replayer.md     # Build + usage notes
│   ├── extract-callgraph.sh        # ast-grep call graph extraction
│   ├── ghidra-*.py                 # Ghidra batch-decomp + type-apply tools
│   ├── gen-*.py                    # Recompiler + linker stub generators
│   └── map_engine.py / map-types.py  # Engine classifiers
├── output/
│   ├── vu1/                        # Extracted VU1 programs (bin + disasm)
│   ├── goblin-cave.gs              # Worst-case GS dump (102K draws/frame)
│   ├── town.gs                     # Kelethin GS dump (73K draws/frame)
│   ├── cave.gs                     # Cave GS dump
│   └── cheats/90E66BC5.pnach       # Debug menu enabler
└── bin/disc/                       # Extracted disc image (gitignored)
```

## Toolchain

| Tool | Purpose | Status |
|------|---------|--------|
| PS2Recomp (0xjjjjjj fork) | MIPS R5900 → C++ static recompilation | Done — 9,395 files clean, 8 headless-mode patches committed |
| Ghidra 11.4.2 + ghidra-emotionengine-reloaded v2.1.33 | Manual RE, decompilation | 6,446 functions batch-decompiled |
| paraLLEl-GS | Vulkan GS emulator (rendering backend) | Validated end-to-end, PNG-dump patch built |
| PCSX2 debugger | Runtime analysis, pointer tracking | Available |
| ast-grep | C++ AST-based call graph extraction | Working — `tools/extract-callgraph.sh` |
| Python (lief, capstone, pyelftools) | ELF analysis + type recovery | Complete |

## Build (Ubuntu 24.04, x86_64 dev workstation)

```bash
git clone https://github.com/0xjjjjjj/halogen.git
cd halogen
git clone https://github.com/0xjjjjjj/PS2Recomp.git vendor/PS2Recomp  # nested, not a submodule
# ... run PS2Recomp against SLUS-20565 to populate output/champions-of-norrath/ ...
python3 tools/patch-recompiled.py                                     # apply post-regen fixes
mkdir -p build-headless && cd build-headless
cmake -DHEADLESS=1 -DCMAKE_BUILD_TYPE=RelWithDebInfo ..
make halogen-headless -j$(nproc)
```

Sample run (captures a GS dump + auto-mashes X to advance menus):
```bash
HALOGEN_GS_DUMP=/tmp/halogen.gs HALOGEN_PAD_MASH=1 \
  ./halogen-headless --cd-root ../bin/disc ../bin/disc/SLUS_205.65
```

## Why This Is Tractable Now (2026)

- **PS2Recomp** — Static recompiler: PS2 ELF → C++.  We've extended the fork with 8 headless-runtime patches (cooperative yields, thread-status fixes, cd-filesystem, GS dump export, priv-register snapshots).
- **ghidra-emotionengine-reloaded** — Ghidra extension with full EE/MMI/VU0 support.  Recovers debug symbols; we used it against the Demon Stone prototype to recover complete engine type info.
- **paraLLEl-GS** — Same author as paraLLEl-RDP (shipped in N64 Recompiled).  Now confirmed working end-to-end for our own emitted dumps.
- **N64 Recompiled** — Proved the pattern.  PS2 is harder but the playbook exists.

## References

### Tools
- [PS2Recomp](https://github.com/ran-j/PS2Recomp) — Static recompiler (upstream)
- [0xjjjjjj/PS2Recomp](https://github.com/0xjjjjjj/PS2Recomp) — Our fork with headless patches
- [ghidra-emotionengine-reloaded](https://github.com/chaoticgd/ghidra-emotionengine-reloaded) — Ghidra EE extension
- [paraLLEl-GS](https://github.com/Arntzen-Software/parallel-gs) — Vulkan GS emulator
- [ps2tek](https://psi-rockin.github.io/ps2tek/) — PS2 hardware documentation

### Prior Art
- [N64 Recompiled](https://github.com/N64Recomp/N64Recomp) — The playbook
- [RE:CVX Decompilation](https://residentevil.org/threads/re-cvx-decompilation-project-ps2-ver.13514/) — PS2 RE example
- [retroreversing.com/ps2](https://www.retroreversing.com/ps2) — PS2 RE overview

### Community
- 25K petition: [Change.org — Remaster Champions of Norrath](https://www.change.org/p/time-warner-remaster-champions-of-norrath-for-ps4-and-xbox-1)
