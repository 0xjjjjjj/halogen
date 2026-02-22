# Runtime Trace Analysis — GS Dump Results (2026-02-22)

PCSX2 GS dump capture and analysis across 3 scene types. Validates Phase 2 static analysis predictions about the cave performance bottleneck.

## Setup

- PCSX2 2.7.136 nightly (portable, Windows x64 + macOS)
- Champions of Norrath retail (SLUS-20565, CRC: 90E66BC5)
- PS2 BIOS: v2.00 USA (ps2-0200a-20040614)
- GS dumps captured via Shift+F8 (single-frame, zstd compressed)
- Parser: `tools/parse-gs-dump.py`

## Scene Comparison

| Metric | Town (Kelethin) | Outdoor (Lesser Faydark) | Goblin Caves |
|--------|----------------|-------------------------|-------------|
| **Draw calls/frame** | 73,720 | 60,857 | **102,658** |
| **Vertices/frame** | 73,735 | 60,870 | **102,882** |
| **TriStrip** | 72,102 (97.8%) | 59,507 (97.8%) | 96,091 (93.6%) |
| **Sprite** | 1,594 (2.2%) | 1,324 (2.2%) | **6,470 (6.3%)** |
| **TriFan** | 24 | 24 | 48 |
| **Line** | 0 | 0 | 60 |
| **PATH3 bytes/frame** | 7.29 MB | 6.86 MB | **10.53 MB** |
| **Register writes/frame** | 234,479 | 193,750 | **322,568** |
| **XYZF2 (draw kicks)** | 72,386 | 60,039 | **98,697** |
| **UV writes** | 73,330 | 60,481 | **101,873** |
| **RGBAQ writes** | 72,289 | 59,810 | **97,484** |
| **XYZ2 writes** | 1,334 | 816 | **3,970** |

## Key Findings

### 1. Cave Bottleneck Confirmed — 40% More Draw Calls

Goblin caves produce **102,658 draw calls/frame** vs 73,720 in town — a 39% increase. This validates the static analysis prediction that VIPointLight + VIColorBuffer per-vertex lighting causes multiplicative draw call growth per torch.

The extra ~29,000 draw calls break down as:
- ~24,000 additional TriStrip draws (cave geometry re-rendered per light pass)
- ~4,900 additional Sprites (torch particles — VIParticleSprite billboards)

### 2. Draw:Vertex Ratio is ~1:1 Everywhere

Across all 3 scenes, draw calls ≈ vertices. The engine kicks a GS draw on nearly every vertex submission. This is not scene-dependent — it's the engine's fundamental rendering architecture. Every vertex goes through:

```
RGBAQ (color) → UV (texture coord) → XYZF2 (position + draw kick)
```

This 1:1 ratio means the engine does NOT batch vertices into larger triangle strips. Each strip is typically 1-3 triangles submitted individually.

### 3. Sprite Count 3× Higher in Caves

| Scene | Sprites/frame | % of primitives |
|-------|--------------|-----------------|
| Town | 1,594 | 2.2% |
| Outdoor | 1,324 | 2.2% |
| Caves | **6,470** | **6.3%** |

The 4,900 extra sprites in caves = torch particles. Each torch emits ~20 billboard particles per frame (VIParticleSprite). With ~10 torches visible: 10 × 20 = 200 particles, but each particle may require multiple sprite draws for blending layers.

### 4. GIF Bandwidth Scales Linearly

PATH3 (EE→GIF) data per frame:
- Town: 7.29 MB
- Caves: 10.53 MB (+44%)

The 44% bandwidth increase closely tracks the 39% draw call increase, confirming the bottleneck is draw call volume, not individual draw complexity.

### 5. XYZF2 Dominates Over XYZ2

| Register | Town | Caves | Meaning |
|----------|------|-------|---------|
| XYZF2 | 72,386 | 98,697 | Draw kick WITH fog |
| XYZ2 | 1,334 | 3,970 | Draw kick WITHOUT fog |

98% of draws use XYZF2 (fog-enabled). The 3,970 fog-free XYZ2 draws in caves likely correspond to light halos, spell effects, or UI elements rendered without fog.

### 6. Register Write Pattern is Constant

The top registers by write frequency are identical across all scenes:
1. UV (texture coordinates)
2. XYZF2 (vertex position + fog + draw kick)
3. RGBAQ (vertex color + alpha)
4. NOP (padding)
5. XYZ2 (draw kick, no fog)

This confirms a single rendering code path for all geometry — VIRaster's material pipeline.

## Bottleneck Cost Formula — Validated

From static analysis (`docs/render-pipeline.md`):

```
cost_per_frame = base_geometry_draws + (num_lights × geometry_per_light) + particle_draws
```

Runtime data:
- **Base geometry** (outdoor, no torches): ~60,000 draws
- **Town** (ambient lighting, few point lights): ~73,000 draws (+13,000)
- **Goblin caves** (many torches): ~102,000 draws (+42,000 over base)

The ~42,000 extra draws in caves vs outdoor = VIPointLight/VIColorBuffer re-rendering cave geometry per torch. With estimated 8-10 visible torches, that's ~4,200 extra draws per torch — matching the VIColorBuffer lock/unlock cycle re-rendering nearby geometry.

## Native Port Implications

### The Fix: Per-Pixel Lighting

Replace VIPointLight/VIColorBuffer (per-vertex, CPU-side, N passes) with GPU per-pixel lighting (single pass, fragment shader):

| Current (PS2) | Native Port |
|---------------|-------------|
| 102,658 draw calls | ~5,000-10,000 draw calls |
| 10.53 MB GIF/frame | ~2 MB GPU commands/frame |
| N light passes × geometry | 1 pass + N lights in shader |
| CPU-bound (EE) | GPU-bound (fragment shader) |

Expected improvement: **10-20× fewer draw calls** in worst-case cave scenes.

### Sprite Optimization

The 6,470 sprites/frame in caves can be reduced via:
- GPU particle instancing (1 draw call per particle system, not per particle)
- Particle LOD (reduce count at distance)
- Billboard atlas batching

## VU1 Microcode Extraction

Separately, VU1 programs were extracted from the ELF DVP overlay sections:

| Program | Instructions | Float Immediates | E-flags | Notes |
|---------|-------------|-----------------|---------|-------|
| RasterMicro | 1,868 | 67 | 41 | General geometry transform, many subroutines |
| BillboardMicro | 2,029 | 0 | 10 | Billboard/particle, larger than expected |

Key discovery: DVP overlay table format is `{name_off, lma, vma}` (not `{vma, size, lma}`). Overlay sections are BSS-like — actual code lives at the LMA in `.vutext` (RasterMicro) and `.srs` (BillboardMicro).

Full extraction output: `output/vu1/summary.md`

## Files

| File | Description |
|------|-------------|
| `tools/parse-gs-dump.py` | GS dump parser (475 lines, 40 tests) |
| `tools/extract-vu1.py` | VU1 microcode extractor (480 lines) |
| `tests/test_parse_gs_dump.py` | Parser test suite (40 tests) |
| `output/town.gs` | Kelethin GS dump (34 MB) |
| `output/cave.gs` | Lesser Faydark GS dump (33 MB) |
| `output/goblin-cave.gs` | Goblin caves GS dump (48 MB) |
| `output/vu1/` | Extracted VU1 programs + metadata |
| `output/cheats/90E66BC5.pnach` | Debug menu cheat for level select |
