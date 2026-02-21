"""Ghidra Jython script: batch-decompile all functions from engine-map.json.

Run via analyzeHeadless:
  analyzeHeadless.bat <project_dir> <project_name> ^
    -process "*" -noanalysis ^
    -postScript ghidra-batch-decompile.py ^
    -scriptPath <this_dir> ^
    -scriptlog decompile.log

Or from the Ghidra Script Manager (Window > Script Manager > Run).

Output: one .c file per function in OUTPUT_DIR, plus a combined all_decompiled.txt.
"""

import os
import json

# ==== CONFIGURATION ====
# Adjust these paths for your system
OUTPUT_DIR = r"C:\ghidra\output\decompiled"
ENGINE_MAP = r"C:\ghidra\scripts\engine-map.json"

# Set to a subsystem name to only decompile that subsystem, or None for all
FILTER_SUBSYSTEM = None  # e.g., "Renderer", "Scene", "Lighting", None = all

# Timeout per function in seconds (large functions like VIScene::Render need more)
TIMEOUT_SECONDS = 120
# =======================

from ghidra.app.decompiler import DecompInterface, DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor

def load_targets(engine_map_path, subsystem_filter=None):
    """Load function targets from engine-map.json."""
    targets = []
    with open(engine_map_path, "r") as f:
        data = json.load(f)

    # classes is a dict: {"ClassName": {"subsystem": ..., "methods": [...]}}
    classes = data.get("classes", {})
    for class_name, cls_data in classes.items():
        subsystem = cls_data.get("subsystem", "unknown")
        if subsystem_filter and subsystem != subsystem_filter:
            continue
        for method in cls_data.get("methods", []):
            addr = method.get("addr", method.get("address"))
            name = method.get("name", "unknown")
            size = method.get("size", 0)
            if addr and size > 0:
                # address is hex string like "0x0113bb48" or int
                if isinstance(addr, (str, unicode)):
                    addr_int = int(addr, 16)
                else:
                    addr_int = int(addr)
                qualified = "{}::{}".format(class_name, name)
                targets.append((addr_int, qualified, size, subsystem))

    targets.sort(key=lambda x: x[0])
    return targets


def safe_filename(name):
    """Convert function name to safe filename."""
    return name.replace("::", "__").replace("<", "_").replace(">", "_").replace(" ", "_")


def main():
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    # Load targets
    if os.path.exists(ENGINE_MAP):
        targets = load_targets(ENGINE_MAP, FILTER_SUBSYSTEM)
        print("Loaded {} targets from engine-map.json".format(len(targets)))
    else:
        print("ERROR: engine-map.json not found at {}".format(ENGINE_MAP))
        print("Falling back to manual address list")
        # Fallback: paste addresses here manually
        targets = [
            # (address, "Class::Method", size, "subsystem"),
        ]

    if not targets:
        print("No targets to decompile!")
        return

    # Set up decompiler
    ifc = DecompInterface()
    opts = DecompileOptions()
    ifc.setOptions(opts)
    ifc.openProgram(currentProgram)
    monitor = ConsoleTaskMonitor()

    succeeded = 0
    failed = 0
    skipped = 0

    # Combined output file
    combined_path = os.path.join(OUTPUT_DIR, "all_decompiled.txt")
    combined = open(combined_path, "w")
    combined.write("// Batch decompilation of {}\n".format(currentProgram.getName()))
    combined.write("// Total targets: {}\n\n".format(len(targets)))

    for addr_int, name, size, subsystem in targets:
        addr = toAddr(addr_int)

        # Try exact match first, then containing
        func = getFunctionAt(addr)
        if func is None:
            func = getFunctionContaining(addr)
        if func is None:
            print("SKIP: no function at 0x{:08x} ({})".format(addr_int, name))
            skipped += 1
            continue

        # Decompile
        result = ifc.decompileFunction(func, TIMEOUT_SECONDS, monitor)
        if not result.decompileCompleted():
            print("FAIL: 0x{:08x} {} - {}".format(addr_int, name, result.getErrorMessage()))
            failed += 1
            continue

        c_code = result.getDecompiledFunction().getC()
        if not c_code:
            print("FAIL: 0x{:08x} {} - empty output".format(addr_int, name))
            failed += 1
            continue

        # Write individual file
        fname = safe_filename(name)
        out_path = os.path.join(OUTPUT_DIR, "0x{:08x}_{}.c".format(addr_int, fname))
        with open(out_path, "w") as f:
            f.write("// Function: {}\n".format(name))
            f.write("// Address:  0x{:08x}\n".format(addr_int))
            f.write("// Size:     {} bytes\n".format(size))
            f.write("// Subsystem: {}\n\n".format(subsystem))
            f.write(c_code)

        # Write to combined file
        combined.write("=" * 80 + "\n")
        combined.write("// {} @ 0x{:08x} ({} bytes) [{}]\n".format(name, addr_int, size, subsystem))
        combined.write("=" * 80 + "\n\n")
        combined.write(c_code)
        combined.write("\n\n")

        succeeded += 1
        if succeeded % 100 == 0:
            print("Progress: {}/{} done...".format(succeeded, len(targets)))

    combined.close()
    ifc.closeProgram()

    print("\n" + "=" * 60)
    print("BATCH DECOMPILATION COMPLETE")
    print("  Succeeded: {}".format(succeeded))
    print("  Failed:    {}".format(failed))
    print("  Skipped:   {}".format(skipped))
    print("  Total:     {}".format(len(targets)))
    print("  Output:    {}".format(OUTPUT_DIR))
    print("  Combined:  {}".format(combined_path))
    print("=" * 60)


main()
