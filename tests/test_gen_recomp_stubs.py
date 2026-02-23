"""Tests for tools/gen-recomp-stubs.py -- generates ps2_recompiled_stubs.h.

The script reads ps2_recompiled_functions.h to get all function declarations,
scans .cpp files to identify stubs (those not including ps2_recompiled_stubs.h),
and generates a header with forward declarations for stub functions only.
"""

import importlib.util
import sys
import tempfile
import os
from pathlib import Path

import pytest

# Import the module from tools/ path
TOOLS_DIR = Path(__file__).parent.parent / "tools"
spec = importlib.util.spec_from_file_location(
    "gen_recomp_stubs", TOOLS_DIR / "gen-recomp-stubs.py"
)
gen_recomp_stubs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(gen_recomp_stubs)


# --- Fixtures ---


SAMPLE_FUNCTIONS_HEADER = """\
#ifndef PS2_RECOMPILED_FUNCTIONS_H
#define PS2_RECOMPILED_FUNCTIONS_H

#include <cstdint>

struct R5900Context;
class PS2Runtime;

void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);
void abort_0x2ff8c0(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);
void atan_0x2f7988(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);
void Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);
void Render__7VIScene_0x10d0000(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);
void malloc_0x301000(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);

#endif // PS2_RECOMPILED_FUNCTIONS_H
"""

STUB_CPP_ABORT = """\
#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"

void abort_0x2ff8c0(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    const uint32_t __entryPc = ctx->pc;
    ps2_stubs::TODO_NAMED("abort", rdram, ctx, runtime);
    if (ctx->pc == __entryPc)
    {
        ctx->pc = getRegU32(ctx, 31);
    }
}
"""

STUB_CPP_ATAN = """\
#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"

void atan_0x2f7988(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    const uint32_t __entryPc = ctx->pc;
    ps2_stubs::atan(rdram, ctx, runtime);
    if (ctx->pc == __entryPc)
    {
        ctx->pc = getRegU32(ctx, 31);
    }
}
"""

STUB_CPP_MALLOC = """\
#include "ps2_runtime.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"

void malloc_0x301000(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    const uint32_t __entryPc = ctx->pc;
    ps2_stubs::malloc(rdram, ctx, runtime);
    if (ctx->pc == __entryPc)
    {
        ctx->pc = getRegU32(ctx, 31);
    }
}
"""

DECOMPILED_CPP_START = """\
#include "ps2_runtime_macros.h"
#include "ps2_runtime.h"
#include "ps2_recompiled_functions.h"
#include "ps2_recompiled_stubs.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"

// Function: _start
// Address: 0x100008 - 0x100248
void _start_0x100008(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    ctx->pc = 0x100008u;
    // ... actual decompiled code ...
}
"""

DECOMPILED_CPP_ADD = """\
#include "ps2_runtime_macros.h"
#include "ps2_runtime.h"
#include "ps2_recompiled_functions.h"
#include "ps2_recompiled_stubs.h"

#include "ps2_syscalls.h"
#include "ps2_stubs.h"

// Function: Add__10VIMatrix33RC10VIMatrix33f
// Address: 0x108aeb0 - 0x108af30
void Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    ctx->pc = 0x108aeb0u;
    // ... actual decompiled code ...
}
"""

DECOMPILED_CPP_RENDER = """\
#include "ps2_runtime_macros.h"
#include "ps2_runtime.h"
#include "ps2_recompiled_functions.h"
#include "ps2_recompiled_stubs.h"
#include "ps2_syscalls.h"
#include "ps2_stubs.h"

// Function: Render__7VIScene
// Address: 0x10d0000 - 0x10d0100
void Render__7VIScene_0x10d0000(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime) {
    ctx->pc = 0x10d0000u;
    // ... actual decompiled code ...
}
"""


@pytest.fixture
def sample_output_dir(tmp_path):
    """Create a minimal output directory mirroring PS2Recomp structure."""
    outdir = tmp_path / "champions-of-norrath"
    outdir.mkdir()

    # Write the functions header
    (outdir / "ps2_recompiled_functions.h").write_text(SAMPLE_FUNCTIONS_HEADER)

    # Write stub .cpp files (3 stubs)
    (outdir / "abort_0x2ff8c0.cpp").write_text(STUB_CPP_ABORT)
    (outdir / "atan_0x2f7988.cpp").write_text(STUB_CPP_ATAN)
    (outdir / "malloc_0x301000.cpp").write_text(STUB_CPP_MALLOC)

    # Write decompiled .cpp files (3 decompiled)
    (outdir / "_start_0x100008.cpp").write_text(DECOMPILED_CPP_START)
    (outdir / "Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0.cpp").write_text(
        DECOMPILED_CPP_ADD
    )
    (outdir / "Render__7VIScene_0x10d0000.cpp").write_text(DECOMPILED_CPP_RENDER)

    return outdir


# --- Tests: parse_declarations ---


