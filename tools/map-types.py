#!/usr/bin/env python3
"""Map Demon Stone (Cl*) struct layouts to Champions of Norrath (VI*) classes.

Uses:
- docs/demon-stone-types.json: 1,211 structs with byte offsets + member names
- docs/engine-map.json: 660 VI* classes with method lists
- output/decompiled/*.c: 6,447 decompiled functions (offset usage patterns)

Outputs:
- output/type-mapping.json: cross-referenced type map
- output/snowblind-types.h: Ghidra-importable C header with struct definitions
"""

import json
import os
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).parent.parent

# ─── Class name mapping (Demon Stone Cl* → CoN VI*) ───
# From docs/demon-stone-source-map.md table + manual analysis
CL_TO_VI = {
    # Rendering
    "ClGfx": "VIRaster",
    "ClGfxDmaBuffer": "VIRaster",  # DMA subsystem within VIRaster
    "ClTexEnv": "VIRaster",        # Texture env is part of raster state
    "ClShaderPass": "VIRaster",    # Shader passes feed into raster
    "ClShaderSystem": "VIRaster",
    "ClPbi": "VIRaster",           # Packed buffer interface
    "ClRegList": "VIRaster",       # GS register lists
    "ClDraw2D": "VIRaster",        # 2D drawing

    # World / spatial
    "ClWorld": "VIZone",
    "ClWorldNode": "VIZone",
    "ClWorldDrawDataPs2": "VIZone",
    "ClWorldCollisionNode": "VIZone",
    "ClWorldCollisionDataPs2": "VIZone",
    "ClPortalDrawManager": "VIZone",
    "ClSector": "VIZone",
    "ClNodeObjectList": "VIZone",

    # Terrain / streaming
    "ClWorldStreamingManager": "VIWorld",
    "ClWorldWater": "VIWorld",
    "ClWorldPlant": "VIWorld",
    "ClWorldBillboard": "VIWorld",
    "ClGrass": "VIWorld",
    "ClLava": "VIWorld",

    # Lighting
    "ClDynamicLightManager": "VIColorBuffer",
    "ClDynamicLightRendererPS2": "VIPointLight",
    "ClEngineLight": "VIPointLight",
    "ClLightGlow": "VIPointLight",

    # Particles
    "ClPfxSystem": "VIParticleSystem",
    "ClPfxPattern": "VIParticleDefinition",
    "ClPfxMachinePs2": "VIParticleSystem",
    "ClBillboardParticleRendererPs2": "VIParticleSprite",
    "ClTrailParticleRendererPs2": "VIParticleSystem",
    "ClFirePatternRendererPs2": "VIParticleSystem",

    # Skeletal animation (Noam = VIHSprite/VICSprite)
    "ClNoamActor": "VIHSprite",
    "ClNoamSkeleton": "VIHSprite",
    "ClNoamFigure": "VIHSprite",
    "ClNoamFigurePs2": "VIHSprite",
    "ClNoamPs2UcodeInterface": "VIHSprite",
    "ClAnimBin": "VIHSprite",
    "ClAnimStream": "VIHSprite",
    "ClMixer": "VIHSprite",
    "ClMorpher": "VIHSprite",
    "ClActor": "VIHSprite",
    "ClActorData": "VIHSprite",

    # Audio
    "ClAudio": "VISoundDevice",
    "ClAudioData": "VISoundDevice",
    "ClAudioPs2": "VISoundDevice",

    # Collision
    "ClCollisionAttrib": "VICollide",
    "ClCollisionManager": "VICollide",
    "ClBoundingInfo": "VICollide",
    "ClCollisionMaterial": "VICollide",
    "ClCollisionTriangle": "VICollide",

    # UI
    "ClMenu": "VIWnd",
    "ClShell": "VIWnd",
    "ClFont": "VIWnd",
    "ClFontType": "VIWnd",
    "ClObx": "VIWnd",
    "ClControlPs2": "VIWnd",

    # Scripting
    "ClScript": "AMXPawn",
    "ClScriptLink": "AMXPawn",
    "ClScriptObj": "AMXPawn",

    # Asset loading
    "ClWad": "VILoader",

    # Weather / atmosphere
    "ClRain": "VIAtmosphere",
    "ClWind": "VIAtmosphere",
    "ClCloud": "VIAtmosphere",
    "ClSkyBoxPS2": "VIAtmosphere",

    # Scene
    "ClEngine": "VIScene",
    "ClEnginePS2": "VIScene",

    # Camera
    "ClCamera": "VICamera",

    # Game entities (direct mapping for game layer)
    "ClCharacterObj": "Creature",
    "ClPlayerObj": "Player",
    "ClPropObj": "VIProp",
    "ClAttributeObj": "VIAttributeObj",
    "ClObject": "VIObject",

    # Physics
    "ClRigidBody": "VIPhysics",
    "ClSimulationBase": "VISimulation",
    "ClSimulationManager": "VISimulation",

    # Math types (these map to engine math types)
    "ClMatrix": "VIMatrix44",
    "ClVector3d": "VIVect3",
    "ClVector4d": "VIVect4",
    "ClQuaternion": "VIQuat",
    "ClFrustum": "VIFrustum",

    # DMA
    "ClDmaBuffer": "VIDMABuffer",
    "ClScratchpadDMA": "VIScratchpad",
    "ClVif0DmaBuffer": "VIVif0DMA",

    # Memory
    "ClMemory": "VIMemory",

    # Display / viewport
    "ClDisplayPs2": "VIDisplay",
    "ClViewport": "VIViewport",
    "ClFader": "VIFader",

    # Decals / effects
    "ClDecal": "VIDecal",
    "ClCloth": "VICloth",

    # VU microcode
    "ClUcodeInterface": "VIVUMicro",
    "ClVU0Manager": "VIVU0",
    "ClVU1Manager": "VIVU1",

    # GS hardware
    "ClGfxManager": "VIGfxManager",
    "ClGSDisplayList": "VIGSDisplayList",

    # Input
    "ClDevicePs2GamePad": "VIPad",
    "ClDeviceMgrPS2": "VIDeviceMgr",
    "ClRumbleManager": "VIRumble",

    # Save/load
    "ClSaveLoad": "VISaveLoad",
    "ClSaveDevicePs2": "VISaveDevice",

    # PS2 hardware
    "ClIop": "VIIOP",
    "ClPerfCounters": "VIPerfCounters",

    # Service system
    "ClServiceManager": "VIServiceManager",
}

