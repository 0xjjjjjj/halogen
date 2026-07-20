#!/usr/bin/env python3
"""Post-recompilation patches for output/champions-of-norrath/*.cpp.

Run after PS2Recomp regenerates the C++ output.  Applies game-specific
workarounds for guest-code bugs that only manifest in the headless
runtime (where texture assets may be missing or return garbage).
"""

import re
import sys
from pathlib import Path

OUT_DIR = Path(__file__).parent.parent / "output" / "champions-of-norrath"


def patch_texture_smooth_border() -> bool:
    """textureSmoothBorder infinite loop guard.

    The function reads a texture-header field as loop-increment `s2`.
    When the texture is missing/garbage the field reads 0, and the
    resulting `while(counter<limit) counter+=0` loops forever.
    Patch: skip the whole function's rendering if s2 <= 0.
    """
    f = OUT_DIR / "textureSmoothBorder__FiiiiiUiiii_0x16efd8.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = "SET_GPR_S32(ctx, 18, (int16_t)READ16(ADD32(GPR_U32(ctx, 3), 0)));"
    if marker not in src:
        print(f"[patch] {f.name}: marker not found, skipping", file=sys.stderr)
        return False
    guard = (marker + "\n"
             "    if (GPR_S32(ctx, 18) <= 0) {\n"
             "        static bool warnedZero = false;\n"
             '        if (!warnedZero) { std::cerr << "[tsB] EARLY RETURN: s2 tile-height <= 0 (bad texture header)\\n"; warnedZero = true; }\n'
             "        goto label_16f5b8;\n"
             "    }")
    if guard in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(marker, guard, 1)
    if "#include <iostream>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <iostream>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied s2<=0 early-return guard")
    return True


def patch_start_new_world() -> bool:
    """startNewWorld: log gameLoadWorld arg + HALOGEN_FORCE_LEVEL override.

    Lets us see which level string the game passes to gameLoadWorld
    (typically 'intro' -> 'kelsel'), and lets a runtime env var
    (HALOGEN_FORCE_LEVEL) replace it with any level name to jump
    past the front-end menu flow.
    """
    f = OUT_DIR / "startNewWorld__Fv_0x2cd1e0.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = ('    ctx->pc = 0x1CBC48u;\n'
              '    {\n'
              '        const uint32_t __entryPc = ctx->pc;\n'
              '        gameLoadWorld__FPc_0x1cbc48(rdram, ctx, runtime);')
    if marker not in src:
        print(f"[patch] {f.name}: marker not found", file=sys.stderr)
        return False
    replacement = (
        '    ctx->pc = 0x1CBC48u;\n'
        '    {\n'
        '        uint32_t nameAddr = GPR_U32(ctx, 4);\n'
        '        const char *cstr = reinterpret_cast<const char*>(getConstMemPtr(rdram, nameAddr));\n'
        '        std::cerr << "[startNewWorld] gameLoadWorld arg name=\\""\n'
        '                  << (cstr ? cstr : "<NULL>") << "\\" addr=0x" << std::hex << nameAddr << std::dec << std::endl;\n'
        '        if (const char *forced = std::getenv("HALOGEN_FORCE_LEVEL"); forced && forced[0] && cstr) {\n'
        '            char *mut = const_cast<char*>(cstr);\n'
        '            std::strncpy(mut, forced, 15); mut[15] = 0;\n'
        '            std::cerr << "[startNewWorld] FORCE level name -> \\"" << mut << "\\"" << std::endl;\n'
        '        }\n'
        '        const uint32_t __entryPc = ctx->pc;\n'
        '        gameLoadWorld__FPc_0x1cbc48(rdram, ctx, runtime);')
    if replacement in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(marker, replacement, 1)
    if "#include <cstring>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <cstring>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied gameLoadWorld arg probe + HALOGEN_FORCE_LEVEL override")
    return True


def main() -> int:
    ok = True
    ok &= patch_texture_smooth_border()
    ok &= patch_start_new_world()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
