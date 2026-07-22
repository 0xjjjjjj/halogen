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


def patch_create_random_noop() -> bool:
    """createRandom no-op: return zero-filled item, skip the RNG loop entirely.

    createRandom (0x104440) is the random-loot generator called from
    shopStart to populate merchant inventories.  When the item-description
    table is bogus (which happens because upstream lumpFind returns garbage
    for missing assets), the inner loop_104cf8 spins forever probing item
    tables that never satisfy its threshold check.  An existing force-break
    escapes the loop at 100k iters and continues execution with garbage on
    the stack, which downstream shop/item code chokes on later.

    Not core rendering.  Full no-op is safer than partial escape: zero the
    return-value struct at *$a0 (32 bytes covers item layout) then jump
    straight to the epilogue.
    """
    f = OUT_DIR / "createRandom__4itemPQ24item11descriptioniiii_0x104440.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = ("    WRITE64(ADD32(GPR_U32(ctx, 29), 792), GPR_U64(ctx, 31));\n"
              "    // 0x104478: 0xafa40250")
    if marker not in src:
        print(f"[patch] {f.name}: marker not found", file=sys.stderr)
        return False
    inject = (
        "    WRITE64(ADD32(GPR_U32(ctx, 29), 792), GPR_U64(ctx, 31));\n"
        "    {\n"
        "        static bool warnedCR = false;\n"
        "        if (!warnedCR) { std::cerr << \"[createRandom] NO-OP: returning zero-item (shop inventory disabled)\\n\"; warnedCR = true; }\n"
        "        uint32_t retAddr = GPR_U32(ctx, 4);\n"
        "        for (uint32_t off = 0; off < 32; off += 4) { WRITE32(ADD32(retAddr, off), 0); }\n"
        "        goto label_10548c;\n"
        "    }\n"
        "    // 0x104478: 0xafa40250")
    if inject in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(marker, inject, 1)
    if "#include <iostream>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <iostream>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied no-op stub (zero-item + jump to epilogue)")
    return True


def patch_lump_find_trace() -> bool:
    """lumpFind (0x166580) trace: log every asset lookup + return.

    lumpFind (name, archive) is the asset loader.  We hypothesize it returns
    bogus non-null pointers for missing assets, which is why downstream
    consumers (textureSmoothBorder, createRandom, others) loop forever on
    zeroed fields.  Instrument entry (log requested name + archive ptr) and
    exit (log return value in $v0) so we can see the actual call pattern.

    Args at entry:
      $a0 = archive pointer (guest addr)
      $a1 = name c-string (guest addr)
    Return in $v0.
    """
    f = OUT_DIR / "lumpFind__FPvPc_0x166580.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = "    ctx->pc = 0x166580u;\n\n    // 0x166580: 0x27bdffc0"
    if marker not in src:
        print(f"[patch] {f.name}: entry marker not found", file=sys.stderr)
        return False
    inject_entry = (
        "    ctx->pc = 0x166580u;\n"
        "    {\n"
        "        static uint32_t __lfCount = 0; ++__lfCount;\n"
        "        if (__lfCount <= 500 || (__lfCount % 500) == 0) {\n"
        "            uint32_t archiveAddr = GPR_U32(ctx, 4);\n"
        "            uint32_t nameAddr = GPR_U32(ctx, 5);\n"
        "            const char *nm = reinterpret_cast<const char*>(getConstMemPtr(rdram, nameAddr));\n"
        "            std::cerr << \"[lumpFind#\" << __lfCount << \"] archive=0x\" << std::hex << archiveAddr\n"
        "                      << \" name=0x\" << nameAddr << std::dec\n"
        "                      << \" str=\\\"\" << (nm ? nm : \"<NULL>\") << \"\\\"\" << std::endl;\n"
        "        }\n"
        "    }\n\n"
        "    // 0x166580: 0x27bdffc0")
    if inject_entry in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(marker, inject_entry, 1)
    if "#include <iostream>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <iostream>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied entry-trace")
    return True


