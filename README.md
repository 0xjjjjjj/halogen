# halogen

Reverse engineering the Snowblind Engine (PS2) for native ports and optimization.

## Target Games (Snowblind Engine)

- Champions of Norrath (2004)
- Champions: Return to Arms (2005)
- Baldur's Gate: Dark Alliance (2001)
- Baldur's Gate: Dark Alliance II (2004)
- Everquest Online Adventures (2003)
- Justice League Heroes (2006)

## Why

- 25K+ petition signatures for Champions of Norrath remaster - will never happen
- All Snowblind games run poorly on PCSX2 (10 FPS in caves, particle effects kill performance)
- Zero reverse engineering or modding community exists
- PS2Recomp (2026) makes this tractable - converts PS2 ELF → C++ automatically

## Approach

```
PS2 Game Binary (ELF)
    │
    ▼
PS2Recomp (static recompiler → C++)
    │
    ▼
Snowblind Engine analysis & optimization
    │
    ▼
Native builds (PC, ARM, wherever)
```

## Status

Research phase. No code yet.
