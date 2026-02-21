#!/usr/bin/env python3
"""Map Snowblind Engine architecture from ELF symbol table.

Parses readelf -sW output to extract C++ class hierarchy, subsystem mapping,
and engine architecture. Uses C++ name mangling conventions to identify
class::method relationships.

Usage:
    readelf -sW bin/SLUS_205.65 | python3 tools/map_engine.py
    python3 tools/map_engine.py --input /tmp/readelf_output.txt
"""

import argparse
import re
import sys
import json
from collections import defaultdict
from pathlib import Path


def parse_readelf_line(line: str) -> dict | None:
    """Parse a readelf -sW symbol table line."""
    parts = line.split()
    if len(parts) < 8:
        return None
    try:
        return {
            "addr": int(parts[1], 16),
            "size": int(parts[2]),
            "type": parts[3],
            "bind": parts[4],
            "vis": parts[5],
            "section": parts[6],
            "name": parts[7] if len(parts) == 8 else " ".join(parts[7:]),
        }
    except (ValueError, IndexError):
        return None


def demangle_old_style(name: str) -> tuple[str | None, str]:
    """Extract class name from old-style C++ mangling (GNU 2.x / cfront).

    Patterns:
      method__ClassArgs       -> (Class, method)
      method__FArgs           -> (None, method)  [free function]
      __ClassArgs             -> (Class, ctor)
      _$_ClassArgs            -> (Class, dtor)
      __tf7ClassName          -> (ClassName, typeinfo)
    """
    # Typeinfo: __tf<len><ClassName>
    m = re.match(r'__tf(\d+)(\w+)', name)
    if m:
        length = int(m.group(1))
        cls = m.group(2)[:length]
        return cls, "__typeinfo"

    # Destructor: _$_<len><ClassName>
    m = re.match(r'_\$_(\d+)(\w+)', name)
    if m:
        length = int(m.group(1))
        rest = m.group(2)
        if length <= len(rest):
            cls = rest[:length]
            return cls, "~destructor"
        # fall through if malformed

    # Constructor: __<len><ClassName><Args>
    m = re.match(r'^__(\d+)(\w+)', name)
    if m:
        length = int(m.group(1))
        rest = m.group(2)
        if length <= len(rest):
            cls = rest[:length]
            return cls, "constructor"
        # fall through if malformed

    # Method: method__<len><ClassName><Args>
    m = re.match(r'^(\w+?)__(\d+)(\w+)', name)
    if m:
        method = m.group(1)
        length = int(m.group(2))
        rest = m.group(3)
        if length <= len(rest):
            cls = rest[:length]
            return cls, method

    # Method on nested class: method__Q2<len1><Class1><len2><Class2>
    m = re.match(r'^(\w+?)__Q(\d)(\w+)', name)
    if m:
        method = m.group(1)
        nesting = int(m.group(2))
        rest = m.group(3)
        # Parse nested class names
        classes = []
        pos = 0
        for _ in range(nesting):
            lm = re.match(r'(\d+)', rest[pos:])
            if not lm:
                classes = []  # malformed — discard partial result
                break
            clen = int(lm.group(1))
            pos += len(lm.group(1))
            if pos + clen > len(rest):
                classes = []  # length overrun — discard
                break
            classes.append(rest[pos:pos+clen])
            pos += clen
        if classes:
            return "::".join(classes), method

    # Method on template class: method__t<len><ClassName><TemplateArgs>
    m = re.match(r'^(\w+?)__t(\d+)(\w+)', name)
    if m:
        method = m.group(1)
        length = int(m.group(2))
        rest = m.group(3)
        if length <= len(rest):
            cls = rest[:length]
            return cls, method

    # Template constructor: __t<len><ClassName><TemplateArgs>
    m = re.match(r'^__t(\d+)(\w+)', name)
    if m:
        length = int(m.group(1))
        rest = m.group(2)
        if length <= len(rest):
            cls = rest[:length]
            return cls, "constructor"

    # Free function: method__F<Args>
    m = re.match(r'^(\w+?)__F', name)
    if m:
        return None, m.group(1)

    # Global init/dtor
    if name.startswith("_GLOBAL_"):
        return None, name

    return None, name


def _kw(word: str, text: str) -> bool:
    """Word-boundary keyword match to avoid false positives."""
    return bool(re.search(rf'(?:^|[^a-z]){word}', text, re.IGNORECASE))


