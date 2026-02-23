#!/usr/bin/env python3
"""Rename recomp .cpp files whose names exceed MAX_PATH threshold to address-only names.

PS2Recomp generates files named after Metrowerks-mangled ELF symbols, which can be 200+
chars. On Windows, prefix + filename > 260 causes cl.exe to fail. We rename to just the
hex address suffix (e.g., _0x1032b30.cpp -> 0x1032b30.cpp) when the name is too long.

Usage: python3 tools/fix-long-filenames.py [--max-len N] [dir]
"""
import os
import re
import sys
import argparse

DEFAULT_DIR = "output/champions-of-norrath"
DEFAULT_MAX = 200  # chars; with a short prefix this keeps total under MAX_PATH


def fix_dir(directory: str, max_len: int, dry_run: bool) -> None:
    renamed = 0
    skipped = 0
    for name in os.listdir(directory):
        if not name.endswith(".cpp"):
            continue
        if len(name) <= max_len:
            skipped += 1
            continue
        # Extract the hex address suffix: _0xABCDEF.cpp
        m = re.search(r'(_0x[0-9a-f]+\.cpp)$', name, re.IGNORECASE)
        if not m:
            print(f"  SKIP (no address): {name[:80]}...")
            continue
        new_name = m.group(1).lstrip('_')  # e.g. 0x1032b30.cpp
        old_path = os.path.join(directory, name)
        new_path = os.path.join(directory, new_name)
        if os.path.exists(new_path):
            print(f"  CONFLICT: {new_name} already exists, skipping")
            continue
        print(f"  {len(name):3d} -> {len(new_name):3d}: {name[:60]}...{m.group(1)}")
        if not dry_run:
            os.rename(old_path, new_path)
        renamed += 1

    print(f"\nDone: {renamed} renamed, {skipped} within limit (kept as-is)")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("dir", nargs="?", default=DEFAULT_DIR, help="recomp output dir")
    parser.add_argument("--max-len", type=int, default=DEFAULT_MAX)
    parser.add_argument("--dry-run", action="store_true", help="show what would be renamed")
    args = parser.parse_args()

    directory = os.path.abspath(args.dir)
    if not os.path.isdir(directory):
        print(f"Error: {directory} is not a directory")
        sys.exit(1)

    print(f"Checking {directory} for filenames > {args.max_len} chars...")
    if args.dry_run:
        print("(DRY RUN)")
    fix_dir(directory, args.max_len, args.dry_run)


if __name__ == "__main__":
    main()