# Reverse mapping for lookup
VI_TO_CL = defaultdict(list)
for cl, vi in CL_TO_VI.items():
    VI_TO_CL[vi].append(cl)


def load_demon_stone_types():
    """Load Demon Stone struct definitions."""
    path = ROOT / "docs" / "demon-stone-types.json"
    with open(path) as f:
        data = json.load(f)
    # Index by name
    by_name = {}
    for s in data["structs"]:
        by_name[s["name"]] = s
    return by_name


def load_engine_map():
    """Load CoN engine class/method map."""
    path = ROOT / "docs" / "engine-map.json"
    with open(path) as f:
        return json.load(f)


def scan_offsets_in_decompiled(class_name, decompiled_dir):
    """Scan decompiled .c files for a class and extract offset accesses.

    Returns dict: {offset_hex: count} of all offsets accessed on `this` pointer.
    """
    offsets = defaultdict(int)
    pattern = re.compile(
        r'\*\s*\([^)]*\)\s*\(\w+\s*\+\s*(0x[0-9a-fA-F]+)\)'
        r'|'
        r'\w+\s*\+\s*(0x[0-9a-fA-F]+)'
    )

    # Find files matching this class
    safe_name = class_name.replace("::", "__")
    for fname in os.listdir(decompiled_dir):
        if not fname.endswith(".c"):
            continue
        # Match files belonging to this class
        # Format: 0x{addr}_{ClassName__Method}.c
        parts = fname.split("_", 1)
        if len(parts) < 2:
            continue
        func_part = parts[1].rsplit(".c", 1)[0]
        # Check if this function belongs to the class
        if not func_part.startswith(safe_name + "__"):
            continue

        filepath = os.path.join(decompiled_dir, fname)
        with open(filepath, "r") as f:
            content = f.read()

        # Find all offset accesses (param_1 + 0x...)
        # These represent struct member accesses on `this`
        for match in pattern.finditer(content):
            offset = match.group(1) or match.group(2)
            if offset:
                offsets[int(offset, 16)] += 1

    return dict(offsets)