def classify_subsystem(cls: str | None, method: str, name: str) -> str:
    """Classify a function into an engine subsystem."""
    n = name.lower()
    c = (cls or "").lower()
    m = method.lower()

    # Engine core (VI prefix)
    if c.startswith("vi"):
        if c in ("viraster",):
            return "Renderer"
        if c in ("vihsprite",):
            return "Sprites"
        if c in ("virfont",):
            return "Font"
        if c in ("viscene",):
            return "Scene"
        if c in ("viworld",):
            return "World"
        if c in ("vizone",):
            return "Zone"
        if c in ("viobjfile", "viloader"):
            return "Asset Loading"
        if c in ("vifile",):
            return "File I/O"
        if c in ("vistring",):
            return "String Utils"
        if c in ("viui", "viwnd", "viwndedit"):
            return "UI"
        if c in ("vicollide",):
            return "Collision"
        if c in ("viwave",):
            return "Audio"
        if c in ("visetup",):
            return "Setup/Config"
        if c.startswith("vicamera") or c == "vicamera":
            return "Camera"
        if c.startswith("vicolor") or c.startswith("vilight"):
            return "Lighting"
        return f"Engine ({cls})"

    # Camera
    if c == "camera" or "camera" in n:
        return "Camera"

    # Rendering
    if any(x in n for x in ("render", "blit", "raster")) or _kw("draw", name):
        return "Renderer"
    if any(x in n for x in ("particle", "lightning", "fractal")) or _kw("trail", name):
        return "Particles"
    if "illumin" in n or _kw("light", name) or _kw("shadow", name):
        return "Lighting"

    # DMA/GIF/VIF pipeline
    if any(x in n for x in ("dma", "gif", "vif", "dmatag", "giftag")):
        return "DMA/GIF Pipeline"

    # Scripting
    if n.startswith("amx") or "amx" in c:
        return "AMX Scripting"

    # Network
    if any(x in n for x in ("packet", "socket", "tcp", "udp", "netinit",
                              "realm", "lobby", "server", "client")):
        return "Networking"

    # Audio
    if any(x in n for x in ("sound", "audio", "music", "sfx", "wave")):
        return "Audio"

    # Physics
    if any(x in n for x in ("collis", "physic", "steer", "vehicle")):
        return "Physics"
    if c == "vehicle":
        return "Physics"

    # Entity/Game — monsters, NPCs, items, props
    if c in ("creature", "orc", "goblin", "skeleton", "mummy", "soul",
             "player", "npc", "item", "base", "critter",
             "woodelfsoldier", "cyclops", "spiderqueen", "antqueen",
             "blackwidow", "vampirelord", "demon", "ghoul", "scorpion",
             "wraith", "cloudgiant", "innoruuk", "superorc",
             "mummyking", "undeadknight", "undeadknightclone",
             "froglock", "seamonster", "arenabeast", "ant", "lavamonster",
             "cthulu", "nightmare", "firebeetle", "firefly", "mermaid",
             "gnome", "gnomenavigator", "maledarkelfelfsoldier",
             "maledarkelf", "femaledarkelfsoldier", "femaledarkelf",
             "cat", "shooter", "rondo"):
        return "Game Entities"

    # Skills (Skill* classes)
    if c.startswith("skill"):
        return "Skills"

    # Spells (Spell* classes, not VISpell which is engine)
    if c.startswith("spell") and not c.startswith("vispell"):
        return "Spells"

    # Game objects/props
    if c in ("gameobject", "container", "chest", "autochest", "autochestlp",
             "savepoint", "doorswing", "doorsecret", "lever", "floorswitch",
             "trigger", "pushtrigger", "generator", "jumpgate", "teleporter",
             "autoprop", "autoproplp", "autopropphysics", "cosmeticprop",
             "cosmeticpropanim", "userparamprop", "pushphysicsprop",
             "particleprop", "weaponrack", "boat", "skulboat", "wheel",
             "clock", "candle", "candle2", "gold", "fire", "loosefire",
             "trap", "missiletrap", "webtrap"):
        return "Game Props"

    # Projectiles/effects
    if c in ("missileweapon", "animatedmissile", "playerprojectile",
             "beetleprojectile", "shockprojectile", "coldarrowprojectile",
             "hateprojectile", "holybolt", "diseasebolt",
             "iceball", "lavabomb", "waterSpout", "web",
             "sparks", "gutchunk", "flyingtext", "dustcloud"):
        return "Projectiles"

    # Sony SDK
    if n.startswith("sce") or n.startswith("_sce"):
        return "Sony SDK"

    # C++ stdlib
    if c in ("istream", "ostream", "streambuf", "filebuf", "ios",
             "string", "basic_string"):
        return "C++ Stdlib"
    if n.startswith("__") and not n.startswith("__Q"):
        return "C++ Runtime"

    # Math
    if any(x in n for x in ("matrix", "vector", "quat", "point3", "vect")):
        return "Math"

    return "Other"