def patch_lump_load_trace() -> bool:
    """lumpLoad (0x165b30) trace: log every archive load + return.

    lumpLoad(name) is the outer archive loader — loads a .LMP file into
    memory.  lumpFind then searches within.  Instrument entry+exit to
    see what archives the world load asks for and what pointer comes back
    (or if it returns NULL / fails).
    """
    f = OUT_DIR / "lumpLoad__FPc_0x165b30.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = "    ctx->pc = 0x165b30u;\n\n    // 0x165b30: 0x3c02006d"
    if marker not in src:
        print(f"[patch] {f.name}: entry marker not found", file=sys.stderr)
        return False
    inject_entry = (
        "    ctx->pc = 0x165b30u;\n"
        "    {\n"
        "        static uint32_t __llCount = 0; ++__llCount;\n"
        "        uint32_t nameAddr = GPR_U32(ctx, 4);\n"
        "        uint32_t retAddr = GPR_U32(ctx, 31);\n"
        "        const char *nm = reinterpret_cast<const char*>(getConstMemPtr(rdram, nameAddr));\n"
        "        std::cerr << \"[lumpLoad#\" << __llCount << \"] name=\\\"\" << (nm ? nm : \"<NULL>\")\n"
        "                  << \"\\\" ra=0x\" << std::hex << retAddr << std::dec << std::endl;\n"
        "    }\n\n"
        "    // 0x165b30: 0x3c02006d")
    if inject_entry in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(marker, inject_entry, 1)
    if "#include <iostream>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <iostream>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied entry-trace")
    return True


def patch_mca_busy_return_zero() -> bool:
    """MCA_Busy (0x25c700) force-return 0 (not busy).

    The game's frontend menu polls MCA_Busy every event-loop iteration and
    refuses to advance to the memory-card prompt / new-game menu until it
    returns 0.  Our runtime never clears gp_f2e8 (the queued-command flag)
    because we don't emulate the MC async completion callback path.  Force
    MCA_Busy to always return 0 so the frontend advances.
    """
    f = OUT_DIR / "MCA_Busy__Fv_0x25c700.cpp"
    if not f.exists():
        print(f"[patch] MISSING {f.name}", file=sys.stderr)
        return False
    src = f.read_text()
    marker = "    ctx->pc = 0x25c700u;\n\n    { static int busyCalls = 0;"
    alt_marker = "    ctx->pc = 0x25c700u;\n\n    // 0x25c700: 0x8f84f2e8"
    use_marker = marker if marker in src else (alt_marker if alt_marker in src else None)
    if use_marker is None:
        print(f"[patch] {f.name}: no marker match", file=sys.stderr)
        return False
    inject = ("    ctx->pc = 0x25c700u;\n"
              "    { static bool warnedMcaBusy = false;\n"
              "      if (!warnedMcaBusy) { std::cerr << \"[MCA_Busy] FORCE 0 (patched)\\n\"; warnedMcaBusy = true; }\n"
              "      SET_GPR_S32(ctx, 2, 0);\n"
              "      ctx->pc = GPR_U32(ctx, 31);\n"
              "      return;\n"
              "    }\n\n"
              + (use_marker.split("ctx->pc = 0x25c700u;\n\n", 1)[1]))
    if inject in src:
        print(f"[patch] {f.name}: already patched")
        return True
    src2 = src.replace(use_marker, inject, 1)
    if "#include <iostream>" not in src2:
        src2 = src2.replace('#include "ps2_stubs.h"',
                            '#include "ps2_stubs.h"\n#include <iostream>', 1)
    f.write_text(src2)
    print(f"[patch] {f.name}: applied force-return-0 stub")
    return True


def main() -> int:
    ok = True
    ok &= patch_texture_smooth_border()
    ok &= patch_start_new_world()
    ok &= patch_create_random_noop()
    ok &= patch_lump_find_trace()
    ok &= patch_lump_load_trace()
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