def build_type_mapping(ds_types, engine_map):
    """Build the cross-referenced type mapping."""
    mapping = {}
    classes = engine_map.get("classes", {})

    for vi_class, cl_names in VI_TO_CL.items():
        # Get CoN class info
        con_info = classes.get(vi_class, {})
        method_count = len(con_info.get("methods", []))

        # Collect all Demon Stone struct layouts for this mapping
        cl_structs = []
        for cl_name in cl_names:
            if cl_name in ds_types:
                s = ds_types[cl_name]
                cl_structs.append({
                    "cl_name": cl_name,
                    "byte_size": s["byte_size"],
                    "member_count": len(s["members"]),
                    "members": [
                        {
                            "name": m["name"],
                            "type": m["type"],
                            "offset": m["offset"],
                            **({"bit_size": m["bit_size"]} if "bit_size" in m else {}),
                            **({"bit_offset": m["bit_offset"]} if "bit_offset" in m else {}),
                        }
                        for m in s["members"]
                    ],
                    "base_classes": s.get("base_classes", []),
                })

        if not cl_structs:
            continue

        # Scan decompiled code for offset usage
        decompiled_dir = ROOT / "output" / "decompiled"
        offset_usage = {}
        if decompiled_dir.exists():
            offset_usage = scan_offsets_in_decompiled(vi_class, decompiled_dir)

        mapping[vi_class] = {
            "con_class": vi_class,
            "con_subsystem": con_info.get("subsystem", "unknown"),
            "con_method_count": method_count,
            "demon_stone_sources": cl_structs,
            "offset_usage_in_decompiled": {
                f"0x{k:04x}": v for k, v in sorted(offset_usage.items())
            } if offset_usage else {},
        }

    return mapping


