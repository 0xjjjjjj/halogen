#!/usr/bin/env python3
"""Parse PCSX2 GameIndex.yaml for Snowblind Engine game entries.

Downloads the GameIndex from PCSX2's GitHub repo and extracts entries
for all known Snowblind Engine games. Outputs structured data about
game fixes, GS hardware fixes, and compatibility info.

Usage:
    python tools/pcsx2_hacks.py                    # Show all Snowblind games
    python tools/pcsx2_hacks.py --serial SLUS-20565  # Show specific game
    python tools/pcsx2_hacks.py --json              # JSON output
    python tools/pcsx2_hacks.py --common            # Show shared engine patterns
"""

import argparse
import json
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("PyYAML required: pip install pyyaml", file=sys.stderr)
    sys.exit(1)

GAMEINDEX_URL = "https://raw.githubusercontent.com/PCSX2/pcsx2/master/bin/resources/GameIndex.yaml"
CACHE_PATH = Path.home() / ".cache" / "halogen" / "GameIndex.yaml"

# All known Snowblind Engine game serials (NTSC-U)
SNOWBLIND_SERIALS = {
    "SLUS-20035": "Baldur's Gate: Dark Alliance",
    "SLUS-20470": "EverQuest Online Adventures",
    "SLUS-20565": "Champions of Norrath",
    "SLUS-20675": "Baldur's Gate: Dark Alliance II",
    "SLUS-20744": "EverQuest Online Adventures: Frontiers",
    "SLUS-20973": "Champions: Return to Arms",
    "SLUS-21304": "Justice League Heroes",
    # PAL versions
    "SLES-50672": "Baldur's Gate: Dark Alliance (PAL)",
    "SLES-52187": "Champions of Norrath (PAL)",
    "SLES-52325": "Baldur's Gate: Dark Alliance II (PAL)",
    "SLES-53039": "Champions: Return to Arms (PAL)",
    "SLES-54423": "Justice League Heroes (PAL)",
}


def download_gameindex() -> Path:
    """Download GameIndex.yaml if not cached."""
    if CACHE_PATH.exists():
        return CACHE_PATH

    import urllib.request
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    print(f"Downloading GameIndex.yaml...", file=sys.stderr)
    urllib.request.urlretrieve(GAMEINDEX_URL, CACHE_PATH)
    return CACHE_PATH


def load_gameindex(path: Path) -> dict:
    """Load and parse the GameIndex.yaml."""
    with open(path) as f:
        return yaml.safe_load(f)


def extract_snowblind_entries(gameindex: dict) -> dict:
    """Extract all Snowblind Engine game entries."""
    entries = {}
    for serial, name in SNOWBLIND_SERIALS.items():
        if serial in gameindex:
            entry = gameindex[serial]
            entry["_serial"] = serial
            entry["_snowblind_name"] = name
            entries[serial] = entry
    return entries


def find_common_fixes(entries: dict) -> dict:
    """Find GS hardware fixes shared across all Snowblind games."""
    all_gs_fixes = []
    for entry in entries.values():
        gs = entry.get("gsHWFixes", {})
        if gs:
            all_gs_fixes.append(set(gs.keys()))

    if not all_gs_fixes:
        return {}

    common = all_gs_fixes[0]
    for fixes in all_gs_fixes[1:]:
        common &= fixes

    return {k: "shared across all Snowblind games" for k in sorted(common)}


def print_entry(serial: str, entry: dict):
    """Pretty-print a game entry."""
    name = entry.get("name", entry.get("_snowblind_name", "Unknown"))
    print(f"\n{'='*60}")
    print(f"  {name}")
    print(f"  Serial: {serial}  |  Region: {entry.get('region', '?')}  |  Compat: {entry.get('compat', '?')}")
    print(f"{'='*60}")

    if "gameFixes" in entry:
        print("\n  Game Fixes:")
        for fix in entry["gameFixes"]:
            print(f"    - {fix}")

    if "gsHWFixes" in entry:
        print("\n  GS Hardware Fixes:")
        for fix, val in entry["gsHWFixes"].items():
            print(f"    {fix}: {val}")

    if "clampModes" in entry:
        print("\n  Clamp Modes:")
        for mode, val in entry["clampModes"].items():
            print(f"    {mode}: {val}")

    if "speedHacks" in entry:
        print("\n  Speed Hacks:")
        for hack, val in entry["speedHacks"].items():
            print(f"    {hack}: {val}")

    if "memcardFilters" in entry:
        print("\n  Memory Card Filters:")
        for f in entry["memcardFilters"]:
            print(f"    - {f}")

    if "patches" in entry:
        print("\n  Patches:")
        for crc, patch in entry["patches"].items():
            print(f"    CRC {crc}:")
            for line in patch.get("content", "").split("\n"):
                print(f"      {line}")


def main():
    parser = argparse.ArgumentParser(description="PCSX2 Snowblind Engine game analysis")
    parser.add_argument("--serial", help="Show specific game serial")
    parser.add_argument("--json", action="store_true", help="JSON output")
    parser.add_argument("--common", action="store_true", help="Show shared engine patterns")
    parser.add_argument("--cache", type=Path, default=CACHE_PATH, help="GameIndex cache path")
    args = parser.parse_args()

    path = download_gameindex() if not args.cache.exists() else args.cache
    gameindex = load_gameindex(path)
    entries = extract_snowblind_entries(gameindex)

    if args.json:
        # Clean internal keys for JSON output
        clean = {}
        for serial, entry in entries.items():
            clean[serial] = {k: v for k, v in entry.items() if not k.startswith("_")}
        print(json.dumps(clean, indent=2))
        return

    if args.common:
        common = find_common_fixes(entries)
        print("\nShared GS Hardware Fixes (all Snowblind games):")
        for fix in common:
            print(f"  - {fix}")
        return

    if args.serial:
        if args.serial in entries:
            print_entry(args.serial, entries[args.serial])
        else:
            print(f"Serial {args.serial} not found in Snowblind games")
            print(f"Known serials: {', '.join(sorted(SNOWBLIND_SERIALS.keys()))}")
        return

    # Default: show all
    print(f"Snowblind Engine Games in PCSX2 GameDatabase")
    print(f"Found {len(entries)}/{len(SNOWBLIND_SERIALS)} entries\n")

    for serial in sorted(entries.keys()):
        print_entry(serial, entries[serial])

    print(f"\n{'='*60}")
    common = find_common_fixes(entries)
    if common:
        print("\nShared GS Hardware Fixes (engine-level patterns):")
        for fix in common:
            print(f"  - {fix}")


if __name__ == "__main__":
    main()
