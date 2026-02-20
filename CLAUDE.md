# halogen - Snowblind Engine Reverse Engineering

## Project Overview

Reverse engineer the Snowblind Engine (PS2) to enable native ports and optimization patches for Champions of Norrath and related titles. Uses PS2Recomp as the starting point for decompilation.

## Current State

**Phase: Research. No code yet.**

## Background

- Friend identified Champions of Norrath as a game that famously runs poorly on emulators
- 25K+ petition for a remaster that's never coming
- Snowblind Engine powers 6+ PS2 games with cult followings, none remastered
- PS2 decomp scene is exploding (Jan 2026): PS2Recomp, OpenGOAL, RE:CVX decomp
- Nobody is working on Snowblind Engine specifically

## The Snowblind Engine

Used by Snowblind Studios (later acquired by WB Games → shut down). Powers:
- Champions of Norrath (2004)
- Champions: Return to Arms (2005)
- Baldur's Gate: Dark Alliance (2001)
- Baldur's Gate: Dark Alliance II (2004)
- Everquest Online Adventures (2003)
- Justice League Heroes (2006)

Known issues on PCSX2:
- 10 FPS in caves/underground areas
- Particle effects (fire) destroy performance
- "Fast Texture Invalidation" hack partially helps
- Higher resolution scaling makes it worse

## Key Tools

- **PS2Recomp** (github.com/ran-j/PS2Recomp) - Static recompiler, PS2 ELF → C++. GPL-3.0. Early stage, actively seeking contributors.
- **PCSX2** - Reference for how the games behave under emulation
- **Ghidra** - For manual RE when PS2Recomp needs help
- **decomp.me** - Collaborative decompilation platform

## Approach (3 phases)

### Phase 1: Reconnaissance
- Get Champions of Norrath ELF extracted
- Run through PS2Recomp, see what comes out
- Identify Snowblind Engine structures (renderer, audio, physics, scripting)
- Map the binary: what's engine vs what's game-specific
- Study PCSX2 game-specific hacks for clues about engine behavior

### Phase 2: Engine Understanding
- Reverse the renderer (what makes it choke on particles/caves)
- Reverse the asset pipeline (models, textures, levels)
- Identify the scripting/gameplay layer
- Document engine architecture

### Phase 3: Native Port
- Use PS2Recomp output as base
- Replace PS2 renderer with modern Vulkan/OpenGL
- Fix the performance issues at source (not emulator hacks)
- Native PC build, potentially ARM builds too

## Connections to Other Projects

- **ogx** (~/git/ogx) - Sister project, OG Xbox emulation on ARM handhelds
- Both stem from the same conversation about emulation gaps
- Halogen is higher community impact (25K petition, 6 games, no existing work)
- ogx is more straightforward engineering (xemu already mostly works on ARM)

## References

- PS2Recomp: https://github.com/ran-j/PS2Recomp
- N64Recomp (inspiration): https://github.com/N64Recomp
- decomp.me: https://decomp.me
- Snowblind Engine wiki: search for game-specific technical docs
- PCSX2 forums: Champions of Norrath performance threads
- Change.org petition: https://www.change.org/p/time-warner-remaster-champions-of-norrath-for-ps4-and-xbox-1

## Context

- Repo: https://github.com/0xjjjjjj/halogen (private)
- Back burner behind freelance cash flow (like ogx)
- Learnings stored in claude memory under tags: halogen, snowblind, ps2, decomp, reverse-engineering