def generate_c_header(mapping, ds_types):
    """Generate a Ghidra-importable C header with struct definitions."""
    lines = [
        "/* Snowblind Engine struct definitions",
        " * Auto-generated from Demon Stone DWARF1 debug info",
        " * Maps Demon Stone (Cl*) → Champions of Norrath (VI*)",
        " *",
        " * Import into Ghidra: File → Parse C Source",
        " */",
        "",
        "#ifndef SNOWBLIND_TYPES_H",
        "#define SNOWBLIND_TYPES_H",
        "",
        "#include <stdint.h>",
        "",
        "/* Forward declarations */",
    ]

    # Collect all struct names for forward declarations
    all_names = set()
    for vi_class, info in sorted(mapping.items()):
        all_names.add(vi_class)
        for cl in info["demon_stone_sources"]:
            all_names.add(cl["cl_name"])

    for name in sorted(all_names):
        lines.append(f"typedef struct {name} {name};")

    lines.extend(["", "/* ═══ Type Definitions ═══ */", ""])

    # C type mapping for DWARF types
    type_map = {
        "float": "float",
        "double": "double",
        "int": "int32_t",
        "signed int": "int32_t",
        "unsigned int": "uint32_t",
        "short": "int16_t",
        "signed short": "int16_t",
        "unsigned short": "uint16_t",
        "char": "int8_t",
        "signed char": "int8_t",
        "unsigned char": "uint8_t",
        "long": "int32_t",
        "unsigned long": "uint32_t",
        "long long": "int64_t",
        "unsigned long long": "uint64_t",
        "bool": "uint8_t",
        "void": "void",
    }

    def translate_type(dwarf_type):
        """Convert DWARF type string to C type."""
        if not dwarf_type:
            return "uint32_t"
        # Handle pointers
        if dwarf_type.endswith("*"):
            base = dwarf_type[:-1].strip()
            return translate_type(base) + "*"
        # Handle const
        if dwarf_type.startswith("const "):
            return "const " + translate_type(dwarf_type[6:])
        # Direct mapping
        if dwarf_type in type_map:
            return type_map[dwarf_type]
        # Pointer to forward-declared type
        if dwarf_type.startswith("Cl") or dwarf_type.startswith("VI"):
            return dwarf_type
        # Unknown/opaque reference types (ft_0x..., type@0x...)
        if dwarf_type.startswith("ft_") or dwarf_type.startswith("type@"):
            return "uint32_t"  # opaque, use uint32_t placeholder
        # Array types, function pointers, etc
        return "uint32_t"  # safe fallback

    for vi_class, info in sorted(mapping.items()):
        # Use the primary (largest) Demon Stone struct
        primary = max(info["demon_stone_sources"], key=lambda s: s["member_count"])

        lines.append(f"/* {vi_class} ← {primary['cl_name']}")
        lines.append(f" * Size: {primary['byte_size']} bytes, {primary['member_count']} members")
        if info["con_method_count"]:
            lines.append(f" * CoN methods: {info['con_method_count']}")
        lines.append(" */")
        lines.append(f"struct {vi_class} {{")

        prev_offset = 0
        for i, m in enumerate(primary["members"]):
            offset = m["offset"]
            c_type = translate_type(m["type"])
            name = m["name"]

            # Add padding if there's a gap
            if offset > prev_offset and i > 0:
                gap = offset - prev_offset
                if gap > 0 and gap <= 1024:  # reasonable gap
                    pass  # let compiler handle alignment

            # Handle bitfields
            if "bit_size" in m:
                lines.append(f"    {c_type} {name} : {m['bit_size']};  /* +0x{offset:04x} */")
            else:
                lines.append(f"    {c_type} {name};  /* +0x{offset:04x} */")

            # Estimate size for padding calc
            if c_type.endswith("*"):
                prev_offset = offset + 4
            elif c_type == "float" or c_type in ("int32_t", "uint32_t"):
                prev_offset = offset + 4
            elif c_type in ("int16_t", "uint16_t"):
                prev_offset = offset + 2
            elif c_type in ("int8_t", "uint8_t"):
                prev_offset = offset + 1
            elif c_type == "double" or c_type in ("int64_t", "uint64_t"):
                prev_offset = offset + 8
            else:
                prev_offset = offset + 4

        lines.append(f"}};  /* total: {primary['byte_size']} bytes */")
        lines.append("")

    lines.append("#endif /* SNOWBLIND_TYPES_H */")
    return "\n".join(lines)


def cross_reference_offsets(mapping):
    """Cross-reference decompiled offset accesses against known struct members.

    For each VI* class, finds which decompiled offsets match named Demon Stone
    members and which are unknown (need manual RE).
    """
    results = {}

    for vi_class, info in mapping.items():
        # Build offset → member name lookup from all Demon Stone sources
        known_offsets = {}
        for src in info["demon_stone_sources"]:
            for m in src["members"]:
                offset = m["offset"]
                # If multiple sources define the same offset, keep both names
                if offset in known_offsets:
                    existing = known_offsets[offset]
                    if m["name"] != existing["name"]:
                        known_offsets[offset] = {
                            "name": f"{existing['name']} / {m['name']}",
                            "type": existing["type"],
                            "source": f"{existing['source']} + {src['cl_name']}",
                        }
                else:
                    known_offsets[offset] = {
                        "name": m["name"],
                        "type": m["type"],
                        "source": src["cl_name"],
                    }

        # Match against decompiled offsets
        matched = {}
        unmatched = {}
        for offset_hex, count in info.get("offset_usage_in_decompiled", {}).items():
            offset_int = int(offset_hex, 16)
            if offset_int in known_offsets:
                km = known_offsets[offset_int]
                matched[offset_hex] = {
                    "name": km["name"],
                    "type": km["type"],
                    "source": km["source"],
                    "ref_count": count,
                }
            else:
                unmatched[offset_hex] = {"ref_count": count}

        results[vi_class] = {
            "matched": matched,
            "unmatched": unmatched,
            "match_rate": len(matched) / max(len(matched) + len(unmatched), 1),
        }

    return results