def main():
    parser = argparse.ArgumentParser(description="Map Snowblind Engine structure from ELF symbol table")
    parser.add_argument("--input", type=str, help="Path to readelf -sW output file (default: read from stdin)")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of formatted report")
    parser.add_argument("--title", type=str, default="Champions of Norrath (SLUS-20565)",
                        help="Game title for report header")
    args = parser.parse_args()

    # Read from stdin or file
    if args.input:
        lines = Path(args.input).read_text().splitlines()
    else:
        lines = sys.stdin.readlines()

    # Parse symbols
    functions = []
    for line in lines:
        sym = parse_readelf_line(line.strip())
        if sym and sym["type"] == "FUNC" and sym["size"] > 0:
            functions.append(sym)

    # Extract classes and methods
    classes = defaultdict(list)
    free_functions = []
    subsystems = defaultdict(list)

    for func in functions:
        cls, method = demangle_old_style(func["name"])
        subsystem = classify_subsystem(cls, method, func["name"])

        entry = {
            "name": func["name"],
            "addr": func["addr"],
            "size": func["size"],
            "class": cls,
            "method": method,
            "subsystem": subsystem,
        }

        if cls:
            classes[cls].append(entry)
        else:
            free_functions.append(entry)

        subsystems[subsystem].append(entry)

    if args.json:
        output = {
            "total_functions": len(functions),
            "total_classes": len(classes),
            "classes": {
                cls: {
                    "method_count": len(methods),
                    "total_size": sum(m["size"] for m in methods),
                    "subsystem": methods[0]["subsystem"] if methods else "Unknown",
                    "methods": [{"name": m["method"], "addr": hex(m["addr"]), "size": m["size"]} for m in methods],
                }
                for cls, methods in sorted(classes.items(), key=lambda x: -len(x[1]))
            },
            "subsystems": {
                sub: {
                    "function_count": len(funcs),
                    "total_size": sum(f["size"] for f in funcs),
                }
                for sub, funcs in sorted(subsystems.items(), key=lambda x: -sum(f["size"] for f in x[1]))
            },
        }
        print(json.dumps(output, indent=2))
    else:
        # Pretty report
        print("=" * 70)
        print(f"  SNOWBLIND ENGINE STRUCTURE MAP")
        print(f"  {args.title}")
        print(f"  {len(functions)} functions, {len(classes)} classes")
        print("=" * 70)

        print(f"\n{'SUBSYSTEM':<25} {'FUNCS':>6} {'SIZE (KB)':>10}")
        print("-" * 45)
        for sub, funcs in sorted(subsystems.items(), key=lambda x: -sum(f["size"] for f in x[1])):
            total_size = sum(f["size"] for f in funcs)
            print(f"  {sub:<23} {len(funcs):>6} {total_size/1024:>9.1f}")

        print(f"\n\n{'VI* ENGINE CLASSES':}")
        print("-" * 70)
        print(f"  {'Class':<20} {'Methods':>8} {'Size (KB)':>10} {'Subsystem':<20}")
        print("  " + "-" * 66)
        for cls, methods in sorted(classes.items(), key=lambda x: -len(x[1])):
            if cls.startswith("VI") or cls.startswith("vi"):
                total_size = sum(m["size"] for m in methods)
                sub = methods[0]["subsystem"]
                print(f"  {cls:<20} {len(methods):>8} {total_size/1024:>9.1f}  {sub}")

        print(f"\n\n{'GAME ENTITY CLASSES':}")
        print("-" * 70)
        print(f"  {'Class':<20} {'Methods':>8} {'Size (KB)':>10}")
        print("  " + "-" * 42)
        for cls, methods in sorted(classes.items(), key=lambda x: -len(x[1])):
            sub = methods[0]["subsystem"]
            if sub == "Game Entities":
                total_size = sum(m["size"] for m in methods)
                print(f"  {cls:<20} {len(methods):>8} {total_size/1024:>9.1f}")

        print(f"\n\n{'TOP 30 LARGEST FUNCTIONS (performance targets)':}")
        print("-" * 70)
        print(f"  {'Function':<50} {'Size':>6} {'Addr':>10}")
        print("  " + "-" * 66)
        for func in sorted(functions, key=lambda x: -x["size"])[:30]:
            name = func["name"][:48]
            print(f"  {name:<50} {func['size']:>5}  {hex(func['addr'])}")


if __name__ == "__main__":
    main()
