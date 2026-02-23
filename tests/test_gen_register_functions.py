"""Tests for tools/gen-register-functions.py -- generates registerAllFunctions() C++.

Validates:
  1. Parsing of ps2_recompiled_functions.h declarations
  2. Address extraction from _0xHEX suffixes
  3. Handling of duplicate addresses (prefer named over entry_*)
  4. C++ code generation with correct includes and registration calls
  5. Edge cases: empty input, malformed lines, non-declaration lines
"""

import importlib.util
import sys
import textwrap
from pathlib import Path

import pytest

# Import the module from tools/ path (same pattern as existing tests)
TOOLS_DIR = Path(__file__).parent.parent / "tools"
spec = importlib.util.spec_from_file_location(
    "gen_register_functions", TOOLS_DIR / "gen-register-functions.py"
)
gen_mod = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_mod)


# --- Parsing tests ---


class TestParseFunctionDeclarations:
    """Test extraction of (function_name, address) pairs from header lines."""

    def test_simple_declaration(self):
        lines = [
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n"
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1
        assert result[0] == ("_start_0x100008", 0x100008)

    def test_mangled_name(self):
        lines = [
            "void picFind__4itemPc_0x100258(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n"
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1
        assert result[0] == ("picFind__4itemPc_0x100258", 0x100258)

    def test_multiple_declarations(self):
        lines = [
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void _exit_0x100248(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void _root_0x100250(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 3
        assert result[0][1] == 0x100008
        assert result[1][1] == 0x100248
        assert result[2][1] == 0x100250

    def test_skips_preprocessor_lines(self):
        lines = [
            "#ifndef PS2_RECOMPILED_FUNCTIONS_H\n",
            "#define PS2_RECOMPILED_FUNCTIONS_H\n",
            "#include <cstdint>\n",
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "#endif // PS2_RECOMPILED_FUNCTIONS_H\n",
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1
        assert result[0] == ("_start_0x100008", 0x100008)

    def test_skips_forward_declarations(self):
        lines = [
            "struct R5900Context;\n",
            "class PS2Runtime;\n",
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1

    def test_skips_blank_lines(self):
        lines = [
            "\n",
            "  \n",
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1

    def test_empty_input(self):
        result = gen_mod.parse_declarations([])
        assert result == []

    def test_high_address(self):
        """Addresses above 0x1000000 (7+ hex digits) should parse correctly."""
        lines = [
            "void ps2___tf8_IO_FILE_0x1358b70(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n"
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1
        assert result[0][1] == 0x1358B70

    def test_entry_point_declaration(self):
        """entry_XXXX_0xADDR mid-function entry points should be parsed normally."""
        lines = [
            "void entry_1009c00_0x1009cd8(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n"
        ]
        result = gen_mod.parse_declarations(lines)
        assert len(result) == 1
        assert result[0] == ("entry_1009c00_0x1009cd8", 0x1009CD8)


# --- Deduplication tests ---


class TestDeduplication:
    """Test that duplicate addresses are resolved, preferring named functions."""

    def test_prefer_named_over_entry(self):
        """When same address has entry_* and a named function, prefer named."""
        decls = [
            ("entry_1009c00_0x1009cd8", 0x1009CD8),
            ("xmlAddChild_0x1009cd8", 0x1009CD8),
        ]
        result = gen_mod.deduplicate(decls)
        assert len(result) == 1
        assert result[0][0] == "xmlAddChild_0x1009cd8"
        assert result[0][1] == 0x1009CD8

    def test_prefer_named_over_entry_reversed_order(self):
        """Order of appearance should not matter for preference."""
        decls = [
            ("xmlAddChild_0x1009cd8", 0x1009CD8),
            ("entry_1009c00_0x1009cd8", 0x1009CD8),
        ]
        result = gen_mod.deduplicate(decls)
        assert len(result) == 1
        assert result[0][0] == "xmlAddChild_0x1009cd8"

    def test_prefer_named_over_sub(self):
        """sub_XXXX variants are also less useful than named functions."""
        decls = [
            ("entry_130c948_0x130cf60", 0x130CF60),
            ("sub_0130CF60_0x130cf60", 0x130CF60),
        ]
        result = gen_mod.deduplicate(decls)
        # Both are synthetic names; entry_ should lose, sub_ should be kept
        assert len(result) == 1
        assert result[0][0] == "sub_0130CF60_0x130cf60"

    def test_no_duplicates_pass_through(self):
        decls = [
            ("_start_0x100008", 0x100008),
            ("_exit_0x100248", 0x100248),
        ]
        result = gen_mod.deduplicate(decls)
        assert len(result) == 2

    def test_empty_input(self):
        result = gen_mod.deduplicate([])
        assert result == []

    def test_preserves_address_order(self):
        """Output should be sorted by address ascending."""
        decls = [
            ("func_b_0x200", 0x200),
            ("func_a_0x100", 0x100),
            ("func_c_0x300", 0x300),
        ]
        result = gen_mod.deduplicate(decls)
        addrs = [r[1] for r in result]
        assert addrs == [0x100, 0x200, 0x300]


# --- Code generation tests ---


class TestGenerateCpp:
    """Test C++ source code generation."""

    def test_basic_output_structure(self):
        """Generated code should have includes and registerAllFunctions."""
        decls = [("_start_0x100008", 0x100008)]
        code = gen_mod.generate_cpp(decls)
        assert '#include "register_functions.h"' in code
        assert '#include "ps2_runtime.h"' in code
        assert '#include "ps2_recompiled_functions.h"' in code
        assert "void registerAllFunctions(PS2Runtime &runtime)" in code

    def test_registration_call_format(self):
        decls = [("_start_0x100008", 0x100008)]
        code = gen_mod.generate_cpp(decls)
        assert "runtime.registerFunction(0x00100008, _start_0x100008);" in code

    def test_multiple_registrations(self):
        decls = [
            ("_start_0x100008", 0x100008),
            ("_exit_0x100248", 0x100248),
        ]
        code = gen_mod.generate_cpp(decls)
        assert "runtime.registerFunction(0x00100008, _start_0x100008);" in code
        assert "runtime.registerFunction(0x00100248, _exit_0x100248);" in code

    def test_address_format_8_hex_digits(self):
        """Addresses should be zero-padded to 8 hex digits."""
        decls = [("_start_0x100008", 0x100008)]
        code = gen_mod.generate_cpp(decls)
        assert "0x00100008" in code

    def test_large_address_format(self):
        """Addresses > 0x0FFFFFFF should still format correctly."""
        decls = [("func_0x1358b70", 0x1358B70)]
        code = gen_mod.generate_cpp(decls)
        assert "0x01358b70" in code

    def test_empty_input(self):
        """Empty declaration list should produce valid but empty function body."""
        code = gen_mod.generate_cpp([])
        assert "void registerAllFunctions(PS2Runtime &runtime)" in code
        # Should compile but do nothing -- body should have opening/closing braces
        assert "{\n}" in code or "{\n\n}" in code

    def test_function_count_comment(self):
        """Generated file should include a comment with function count."""
        decls = [
            ("_start_0x100008", 0x100008),
            ("_exit_0x100248", 0x100248),
        ]
        code = gen_mod.generate_cpp(decls)
        assert "2 functions" in code


# --- Integration test: parse + dedup + generate ---


class TestEndToEnd:
    """Test full pipeline: header lines -> C++ output."""

    def test_full_pipeline(self):
        header_lines = [
            "#ifndef PS2_RECOMPILED_FUNCTIONS_H\n",
            "#define PS2_RECOMPILED_FUNCTIONS_H\n",
            "\n",
            "#include <cstdint>\n",
            "\n",
            "struct R5900Context;\n",
            "class PS2Runtime;\n",
            "\n",
            "void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void _exit_0x100248(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void entry_1009c00_0x1009cd8(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void xmlAddChild_0x1009cd8(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "\n",
            "#endif // PS2_RECOMPILED_FUNCTIONS_H\n",
        ]

        decls = gen_mod.parse_declarations(header_lines)
        assert len(decls) == 4  # 4 void lines

        deduped = gen_mod.deduplicate(decls)
        assert len(deduped) == 3  # 3 unique addresses

        code = gen_mod.generate_cpp(deduped)
        assert "runtime.registerFunction(0x00100008, _start_0x100008);" in code
        assert "runtime.registerFunction(0x00100248, _exit_0x100248);" in code
        assert "runtime.registerFunction(0x01009cd8, xmlAddChild_0x1009cd8);" in code
        # entry_ variant should NOT be registered
        assert "entry_1009c00_0x1009cd8" not in code
        assert "3 functions" in code

    def test_pipeline_with_real_header_sample(self):
        """Test with a realistic sample matching actual file patterns."""
        header_lines = [
            "void picFind__4itemPc_0x100258(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void picInit__4itemv_0x1003c8(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void entry_130c948_0x130cf60(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
            "void sub_0130CF60_0x130cf60(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n",
        ]

        decls = gen_mod.parse_declarations(header_lines)
        deduped = gen_mod.deduplicate(decls)
        code = gen_mod.generate_cpp(deduped)

        # 3 unique addresses: 0x100258, 0x1003c8, 0x130cf60
        assert "3 functions" in code
        assert "picFind__4itemPc_0x100258" in code
        assert "picInit__4itemv_0x1003c8" in code
        assert "sub_0130CF60_0x130cf60" in code
        assert "entry_130c948_0x130cf60" not in code
