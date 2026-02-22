# -*- coding: utf-8 -*-
"""Ghidra Jython script: retype function parameters using struct definitions.

For each function in engine-map.json, sets param_1 (this) to the correct
struct pointer type from the /SnowblindEngine category. This makes the
decompiler output show named struct fields instead of raw offsets.

Run AFTER ghidra-apply-types.py has been applied.

Usage:
  analyzeHeadless.bat <project_dir> <project_name> ^
    -process "*" -noanalysis ^
    -postScript ghidra-retype-params.py ^
    -scriptPath <this_dir>
"""

import os
import json

# ==== CONFIGURATION ====
ENGINE_MAP = r"C:\ghidra\scripts\engine-map.json"
# =======================

from ghidra.program.model.data import CategoryPath, PointerDataType
from ghidra.program.model.data import Undefined4DataType
from ghidra.program.model.symbol import SourceType
from ghidra.program.model.listing import ParameterImpl
from ghidra.app.decompiler import DecompInterface, DecompileOptions
from ghidra.util.task import ConsoleTaskMonitor

def get_struct_type(dtm, name):
    """Look up a struct in /SnowblindEngine category."""
    cat = dtm.getCategory(CategoryPath("/SnowblindEngine"))
    if cat is None:
        return None
    dt = cat.getDataType(name)
    return dt

# Mapping from engine-map class names to struct names in Ghidra DTM
# Must match what ghidra-apply-types.py created
CLASS_TO_STRUCT = {
    "VIRaster": "VIRaster",
    "VIScene": "VIScene",
    "VIZone": "VIZone",
    "VIHSprite": "VIHSprite",
    "VICSprite": "VIHSprite",
    "VIColorBuffer": "VICollide",  # no direct struct, skip
    "VIPointLight": "VIPointLight",
    "VIParticleSystem": "VIParticleSystem",
    "VIParticleDefinition": "VIParticleDefinition",
    "VIParticleDefinitionEx": "VIParticleDefinition",
    "VISoundDevice": "VISoundDevice",
    "VIWorld": "VIWorld",
    "VIWnd": "VIWnd",
    "VIAtmosphere": "VIAtmosphere",
    "VICamera": "VICamera",
    "VILoader": "VILoader",
    "Player": "Player",
    "Creature": "Creature",
    "VIFrustum": "VIFrustum",
    "VIFader": "VIFader",
    "VICollide": "VICollide",
    "VIPad": "VIPad",
    "VIMatrix44": "VIMatrix44",
}


def load_targets(engine_map_path):
    """Load function targets grouped by class."""
    with open(engine_map_path, "r") as f:
        data = json.load(f)

    targets = []
    classes = data.get("classes", {})
    for class_name, cls_data in classes.items():
        struct_name = CLASS_TO_STRUCT.get(class_name)
        if not struct_name:
            continue
        for method in cls_data.get("methods", []):
            addr = method.get("addr", method.get("address"))
            name = method.get("name", "unknown")
            size = method.get("size", 0)
            if addr and size > 0:
                if isinstance(addr, (str, unicode)):
                    addr_int = int(addr, 16)
                else:
                    addr_int = int(addr)
                targets.append((addr_int, class_name, struct_name, name))

    return targets


def main():
    dtm = currentProgram.getDataTypeManager()
    listing = currentProgram.getListing()

    if not os.path.exists(ENGINE_MAP):
        print("ERROR: engine-map.json not found at {}".format(ENGINE_MAP))
        return

    targets = load_targets(ENGINE_MAP)
    print("Loaded {} targets for retyping".format(len(targets)))

    # Cache struct pointer types
    struct_cache = {}
    retyped = 0
    skipped = 0
    failed = 0

    skip_no_func = 0
    skip_no_struct = 0
    skip_no_params = 0
    warned = set()

    # Debug: check if category exists
    cat = dtm.getCategory(CategoryPath("/SnowblindEngine"))
    if cat is None:
        print("ERROR: /SnowblindEngine category not found in Data Type Manager!")
        print("Run ghidra-apply-types.py first.")
        return
    else:
        print("Found /SnowblindEngine category with {} types".format(
            len(cat.getDataTypes())))

    # Use decompiler to discover actual param count, then retype
    ifc = DecompInterface()
    opts = DecompileOptions()
    ifc.setOptions(opts)
    ifc.openProgram(currentProgram)
    monitor = ConsoleTaskMonitor()

    for addr_int, class_name, struct_name, method_name in targets:
        addr = toAddr(addr_int)
        func = getFunctionAt(addr)
        if func is None:
            func = getFunctionContaining(addr)
        if func is None:
            skip_no_func += 1
            continue

        # Get or create the pointer type
        if struct_name not in struct_cache:
            st = get_struct_type(dtm, struct_name)
            if st is None:
                struct_cache[struct_name] = None
                if struct_name not in warned:
                    print("WARN: struct '{}' not found in DTM".format(struct_name))
                    warned.add(struct_name)
            else:
                struct_cache[struct_name] = PointerDataType(st)

        ptr_type = struct_cache.get(struct_name)
        if ptr_type is None:
            skip_no_struct += 1
            continue

        # Check if function already has params
        params = func.getParameters()
        if len(params) > 0:
            # Has params - just retype first one
            try:
                param0 = params[0]
                param0.setDataType(ptr_type, SourceType.USER_DEFINED)
                param0.setName("this", SourceType.USER_DEFINED)
                retyped += 1
            except Exception as e:
                failed += 1
                if failed <= 3:
                    print("FAIL retype: {} - {}".format(func.getName(), str(e)))
        else:
            # No params - use decompiler to discover them, then commit with our type
            try:
                result = ifc.decompileFunction(func, 30, monitor)
                if result is not None and result.decompileCompleted():
                    hfunc = result.getHighFunction()
                    if hfunc is not None:
                        proto = hfunc.getFunctionPrototype()
                        num_params = proto.getNumParams()
                        if num_params > 0:
                            # Build param list with first param retyped
                            new_params = []
                            this_param = ParameterImpl(
                                "this", ptr_type, currentProgram)
                            new_params.append(this_param)
                            # Keep remaining params as-is
                            for i in range(1, num_params):
                                p = proto.getParam(i)
                                pdt = p.getDataType()
                                pname = "param_{}".format(i + 1)
                                new_params.append(
                                    ParameterImpl(pname, pdt, currentProgram))
                            from ghidra.program.model.listing import Function
                            func.replaceParameters(
                                new_params,
                                Function.FunctionUpdateType.DYNAMIC_STORAGE_ALL_PARAMS,
                                True,
                                SourceType.USER_DEFINED)
                            retyped += 1
                        else:
                            skip_no_params += 1
                    else:
                        skip_no_params += 1
                else:
                    skip_no_params += 1
            except Exception as e:
                failed += 1
                if failed <= 3:
                    print("FAIL decomp: {} - {}".format(func.getName(), str(e)))

        if retyped % 100 == 0 and retyped > 0:
            print("Progress: {}/{} retyped...".format(retyped, len(targets)))

    ifc.closeProgram()

    print("")
    print("=" * 60)
    print("PARAMETER RETYPING COMPLETE")
    print("  Retyped:         {}".format(retyped))
    print("  Skip (no func):  {}".format(skip_no_func))
    print("  Skip (no struct):{}".format(skip_no_struct))
    print("  Skip (no params):{}".format(skip_no_params))
    print("  Failed:          {}".format(failed))
    print("  Total:           {}".format(len(targets)))
    print("=" * 60)


main()
