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
   ELF Extraction
   (7-Zip / isoinfo)
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

## Why This Is Tractable Now (2026)

- **PS2Recomp** — Static recompiler: PS2 ELF → C++. Early stage but functional foundation.
- **ghidra-emotionengine-reloaded** — Ghidra extension with full EE/MMI/VU0 support. Recovers debug symbols from `.mdebug` sections (many PS2 games retained them in retail).
- **paraLLEl-GS** — Vulkan compute-shader Graphics Synthesizer emulator. Same author as paraLLEl-RDP, which shipped in N64 Recompiled. We don't write a GPU driver — we integrate this.
- **N64 Recompiled** — Proved the pattern. N64 → native binary, shipped, runs great. PS2 is harder but the playbook exists.

## Architecture Notes

### The Performance Problem (Hypothesis)

PCSX2's "Fast Texture Invalidation" patch partially helps in cave areas, suggesting the Snowblind renderer does aggressive texture cache manipulation — likely render-to-texture for dynamic lighting/shadows. Particles (fire) create many dynamic lights, each requiring additional passes. The fix isn't "run faster" — it's "render differently."

### Known Engine Details

- **VU1**: Used for geometry processing (vertex transforms). VU microcode lives in `.vudata` ELF section.
- **GIF**: All rendering goes through GIF DMA tags to the Graphics Synthesizer.
- **Overlays**: Game content loaded via DMA during runtime (caves = content stream events).
- **Creator**: Ezra Dreisbach (Snowblind Studios programmer).

### Risks Acknowledged

| Risk | Mitigation |
|------|-----------|
| VU1 microcode unreadable by PS2Recomp | Extract `.vudata`, build VU1 interpreter layer |
| DMA-loaded code (self-modifying) | N64Recomp LOOKUP_FUNC pattern for dynamic jumps |
| GS replacement complexity | paraLLEl-GS exists, use it |
| No debug symbols in retail ELF | First thing to check; if absent, Ghidra + PCSX2 debugger |

## Repo Structure

```
halogen/
├── docs/           # Research, findings, architecture notes
│   └── research-2026-02-20.md
├── tools/          # Python analysis scripts (future)
├── configs/        # PS2Recomp TOML configs (future)
├── notes/          # RE notes, function annotations (future)
└── TOOLCHAIN.md    # Environment setup
```

## Status

**Phase 1: Reconnaissance** (in progress)

- [x] Research: PS2Recomp, Ghidra extensions, PCSX2 hacks, Snowblind architecture
- [x] Risk analysis + mitigations identified
- [ ] Binary: Champions of Norrath ELF not yet acquired
- [ ] Toolchain: PS2Recomp + Ghidra setup pending binary
- [ ] Analysis: engine structure mapping pending binary

## References

### Tools
- [PS2Recomp](https://github.com/ran-j/PS2Recomp) — Static recompiler
- [ghidra-emotionengine-reloaded](https://github.com/chaoticgd/ghidra-emotionengine-reloaded) — Ghidra EE extension
- [paraLLEl-GS](https://github.com/Arntzen-Software/parallel-gs) — Vulkan GS emulator
- [ps2tek](https://psi-rockin.github.io/ps2tek/) — PS2 hardware documentation

### Prior Art
- [N64 Recompiled](https://github.com/N64Recomp/N64Recomp) — The playbook
- [RE:CVX Decompilation](https://residentevil.org/threads/re-cvx-decompilation-project-ps2-ver.13514/) — PS2 RE example
- [retroreversing.com/ps2](https://www.retroreversing.com/ps2) — PS2 RE overview

### Community
- 25K petition: [Change.org — Remaster Champions of Norrath](https://www.change.org/p/time-warner-remaster-champions-of-norrath-for-ps4-and-xbox-1)
- PCSX2 CoN performance: see `docs/research-2026-02-20.md`