def generate_ghidra_script(mapping, xref):
    """Generate a Ghidra Jython script that applies struct types to functions.

    This script can be run in Ghidra to rename variables and annotate
    offset accesses with struct member names.
    """
    lines = [
        '"""Ghidra Jython script: apply Snowblind Engine type annotations.',
        "",
        "Auto-generated by tools/map-types.py from Demon Stone DWARF1 debug info.",
        "Run in Ghidra Script Manager to annotate decompiled functions.",
        '"""',
        "",
        "from ghidra.program.model.data import StructureDataType, CategoryPath",
        "from ghidra.program.model.data import PointerDataType, IntegerDataType",
        "from ghidra.program.model.data import FloatDataType, CharDataType",
        "from ghidra.program.model.data import UnsignedIntegerDataType",
        "from ghidra.program.model.data import ShortDataType, UnsignedShortDataType",
        "from ghidra.program.model.data import ByteDataType, UnsignedCharDataType",
        "",
        "dtm = currentProgram.getDataTypeManager()",
        'cat = CategoryPath("/SnowblindEngine")',
        "",
        "# --- Struct definitions from Demon Stone DWARF1 ---",
        "",
    ]

    type_map_ghidra = {
        "float": "FloatDataType.dataType",
        "double": "FloatDataType.dataType",  # close enough for Ghidra
        "int": "IntegerDataType.dataType",
        "signed int": "IntegerDataType.dataType",
        "unsigned int": "UnsignedIntegerDataType.dataType",
        "short": "ShortDataType.dataType",
        "signed short": "ShortDataType.dataType",
        "unsigned short": "UnsignedShortDataType.dataType",
        "char": "CharDataType.dataType",
        "signed char": "CharDataType.dataType",
        "unsigned char": "UnsignedCharDataType.dataType",
        "bool": "UnsignedCharDataType.dataType",
        "long": "IntegerDataType.dataType",
        "unsigned long": "UnsignedIntegerDataType.dataType",
    }

    for vi_class, info in sorted(mapping.items()):
        primary = max(info["demon_stone_sources"], key=lambda s: s["member_count"])
        if not primary["members"]:
            continue

        lines.append(f'# {vi_class} <- {primary["cl_name"]}')
        lines.append(f's = StructureDataType(cat, "{vi_class}", {primary["byte_size"]})')

        for m in primary["members"]:
            ghidra_type = type_map_ghidra.get(m["type"])
            if not ghidra_type:
                if m["type"].endswith("*"):
                    ghidra_type = "PointerDataType.dataType"
                else:
                    ghidra_type = "IntegerDataType.dataType"

            if "bit_size" not in m:
                lines.append(
                    f's.replaceAtOffset({m["offset"]}, {ghidra_type}, '
                    f'-1, "{m["name"]}", "")'
                )

        lines.append(f'dtm.addDataType(s, None)')
        lines.append("")

    lines.append('print("Applied {} struct types to Ghidra project".format(')
    lines.append(f'    {len(mapping)}))')

    return "\n".join(lines)


def print_summary(mapping, xref=None):
    """Print a summary of the mapping results."""
    total_members = 0
    total_offsets = 0
    total_matched = 0
    total_unmatched = 0

    print("=" * 70)
    print("Cl* → VI* TYPE MAPPING SUMMARY")
    print("=" * 70)
    print()

    for vi_class, info in sorted(mapping.items()):
        members = sum(s["member_count"] for s in info["demon_stone_sources"])
        offsets = len(info["offset_usage_in_decompiled"])
        total_members += members
        total_offsets += offsets

        src_names = ", ".join(s["cl_name"] for s in info["demon_stone_sources"])
        print(f"  {vi_class:30s} ← {src_names}")

        if xref and vi_class in xref:
            xr = xref[vi_class]
            matched = len(xr["matched"])
            unmatched = len(xr["unmatched"])
            total_matched += matched
            total_unmatched += unmatched
            rate = xr["match_rate"] * 100
            print(f"    {members:4d} named members | offsets: {matched} matched, {unmatched} unknown ({rate:.0f}% coverage)")
        else:
            print(f"    {members:4d} named members, {offsets:4d} offset refs in decompiled code")

    print()
    print(f"Total: {len(mapping)} VI* classes mapped")
    print(f"       {total_members} named struct members from Demon Stone")
    print(f"       {total_offsets} offset references found in decompiled code")
    if xref:
        overall_rate = total_matched / max(total_matched + total_unmatched, 1) * 100
        print(f"       {total_matched} offsets matched to named members ({overall_rate:.0f}%)")
        print(f"       {total_unmatched} offsets still unknown")


