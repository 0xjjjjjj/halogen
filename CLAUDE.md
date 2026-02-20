# halogen - Snowblind Engine Reverse Engineering

## Project Overview

Reverse engineer the Snowblind Engine (PS2) to enable native ports and optimization patches for Champions of Norrath and related titles. Uses PS2Recomp + Ghidra + paraLLEl-GS as the toolchain.

## Current State

**Phase 1: Reconnaissance — research complete, awaiting binary.**

Research sprint done (2026-02-20). Toolchain identified, risks assessed and mitigated, repo scaffolded. Blocked on acquiring Champions of Norrath ISO/ELF.

### What's done
- Full research: PS2Recomp, Ghidra extensions, PCSX2 hacks, Snowblind architecture
- Risk pre-mortem with mitigations for all tigers
- Repo structure: docs/, tools/, configs/, notes/
- PS2Recomp TOML config stub for CoN
- Toolchain setup guide (docs/TOOLCHAIN.md)

### What's blocked
- No game binary yet (Champions of Norrath ISO / BASLUS_20565.ELF)

### Next steps (when binary is available)
1. Extract ELF from ISO: `7z x` or `isoinfo`
2. Check for debug symbols: `readelf -S BASLUS_20565.ELF | grep mdebug`
3. Run PS2Recomp against ELF
4. Load into Ghidra with ghidra-emotionengine-reloaded
5. Map engine structure from C++ output + disassembly

## Key Research Findings (Phase 1)

### paraLLEl-GS solves the GS problem
- `github.com/Arntzen-Software/parallel-gs` — Vulkan compute-shader GS emulator
- Same author as paraLLEl-RDP (shipped in N64 Recompiled, production quality)
- We integrate this as the rendering backend instead of writing a GPU driver
- This was the biggest risk; it's now a paper tiger

### Debug symbols may exist in retail ELF
- ghidra-emotionengine-reloaded recovers `.mdebug` section data
- Many early PS2 games retained debug symbols in retail builds
- If CoN has them: function names for free, weeks of manual RE avoided
- **First thing to check when binary is acquired**

### PCSX2 performance clues
- "Fast Texture Invalidation" partially helps caves → aggressive texture cache manipulation
- Hypothesis: render-to-texture for dynamic lighting/shadows
- Particles (fire) = dynamic lights requiring additional passes
- The fix is "render differently," not "run faster"

### VU1 microcode gap (mitigated)
- PS2Recomp can't handle VU1 programs (geometry processing)
- No VU1 disassembler exists anywhere
- Mitigation: extract `.vudata` section, build VU1 interpreter layer
- Phase 1 stubs VU1, Phase 2 implements interpreter

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
| PS2Recomp | MIPS R5900 → C++ static recompilation | Ready to build |
| Ghidra + ghidra-emotionengine-reloaded | Manual RE, symbol recovery, .mdebug parsing | Ready to install |
| paraLLEl-GS | Vulkan GS emulator (rendering backend) | Phase 3 integration |
| PCSX2 debugger | Runtime analysis, pointer tracking | Available |
| Python (lief, capstone, pyelftools) | ELF analysis scripts | Future (tools/) |
| Rust (goblin, capstone-rs) | Performance binary processing | Future |

Setup instructions: `docs/TOOLCHAIN.md`

## Repo Structure

```
halogen/
├── CLAUDE.md                          # This file
├── README.md                          # Project overview
├── docs/
│   ├── research-2026-02-20.md         # Phase 1 research + risk mitigations
│   └── TOOLCHAIN.md                   # Environment setup guide
├── configs/
│   └── champions-of-norrath.toml      # PS2Recomp config
├── tools/                             # Python analysis scripts (future)
└── notes/                             # RE notes, function annotations (future)
```

## Approach (3 phases)

### Phase 1: Reconnaissance (current)
- ~~Research toolchain and engine~~ done
- Get Champions of Norrath ELF extracted
- Run through PS2Recomp, assess output quality
- Identify Snowblind Engine structures (renderer, audio, physics, scripting)
- Map the binary: engine vs game-specific code
- Study PCSX2 GameDatabase.yaml for CoN entries

### Phase 2: Engine Understanding
- Reverse the renderer (what makes it choke on particles/caves)
- Build VU1 interpreter for geometry processing
- Reverse the asset pipeline (models, textures, levels)
- Identify the scripting/gameplay layer
- Document engine architecture

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