class TestParseDeclarations:
    """Test parsing function declarations from ps2_recompiled_functions.h."""

    def test_parses_all_declarations(self, sample_output_dir):
        """All 6 function declarations should be parsed from the header."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        assert len(decls) == 6

    def test_declaration_names_correct(self, sample_output_dir):
        """Parsed declaration names match expected function names."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        names = {d["name"] for d in decls}
        expected = {
            "_start_0x100008",
            "abort_0x2ff8c0",
            "atan_0x2f7988",
            "Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0",
            "Render__7VIScene_0x10d0000",
            "malloc_0x301000",
        }
        assert names == expected

    def test_declaration_line_preserved(self, sample_output_dir):
        """Each declaration preserves the full line text."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        by_name = {d["name"]: d for d in decls}
        expected_line = "void abort_0x2ff8c0(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);"
        assert by_name["abort_0x2ff8c0"]["line"] == expected_line

    def test_ignores_non_declaration_lines(self, tmp_path):
        """Preprocessor directives, blank lines, and non-void lines are skipped."""
        header = tmp_path / "test.h"
        header.write_text(
            "#pragma once\n"
            "#include <cstdint>\n"
            "struct R5900Context;\n"
            "class PS2Runtime;\n"
            "\n"
            "void foo_0x1000(uint8_t* rdram, R5900Context* ctx, PS2Runtime *runtime);\n"
        )
        decls = gen_recomp_stubs.parse_declarations(header)
        assert len(decls) == 1
        assert decls[0]["name"] == "foo_0x1000"

    def test_empty_header_returns_empty(self, tmp_path):
        """An empty header file returns no declarations."""
        header = tmp_path / "empty.h"
        header.write_text("#pragma once\n")
        decls = gen_recomp_stubs.parse_declarations(header)
        assert len(decls) == 0


# --- Tests: identify_stub_files ---


class TestIdentifyStubFiles:
    """Test identification of stub .cpp files."""

    def test_finds_all_stubs(self, sample_output_dir):
        """Should identify exactly the 3 stub files."""
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        assert len(stubs) == 3

    def test_stub_names_correct(self, sample_output_dir):
        """Stub function names extracted from filenames are correct."""
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}
        assert stub_names == {"abort_0x2ff8c0", "atan_0x2f7988", "malloc_0x301000"}

    def test_excludes_decompiled_files(self, sample_output_dir):
        """Decompiled files (with ps2_recompiled_stubs.h) are not in stubs."""
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}
        assert "_start_0x100008" not in stub_names
        assert "Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0" not in stub_names
        assert "Render__7VIScene_0x10d0000" not in stub_names

    def test_no_stubs_returns_empty(self, tmp_path):
        """Directory with only decompiled files returns empty list."""
        outdir = tmp_path / "no-stubs"
        outdir.mkdir()
        (outdir / "foo_0x1000.cpp").write_text(
            '#include "ps2_recompiled_stubs.h"\nvoid foo_0x1000() {}\n'
        )
        stubs = gen_recomp_stubs.identify_stub_files(outdir)
        assert len(stubs) == 0


# --- Tests: generate_header ---


class TestGenerateHeader:
    """Test header file generation."""

    def test_generates_valid_header(self, sample_output_dir):
        """Generated header has pragma once, includes, forward decls, and function decls."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)

        assert "#pragma once" in content
        assert "#include <cstdint>" in content
        assert "struct R5900Context;" in content
        assert "class PS2Runtime;" in content

    def test_contains_only_stub_declarations(self, sample_output_dir):
        """Header contains stub function declarations but not decompiled ones."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)

        # Stubs should be present
        assert "void abort_0x2ff8c0(" in content
        assert "void atan_0x2f7988(" in content
        assert "void malloc_0x301000(" in content

        # Decompiled functions should NOT be present
        assert "void _start_0x100008(" not in content
        assert "void Add__10VIMatrix33RC10VIMatrix33f_0x108aeb0(" not in content
        assert "void Render__7VIScene_0x10d0000(" not in content

    def test_declaration_count(self, sample_output_dir):
        """Exactly 3 stub declarations in generated header."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)

        # Count lines starting with 'void '
        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        assert len(void_lines) == 3

    def test_declarations_are_semicolon_terminated(self, sample_output_dir):
        """Each declaration line ends with a semicolon."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)

        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        for line in void_lines:
            assert line.endswith(";"), f"Declaration not semicolon-terminated: {line}"

    def test_empty_stubs_generates_minimal_header(self):
        """With no stubs, generates header with just boilerplate."""
        content = gen_recomp_stubs.generate_header([], set())
        assert "#pragma once" in content
        assert "struct R5900Context;" in content
        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        assert len(void_lines) == 0

    def test_declarations_sorted_by_address(self, sample_output_dir):
        """Stub declarations are sorted by hex address."""
        header_path = sample_output_dir / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(sample_output_dir)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)

        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        # Extract addresses from function names
        import re

        addrs = []
        for line in void_lines:
            m = re.search(r"_0x([0-9a-f]+)\(", line)
            assert m, f"No address in: {line}"
            addrs.append(int(m.group(1), 16))

        assert addrs == sorted(addrs), f"Declarations not sorted by address: {addrs}"


# --- Tests: end-to-end ---


class TestEndToEnd:
    """Test the full pipeline: scan directory, generate header, write file."""

    def test_full_pipeline(self, sample_output_dir):
        """Full run produces ps2_recompiled_stubs.h with correct content."""
        gen_recomp_stubs.generate_stubs_header(sample_output_dir)

        out_path = sample_output_dir / "ps2_recompiled_stubs.h"
        assert out_path.exists()

        content = out_path.read_text()
        assert "#pragma once" in content
        assert "void abort_0x2ff8c0(" in content
        assert "void atan_0x2f7988(" in content
        assert "void malloc_0x301000(" in content
        assert "void _start_0x100008(" not in content

    def test_full_pipeline_declaration_count(self, sample_output_dir):
        """Full run produces exactly 3 declarations."""
        gen_recomp_stubs.generate_stubs_header(sample_output_dir)

        content = (sample_output_dir / "ps2_recompiled_stubs.h").read_text()
        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        assert len(void_lines) == 3

    def test_idempotent(self, sample_output_dir):
        """Running twice produces identical output."""
        gen_recomp_stubs.generate_stubs_header(sample_output_dir)
        content1 = (sample_output_dir / "ps2_recompiled_stubs.h").read_text()

        gen_recomp_stubs.generate_stubs_header(sample_output_dir)
        content2 = (sample_output_dir / "ps2_recompiled_stubs.h").read_text()

        assert content1 == content2

    def test_does_not_modify_existing_files(self, sample_output_dir):
        """Running the tool does not modify any .cpp files or the functions header."""
        funcs_before = (
            sample_output_dir / "ps2_recompiled_functions.h"
        ).read_text()
        abort_before = (sample_output_dir / "abort_0x2ff8c0.cpp").read_text()

        gen_recomp_stubs.generate_stubs_header(sample_output_dir)

        funcs_after = (
            sample_output_dir / "ps2_recompiled_functions.h"
        ).read_text()
        abort_after = (sample_output_dir / "abort_0x2ff8c0.cpp").read_text()

        assert funcs_before == funcs_after
        assert abort_before == abort_after


# --- Tests: real data validation (against actual output directory) ---


REAL_OUTPUT_DIR = Path(__file__).parent.parent / "output" / "champions-of-norrath"


@pytest.mark.skipif(
    not (REAL_OUTPUT_DIR / "ps2_recompiled_functions.h").exists(),
    reason="Real PS2Recomp output not available",
)
class TestRealData:
    """Validate against actual PS2Recomp output directory."""

    def test_parses_all_real_declarations(self):
        """Should parse all ~14,598 declarations from the real header."""
        header_path = REAL_OUTPUT_DIR / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        # The header has 14,598 function declarations
        assert len(decls) >= 14000, f"Expected ~14598 declarations, got {len(decls)}"

    def test_identifies_real_stubs(self):
        """Should identify ~255 stub files from the real output."""
        stubs = gen_recomp_stubs.identify_stub_files(REAL_OUTPUT_DIR)
        assert len(stubs) == 255, f"Expected 255 stubs, got {len(stubs)}"

    def test_generates_real_header(self, tmp_path):
        """Generate the real header and validate counts."""
        # Copy the functions header to tmp to avoid writing to actual output
        header_path = REAL_OUTPUT_DIR / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        stubs = gen_recomp_stubs.identify_stub_files(REAL_OUTPUT_DIR)
        stub_names = {s["func_name"] for s in stubs}

        content = gen_recomp_stubs.generate_header(decls, stub_names)
        void_lines = [l for l in content.splitlines() if l.startswith("void ")]
        assert len(void_lines) == 255, f"Expected 255 declarations, got {len(void_lines)}"

    def test_all_stub_names_in_functions_header(self):
        """Every stub function name should exist in ps2_recompiled_functions.h."""
        header_path = REAL_OUTPUT_DIR / "ps2_recompiled_functions.h"
        decls = gen_recomp_stubs.parse_declarations(header_path)
        decl_names = {d["name"] for d in decls}

        stubs = gen_recomp_stubs.identify_stub_files(REAL_OUTPUT_DIR)
        for stub in stubs:
            assert stub["func_name"] in decl_names, (
                f"Stub function {stub['func_name']} not found in functions header"
            )

    def test_known_stubs_present(self):
        """Known stub functions (abort, malloc, etc.) should be identified."""
        stubs = gen_recomp_stubs.identify_stub_files(REAL_OUTPUT_DIR)
        stub_names = {s["func_name"] for s in stubs}
        # These are C library stubs we know exist
        assert "abort_0x2ff8c0" in stub_names
        assert "malloc_0x301000" in stub_names or any(
            "malloc" in n for n in stub_names
        )