def main():
    print("Loading Demon Stone struct definitions...")
    ds_types = load_demon_stone_types()
    print(f"  {len(ds_types)} structs loaded")

    print("Loading CoN engine map...")
    engine_map = load_engine_map()
    print(f"  {len(engine_map['classes'])} classes loaded")

    print("Building type mapping (scanning decompiled code)...")
    mapping = build_type_mapping(ds_types, engine_map)

    print("Cross-referencing offsets against struct members...")
    xref = cross_reference_offsets(mapping)

    print_summary(mapping, xref)

    # Write JSON output (includes cross-reference)
    out_json = ROOT / "output" / "type-mapping.json"
    combined = {}
    for vi_class, info in mapping.items():
        combined[vi_class] = {**info}
        if vi_class in xref:
            combined[vi_class]["cross_reference"] = xref[vi_class]
    with open(out_json, "w") as f:
        json.dump(combined, f, indent=2)
    print(f"\nJSON mapping:   {out_json}")

    # Write C header
    out_h = ROOT / "output" / "snowblind-types.h"
    header = generate_c_header(mapping, ds_types)
    with open(out_h, "w") as f:
        f.write(header)
    print(f"C header:       {out_h}")

    # Write Ghidra import script
    out_ghidra = ROOT / "tools" / "ghidra-apply-types.py"
    ghidra_script = generate_ghidra_script(mapping, xref)
    with open(out_ghidra, "w") as f:
        f.write(ghidra_script)
    print(f"Ghidra script:  {out_ghidra}")

    # Write offset cross-reference report
    out_xref = ROOT / "output" / "offset-xref.md"
    with open(out_xref, "w") as f:
        f.write("# Offset Cross-Reference: Decompiled Code vs Struct Members\n\n")
        f.write("For each VI* class, shows which `this + 0xNNN` offset accesses in the\n")
        f.write("decompiled code match known Demon Stone struct members.\n\n")

        for vi_class, xr in sorted(xref.items()):
            if not xr["matched"] and not xr["unmatched"]:
                continue
            rate = xr["match_rate"] * 100
            f.write(f"## {vi_class} ({rate:.0f}% coverage)\n\n")

            if xr["matched"]:
                f.write("### Matched offsets\n\n")
                f.write("| Offset | Member | Type | Source | Refs |\n")
                f.write("|--------|--------|------|--------|------|\n")
                for off, m in sorted(xr["matched"].items(), key=lambda x: int(x[0], 16)):
                    f.write(f"| `{off}` | `{m['name']}` | `{m['type']}` | {m['source']} | {m['ref_count']} |\n")
                f.write("\n")

            if xr["unmatched"]:
                f.write("### Unknown offsets (need manual RE)\n\n")
                f.write("| Offset | Refs |\n")
                f.write("|--------|------|\n")
                for off, m in sorted(xr["unmatched"].items(), key=lambda x: int(x[0], 16)):
                    f.write(f"| `{off}` | {m['ref_count']} |\n")
                f.write("\n")

    print(f"Offset xref:    {out_xref}")

    # Stats
    h_lines = header.count("\n")
    print(f"\nC header: {h_lines} lines")
    print(f"Ghidra script: {ghidra_script.count(chr(10))} lines")

    # Stats
    h_lines = header.count("\n")
    print(f"  ({h_lines} lines)")


if __name__ == "__main__":
    main()
