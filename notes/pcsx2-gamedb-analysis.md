# PCSX2 GameDatabase Analysis: Snowblind Engine Games

Extracted 2026-02-20 from PCSX2 `GameIndex.yaml` (76K lines).

## Shared Engine Patterns

**Every Snowblind game has the same 3 GS hardware fixes:**

| Fix | Comment | What it tells us |
|-----|---------|-----------------|
| `textureInsideRT: 1` | "Fixes half right" | **Engine renders textures inside render targets.** This is the smoking gun for the cave/particle performance issue. The engine uses render-to-texture (RTT) extensively — likely for dynamic lighting, shadows, or reflections. |
| `estimateTextureRegion: 1` | "Improves performance and reduces hash cache size" | **Engine uses non-standard texture regions.** PCSX2 can't efficiently hash the textures because the engine writes to unusual VRAM regions. |
| `gpuPaletteConversion: 1` | "Reduces hashcache size and improves performance" | **Engine uses GPU-side palette conversion.** The engine stores textures in paletted (CLUT) format and converts on the GS. This is a PS2 optimization that confuses the emulator's texture cache. |

**These 3 fixes appear in ALL 5 Snowblind games that have entries.** This is an engine-level pattern, not per-game quirks.

## Per-Game Entries

### Champions of Norrath (SLUS-20565) — Primary Target
```yaml
compat: 5  # Playable
gameFixes:
  - BlitInternalFPSHack  # Fixes internal fps detection in some areas
gsHWFixes:
  textureInsideRT: 1
  estimateTextureRegion: 1
  gpuPaletteConversion: 1
```

**`BlitInternalFPSHack`** — The engine has its own internal FPS detection. PCSX2 needs a hack to make the blit-based FPS counter work correctly. This suggests the engine has a custom frame pacing system.

### Baldur's Gate: Dark Alliance (SLUS-20035)
```yaml
compat: 5
gameFixes:
  - SoftwareRendererFMVHack  # Fixes FMVs
gsHWFixes:
  roundSprite: 1           # Fixes lines in menus
  textureInsideRT: 1
  estimateTextureRegion: 1
  gpuPaletteConversion: 1
```

### Baldur's Gate: Dark Alliance II (SLUS-20675)
```yaml
compat: 5
gameFixes:
  - SoftwareRendererFMVHack  # Fixes FMVs
gsHWFixes:
  textureInsideRT: 1
  estimateTextureRegion: 1
  gpuPaletteConversion: 1
  roundSprite: 1           # Fixes lines in sprites
```

### Champions: Return to Arms (SLUS-20973)
```yaml
compat: 5
gsHWFixes:
  textureInsideRT: 1
  estimateTextureRegion: 1
  gpuPaletteConversion: 1
  roundSprite: 1           # Fixes lines in menus/HUD/game
  halfPixelOffset: 2       # Fixes erroneous line in menus
memcardFilters:
  - "SLUS-20973"
  - "SLUS-20565"           # Cross-saves with Champions of Norrath!
```

### Justice League Heroes (SLUS-21304)
```yaml
compat: 5
clampModes:
  vuClampMode: 2  # Capes become SPS mess with lower VU clamp
gsHWFixes:
  textureInsideRT: 1
  estimateTextureRegion: 1
  gpuPaletteConversion: 1
```

**`vuClampMode: 2`** — VU floating-point clamping needed for geometry (capes). The Snowblind engine does VU math that produces values outside normal float range. The later engine version (JLH, 2006) pushes VU harder.

### EverQuest Online Adventures (SLUS-20470)
```yaml
# No fixes listed — minimal entry
```

### EverQuest Online Adventures: Frontiers (SLUS-20744)
```yaml
compat: 4  # In-Game (not fully Playable)
```

## Key Insights for Halogen

### 1. Render-to-Texture is Central
`textureInsideRT` being universal means the Snowblind renderer fundamentally relies on rendering textures into render targets. This is likely how it does:
- Dynamic lighting (render light map into texture, sample in final pass)
- Shadow mapping (render depth from light POV into texture)
- Particle compositing (render particles into texture, blend)

**For native port:** This maps well to Vulkan render passes / framebuffer attachments. paraLLEl-GS already handles this pattern.

### 2. Paletted Textures (CLUT)
The engine stores textures in 4-bit or 8-bit paletted format with Color Look-Up Tables. This is a PS2 optimization (saves VRAM bandwidth). The GS converts palettes to full color during rendering.

**For native port:** Need to handle CLUT conversion in the texture pipeline. Either convert at load time or use a palette texture in the shader.

### 3. Custom Frame Pacing
`BlitInternalFPSHack` means the engine doesn't just vsync — it has its own frame timing logic using blit operations to measure time. This may relate to the variable framerate issues.

### 4. VU Clamping (JLH only)
Later Snowblind engine version needs VU float clamping. This tells us the VU programs do math that can overflow IEEE floats. Our VU1 interpreter needs to handle PS2 float clamping behavior (PS2 floats are non-IEEE compliant).

### 5. Memory Card Cross-Save
Return to Arms reads Champions of Norrath saves. The save format is shared. If we can parse one game's saves, we can parse both.

## Correct Serial Numbers

| Game | NTSC-U Serial |
|------|---------------|
| Baldur's Gate: Dark Alliance | SLUS-20035 |
| EverQuest Online Adventures | SLUS-20470 |
| Champions of Norrath | SLUS-20565 |
| Baldur's Gate: Dark Alliance II | SLUS-20675 |
| EQ Online Adventures: Frontiers | SLUS-20744 |
| Champions: Return to Arms | SLUS-20973 |
| Justice League Heroes | SLUS-21304 |
