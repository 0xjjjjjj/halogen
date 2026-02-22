#!/usr/bin/env python3
"""Extract VU1 microcode programs from PS2 ELF DVP overlay sections.

Parses the .DVP.ovlytab, .DVP.ovlystrtab, and .DVP.overlay.* sections from
a PS2 ELF to extract VU1 microcode programs. The actual code lives at the
LMA (load memory address) locations in .vutext or .srs, not in the overlay
sections themselves (which are BSS-like and zeroed).

DVP overlay table format (12 bytes per entry):
    uint32_t name_off;  // Offset into .DVP.ovlystrtab
    uint32_t lma;       // Load address where code actually resides
    uint32_t vma;       // Target address in VU1 micro memory (bytes)

VU1 instruction encoding (8 bytes per instruction pair):
    bits [31:0]  = lower instruction (integer ALU / load-store / branch)
    bits [63:32] = upper instruction (FMAC floating-point)

Upper instruction flags (MSBs of upper 32 bits):
    bit 31: I flag - lower 32 bits are IEEE754 float immediate, not instruction
    bit 30: E flag - end of program (VU1 halts after executing this pair)
    bit 29: M flag - M-bit (debug marker)
    bit 28: D flag - debug breakpoint
    bit 27: T flag - debug breakpoint type 2

Usage:
    python extract-vu1.py <elf_path> [-o output_dir] [-v] [--raw-only]
"""

import argparse
import hashlib
import json
import os
import struct
import sys
from pathlib import Path

# VU1 instruction flag bits (in upper instruction word)
FLAG_I = 0x80000000  # Immediate: lower word is float, not instruction
FLAG_E = 0x40000000  # End: VU1 halts after this instruction pair
FLAG_M = 0x20000000  # M-bit debug marker
FLAG_D = 0x10000000  # Debug breakpoint
FLAG_T = 0x08000000  # Debug breakpoint type 2

VU1_MICRO_MEM_SIZE = 16384  # 16KB
VU1_INSTRUCTION_SIZE = 8     # 8 bytes per instruction pair
VU1_MAX_INSTRUCTIONS = VU1_MICRO_MEM_SIZE // VU1_INSTRUCTION_SIZE  # 2048


def read_elf32_header(f):
    """Read and validate an ELF32 header. Returns header dict."""
    f.seek(0)
    data = f.read(52)
    if len(data) < 52:
        raise ValueError("File too small to be an ELF")

    magic = data[0:4]
    if magic != b'\x7fELF':
        raise ValueError(f"Not an ELF file (magic: {magic!r})")

    ei_class = data[4]
    ei_data = data[5]
    if ei_class != 1:
        raise ValueError(f"Expected ELF32 (class=1), got class={ei_class}")
    if ei_data != 1:
        raise ValueError(f"Expected little-endian (data=1), got data={ei_data}")

    return {
        'e_type': struct.unpack('<H', data[16:18])[0],
        'e_machine': struct.unpack('<H', data[18:20])[0],
        'e_entry': struct.unpack('<I', data[24:28])[0],
        'e_phoff': struct.unpack('<I', data[28:32])[0],
        'e_shoff': struct.unpack('<I', data[32:36])[0],
        'e_flags': struct.unpack('<I', data[36:40])[0],
        'e_ehsize': struct.unpack('<H', data[40:42])[0],
        'e_phentsize': struct.unpack('<H', data[42:44])[0],
        'e_phnum': struct.unpack('<H', data[44:46])[0],
        'e_shentsize': struct.unpack('<H', data[46:48])[0],
        'e_shnum': struct.unpack('<H', data[48:50])[0],
        'e_shstrndx': struct.unpack('<H', data[50:52])[0],
    }


def read_sections(f, hdr):
    """Read all section headers and their names. Returns list of dicts."""
    e_shoff = hdr['e_shoff']
    e_shentsize = hdr['e_shentsize']
    e_shnum = hdr['e_shnum']
    e_shstrndx = hdr['e_shstrndx']

    # Read section string table
    f.seek(e_shoff + e_shstrndx * e_shentsize)
    sh = f.read(e_shentsize)
    strtab_off = struct.unpack('<I', sh[16:20])[0]
    strtab_size = struct.unpack('<I', sh[20:24])[0]
    f.seek(strtab_off)
    strtab = f.read(strtab_size)

    sections = []
    for i in range(e_shnum):
        f.seek(e_shoff + i * e_shentsize)
        sh = f.read(e_shentsize)

        sh_name_off = struct.unpack('<I', sh[0:4])[0]
        end = strtab.find(b'\x00', sh_name_off)
        if end == -1:
            end = len(strtab)
        name = strtab[sh_name_off:end].decode('ascii', errors='replace')

        sections.append({
            'index': i,
            'name': name,
            'sh_type': struct.unpack('<I', sh[4:8])[0],
            'sh_flags': struct.unpack('<I', sh[8:12])[0],
            'sh_addr': struct.unpack('<I', sh[12:16])[0],
            'sh_offset': struct.unpack('<I', sh[16:20])[0],
            'sh_size': struct.unpack('<I', sh[20:24])[0],
            'sh_link': struct.unpack('<I', sh[24:28])[0],
            'sh_info': struct.unpack('<I', sh[28:32])[0],
            'sh_addralign': struct.unpack('<I', sh[32:36])[0],
            'sh_entsize': struct.unpack('<I', sh[36:40])[0],
        })

    return sections


def find_section(sections, name):
    """Find a section by exact name. Returns section dict or None."""
    for s in sections:
        if s['name'] == name:
            return s
    return None


def read_section_data(f, section):
    """Read raw data from a section."""
    f.seek(section['sh_offset'])
    return f.read(section['sh_size'])


def parse_overlay_strtab(data):
    """Parse null-terminated strings from the overlay string table.

    Returns dict mapping byte offset -> string.
    """
    strings = {}
    pos = 0
    while pos < len(data):
        end = data.find(b'\x00', pos)
        if end == -1:
            end = len(data)
        s = data[pos:end].decode('ascii', errors='replace')
        if s:
            strings[pos] = s
        pos = end + 1
    return strings


def parse_overlay_table(data, strtab_data, overlay_sections):
    """Parse the DVP overlay table.

    Each entry is 12 bytes: [name_strtab_offset, lma, vma].
    Returns list of overlay entry dicts.
    """
    n_entries = len(data) // 12
    strtab_strings = parse_overlay_strtab(strtab_data)

    entries = []
    for i in range(n_entries):
        off = i * 12
        name_off, lma, vma = struct.unpack('<III', data[off:off + 12])

        # Look up name from string table
        name = strtab_strings.get(name_off, f"unknown_{i}")

        # Match to overlay section for size
        sec_size = 0
        if i < len(overlay_sections):
            sec_size = overlay_sections[i]['sh_size']

        entries.append({
            'index': i,
            'name': name,
            'name_off': name_off,
            'lma': lma,
            'vma': vma,
            'size': sec_size,
            'n_instructions': sec_size // VU1_INSTRUCTION_SIZE,
        })

    return entries


def find_lma_section(sections, lma):
    """Find which section contains a given load memory address.

    Returns (section, file_offset) or (None, 0).
    """
    for s in sections:
        if s['sh_addr'] == 0 or s['sh_size'] == 0:
            continue
        if s['sh_addr'] <= lma < s['sh_addr'] + s['sh_size']:
            file_off = s['sh_offset'] + (lma - s['sh_addr'])
            return s, file_off
    return None, 0


def read_overlay_code(f, entry, sections):
    """Read actual VU1 code from the LMA location.

    The overlay sections themselves are zeroed (BSS). The real code
    lives at the LMA address, which falls in .vutext or .srs.
    """
    sec, file_off = find_lma_section(sections, entry['lma'])
    if sec is None:
        return None, None, 0

    f.seek(file_off)
    data = f.read(entry['size'])
    return data, sec['name'], file_off


def decode_flags(upper):
    """Decode VU1 instruction flag bits from upper word."""
    flags = []
    if upper & FLAG_I:
        flags.append('I')
    if upper & FLAG_E:
        flags.append('E')
    if upper & FLAG_M:
        flags.append('M')
    if upper & FLAG_D:
        flags.append('D')
    if upper & FLAG_T:
        flags.append('T')
    return flags


def analyze_instructions(data):
    """Analyze VU1 instruction data. Returns analysis dict."""
    n_inst = len(data) // VU1_INSTRUCTION_SIZE
    e_flag_locations = []
    i_flag_count = 0
    float_immediates = []
    nop_count = 0

    for i in range(n_inst):
        off = i * VU1_INSTRUCTION_SIZE
        lower = struct.unpack('<I', data[off:off + 4])[0]
        upper = struct.unpack('<I', data[off + 4:off + 8])[0]

        flags = decode_flags(upper)

        if 'E' in flags:
            e_flag_locations.append(i)

        if 'I' in flags:
            i_flag_count += 1
            # The lower word is an IEEE754 float immediate
            float_val = struct.unpack('<f', data[off:off + 4])[0]
            float_immediates.append({
                'instruction': i,
                'raw': f"0x{lower:08X}",
                'value': float_val,
            })

        # NOP = upper=0x000002FF lower=0x8000033C (common VU1 NOP pair)
        # Also check for all-zero (padding)
        if (upper == 0 and lower == 0) or \
           ((upper & 0x07FFFFFF) == 0x000002FF and lower == 0x8000033C):
            nop_count += 1

    return {
        'n_instructions': n_inst,
        'e_flag_locations': e_flag_locations,
        'i_flag_count': i_flag_count,
        'float_immediates': float_immediates,
        'nop_count': nop_count,
        'code_density': 1.0 - (nop_count / n_inst) if n_inst > 0 else 0,
    }


def format_hex_listing(data, vma_base=0, max_lines=None):
    """Format VU1 instructions as a hex listing string."""
    lines = []
    n_inst = len(data) // VU1_INSTRUCTION_SIZE

    if max_lines and n_inst > max_lines:
        n_inst = max_lines

    for i in range(n_inst):
        off = i * VU1_INSTRUCTION_SIZE
        lower = struct.unpack('<I', data[off:off + 4])[0]
        upper = struct.unpack('<I', data[off + 4:off + 8])[0]

        flags = decode_flags(upper)
        flag_str = ''.join(flags) if flags else '-'

        vma_addr = vma_base + i * VU1_INSTRUCTION_SIZE
        lines.append(f"  0x{vma_addr:04X} [{i:4d}] {upper:08X} {lower:08X}  {flag_str}")

        if 'I' in flags:
            float_val = struct.unpack('<f', data[off:off + 4])[0]
            lines[-1] += f"  (float: {float_val})"

    return '\n'.join(lines)


def group_overlays(entries):
    """Group overlays by program ID extracted from section names.

    Section name format: .DVP.overlay..{vma}.{id}.{num}.{seq}
    or: .DVP.overlay..unknvma.{id}.{num}.{seq}

    We group by looking at which overlays share contiguous VMA ranges
    and have related IDs. The pattern is:
    - Each program has a small init overlay at VMA=0
    - Followed by a main overlay also at VMA=0
    - Then continuation overlays stepping through VU1 micro memory
    """
    if not entries:
        return []

    # Group by looking at VMA resets: when VMA goes back to 0 after
    # having been > 0, that's a new program
    programs = []
    current = []
    prev_vma = -1

    for entry in entries:
        if entry['vma'] == 0 and prev_vma > 0:
            # VMA reset - new program group
            if current:
                programs.append(current)
            current = [entry]
        elif entry['vma'] == 0 and prev_vma == 0:
            # Second overlay at VMA=0 - same program (init then main)
            current.append(entry)
        else:
            current.append(entry)
        prev_vma = entry['vma']

    if current:
        programs.append(current)

    return programs


def assemble_program(f, overlays, sections):
    """Assemble a complete VU1 program from its overlay fragments.

    Overlays are laid out by VMA into a single VU1 micro memory image.
    When multiple overlays target the same VMA, the larger one takes
    precedence (it's the main code, the smaller one is init/header).
    """
    # Create a 16KB buffer for VU1 micro memory
    micro_mem = bytearray(VU1_MICRO_MEM_SIZE)
    max_used = 0

    # Sort overlays by VMA, then by size (largest last = takes precedence)
    sorted_ovlys = sorted(overlays, key=lambda o: (o['vma'], o['size']))

    for ovly in sorted_ovlys:
        data, sec_name, file_off = read_overlay_code(f, ovly, sections)
        if data is None:
            continue

        vma = ovly['vma']
        size = min(len(data), VU1_MICRO_MEM_SIZE - vma)
        if vma + size > VU1_MICRO_MEM_SIZE:
            size = VU1_MICRO_MEM_SIZE - vma

        micro_mem[vma:vma + size] = data[:size]
        end = vma + size
        if end > max_used:
            max_used = end

    return bytes(micro_mem[:max_used])


def identify_program_names(programs, f, sections):
    """Try to identify programs as RasterMicro or BillboardMicro.

    Heuristics:
    - RasterMicro: uses float immediates (I flag), handles general geometry
    - BillboardMicro: no float immediates, simpler program for billboards
    - RasterMicro is typically in .vutext, BillboardMicro in .srs
    """
    names = []
    for prog_overlays in programs:
        has_i_flag = False
        in_vutext = False

        for ovly in prog_overlays:
            data, sec_name, _ = read_overlay_code(f, ovly, sections)
            if data is None:
                continue
            if sec_name == '.vutext':
                in_vutext = True

            # Check for I flag
            for i in range(len(data) // VU1_INSTRUCTION_SIZE):
                upper = struct.unpack('<I', data[i * 8 + 4:i * 8 + 8])[0]
                if upper & FLAG_I:
                    has_i_flag = True
                    break
            if has_i_flag:
                break

        # RasterMicro uses float immediates and is in .vutext
        # BillboardMicro has no immediates and is in .srs
        if has_i_flag and in_vutext:
            names.append('RasterMicro')
        elif not has_i_flag and not in_vutext:
            names.append('BillboardMicro')
        elif has_i_flag:
            names.append('RasterMicro')
        elif in_vutext:
            names.append(f'Program_{len(names)}')
        else:
            names.append('BillboardMicro')

    return names


def main():
    parser = argparse.ArgumentParser(
        description='Extract VU1 microcode programs from PS2 ELF DVP overlay sections.',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument('elf_path', help='Path to PS2 ELF file')
    parser.add_argument('-o', '--output', default='output/vu1',
                        help='Output directory (default: output/vu1)')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Print detailed hex listings')
    parser.add_argument('--raw-only', action='store_true',
                        help='Only extract raw binary files, skip analysis')
    args = parser.parse_args()

    elf_path = Path(args.elf_path)
    if not elf_path.exists():
        print(f"Error: ELF file not found: {elf_path}", file=sys.stderr)
        sys.exit(1)

    output_dir = Path(args.output)
    programs_dir = output_dir / 'programs'
    output_dir.mkdir(parents=True, exist_ok=True)
    programs_dir.mkdir(parents=True, exist_ok=True)

    with open(elf_path, 'rb') as f:
        # --- Parse ELF ---
        hdr = read_elf32_header(f)
        print(f"ELF: {elf_path.name}")
        print(f"  Machine: {hdr['e_machine']} (8=MIPS)")
        print(f"  Entry: 0x{hdr['e_entry']:08X}")
        print(f"  Sections: {hdr['e_shnum']}")
        print()

        sections = read_sections(f, hdr)

        # --- Find DVP sections ---
        ovlytab_sec = find_section(sections, '.DVP.ovlytab')
        ovlystrtab_sec = find_section(sections, '.DVP.ovlystrtab')

        if ovlytab_sec is None:
            print("Error: .DVP.ovlytab section not found", file=sys.stderr)
            sys.exit(1)
        if ovlystrtab_sec is None:
            print("Error: .DVP.ovlystrtab section not found", file=sys.stderr)
            sys.exit(1)

        overlay_sections = [s for s in sections if '.DVP.overlay.' in s['name']]
        overlay_sections.sort(key=lambda s: s['index'])

        print(f"DVP sections found:")
        print(f"  .DVP.ovlytab:    {ovlytab_sec['sh_size']} bytes "
              f"({ovlytab_sec['sh_size'] // 12} entries)")
        print(f"  .DVP.ovlystrtab: {ovlystrtab_sec['sh_size']} bytes")
        print(f"  .DVP.overlay.*:  {len(overlay_sections)} sections")
        print()

        # --- Parse overlay table ---
        ovlytab_data = read_section_data(f, ovlytab_sec)
        ovlystrtab_data = read_section_data(f, ovlystrtab_sec)
        entries = parse_overlay_table(ovlytab_data, ovlystrtab_data,
                                      overlay_sections)

        print(f"Overlay Table ({len(entries)} entries):")
        print(f"  {'#':>2s}  {'VMA':>6s}  {'LMA':>10s}  {'Size':>6s}  "
              f"{'Instr':>5s}  {'Source':>8s}  Name")
        print(f"  {'--':>2s}  {'------':>6s}  {'----------':>10s}  {'------':>6s}  "
              f"{'-----':>5s}  {'--------':>8s}  ----")

        for entry in entries:
            sec, file_off = find_lma_section(sections, entry['lma'])
            src_name = sec['name'] if sec else 'unknown'
            print(f"  {entry['index']:2d}  "
                  f"0x{entry['vma']:04X}  "
                  f"0x{entry['lma']:08X}  "
                  f"{entry['size']:6d}  "
                  f"{entry['n_instructions']:5d}  "
                  f"{src_name:>8s}  "
                  f"{entry['name']}")
        print()

        # --- Extract individual overlays ---
        overlay_analyses = []
        for entry in entries:
            data, sec_name, file_off = read_overlay_code(f, entry, sections)

            if data is None:
                print(f"  WARNING: Could not read code for overlay {entry['index']} "
                      f"(LMA=0x{entry['lma']:08X})")
                overlay_analyses.append(None)
                continue

            # Save raw binary
            bin_path = output_dir / f"overlay_{entry['index']:02d}.bin"
            with open(bin_path, 'wb') as out:
                out.write(data)

            if args.raw_only:
                overlay_analyses.append(None)
                continue

            # Analyze
            analysis = analyze_instructions(data)
            analysis['sha256'] = hashlib.sha256(data).hexdigest()
            analysis['source_section'] = sec_name
            analysis['file_offset'] = f"0x{file_off:06X}"
            overlay_analyses.append(analysis)

            if args.verbose:
                print(f"  Overlay {entry['index']} "
                      f"(VMA=0x{entry['vma']:04X}, {entry['n_instructions']} inst, "
                      f"from {sec_name} @ 0x{file_off:06X}):")
                print(format_hex_listing(data, vma_base=entry['vma']))
                print()

        print(f"Extracted {len(entries)} overlay binaries to {output_dir}/")
        print()

        # --- Group into programs ---
        programs = group_overlays(entries)
        prog_names = identify_program_names(programs, f, sections)

        print(f"Programs identified: {len(programs)}")
        for pi, (prog_overlays, name) in enumerate(zip(programs, prog_names)):
            ovly_indices = [o['index'] for o in prog_overlays]
            total_inst = sum(o['n_instructions'] for o in prog_overlays)

            # Assemble full program
            assembled = assemble_program(f, prog_overlays, sections)
            prog_hash = hashlib.sha256(assembled).hexdigest()

            # Save assembled program
            prog_path = programs_dir / f"{name}.bin"
            with open(prog_path, 'wb') as out:
                out.write(assembled)

            print(f"  {pi + 1}. {name}")
            print(f"     Overlays: {ovly_indices}")
            print(f"     Overlay instruction total: {total_inst}")
            print(f"     Assembled size: {len(assembled)} bytes "
                  f"({len(assembled) // VU1_INSTRUCTION_SIZE} instructions)")
            print(f"     SHA256: {prog_hash}")

            if not args.raw_only:
                prog_analysis = analyze_instructions(assembled)
                print(f"     E flags at instructions: {prog_analysis['e_flag_locations']}")
                print(f"     Float immediates: {prog_analysis['i_flag_count']}")
                print(f"     NOPs: {prog_analysis['nop_count']}")
                print(f"     Code density: {prog_analysis['code_density']:.1%}")
            print()

        # --- Generate JSON metadata ---
        if not args.raw_only:
            metadata = {
                'elf': str(elf_path),
                'elf_machine': hdr['e_machine'],
                'elf_entry': f"0x{hdr['e_entry']:08X}",
                'vu1_micro_mem_size': VU1_MICRO_MEM_SIZE,
                'instruction_size': VU1_INSTRUCTION_SIZE,
                'n_overlays': len(entries),
                'overlays': [],
                'programs': [],
            }

            for entry, analysis in zip(entries, overlay_analyses):
                ovly_meta = {
                    'index': entry['index'],
                    'name': entry['name'],
                    'vma': f"0x{entry['vma']:04X}",
                    'lma': f"0x{entry['lma']:08X}",
                    'size': entry['size'],
                    'n_instructions': entry['n_instructions'],
                }
                if analysis:
                    ovly_meta.update({
                        'sha256': analysis['sha256'],
                        'source_section': analysis['source_section'],
                        'file_offset': analysis['file_offset'],
                        'e_flag_locations': analysis['e_flag_locations'],
                        'i_flag_count': analysis['i_flag_count'],
                        'nop_count': analysis['nop_count'],
                        'code_density': round(analysis['code_density'], 3),
                    })
                metadata['overlays'].append(ovly_meta)

            for pi, (prog_overlays, name) in enumerate(zip(programs, prog_names)):
                assembled = assemble_program(f, prog_overlays, sections)
                prog_analysis = analyze_instructions(assembled)

                metadata['programs'].append({
                    'name': name,
                    'overlay_indices': [o['index'] for o in prog_overlays],
                    'assembled_size': len(assembled),
                    'n_instructions': len(assembled) // VU1_INSTRUCTION_SIZE,
                    'sha256': hashlib.sha256(assembled).hexdigest(),
                    'e_flag_locations': prog_analysis['e_flag_locations'],
                    'i_flag_count': prog_analysis['i_flag_count'],
                    'float_immediates': [
                        {'instruction': fi['instruction'],
                         'raw': fi['raw'],
                         'value': fi['value']}
                        for fi in prog_analysis['float_immediates']
                    ],
                    'nop_count': prog_analysis['nop_count'],
                    'code_density': round(prog_analysis['code_density'], 3),
                })

            json_path = output_dir / 'overlay_table.json'
            with open(json_path, 'w') as out:
                json.dump(metadata, out, indent=2)
            print(f"Metadata written to {json_path}")

        # --- Generate summary.md ---
        if not args.raw_only:
            generate_summary(output_dir, entries, overlay_analyses,
                             programs, prog_names, f, sections, elf_path)


def generate_summary(output_dir, entries, overlay_analyses,
                     programs, prog_names, f, sections, elf_path):
    """Generate human-readable summary.md."""
    lines = [
        "# VU1 Microcode Extraction — Champions of Norrath",
        "",
        f"Source: `{elf_path.name}`",
        "",
        "## Overlay Table ({} entries)".format(len(entries)),
        "",
        "| # | Name | VMA | Size | LMA | Source | Instructions |",
        "|---|------|-----|------|-----|--------|-------------|",
    ]

    for entry, analysis in zip(entries, overlay_analyses):
        sec, _ = find_lma_section(sections, entry['lma'])
        src = sec['name'] if sec else '?'
        name_short = entry['name'].replace('.DVP.overlay..', '')
        lines.append(
            f"| {entry['index']} | {name_short} | "
            f"0x{entry['vma']:04X} | {entry['size']} | "
            f"0x{entry['lma']:08X} | {src} | {entry['n_instructions']} |"
        )

    lines.extend(["", "## Programs", ""])

    for pi, (prog_overlays, name) in enumerate(zip(programs, prog_names)):
        assembled = assemble_program(f, prog_overlays, sections)
        prog_analysis = analyze_instructions(assembled)
        prog_hash = hashlib.sha256(assembled).hexdigest()
        ovly_indices = [str(o['index']) for o in prog_overlays]

        lines.extend([
            f"### {pi + 1}. {name}",
            "",
            f"- **Assembled size:** {len(assembled)} bytes "
            f"({len(assembled) // VU1_INSTRUCTION_SIZE} instructions)",
            f"- **SHA256:** `{prog_hash}`",
            f"- **Overlays:** {', '.join(ovly_indices)}",
            f"- **E flags at:** instruction(s) "
            f"{', '.join(str(e) for e in prog_analysis['e_flag_locations'])}",
            f"- **Float immediates (I flag):** {prog_analysis['i_flag_count']}",
            f"- **NOPs:** {prog_analysis['nop_count']} "
            f"({prog_analysis['nop_count'] * 100 // max(prog_analysis['n_instructions'], 1)}%)",
            f"- **Code density:** {prog_analysis['code_density']:.1%}",
            "",
        ])

        # VMA coverage
        lines.append("**VMA coverage:**")
        lines.append("")
        lines.append("| Overlay | VMA Range | Instructions |")
        lines.append("|---------|-----------|-------------|")

        for ovly in prog_overlays:
            vma_start = ovly['vma']
            vma_end = vma_start + ovly['size']
            inst_start = vma_start // VU1_INSTRUCTION_SIZE
            inst_end = inst_start + ovly['n_instructions']
            lines.append(
                f"| {ovly['index']} | "
                f"0x{vma_start:04X}-0x{vma_end:04X} | "
                f"{inst_start}-{inst_end} |"
            )

        lines.append("")

        # Float immediates
        if prog_analysis['float_immediates']:
            lines.extend([
                "**Float immediates (I flag):**",
                "",
                "| Instruction | Raw | Value |",
                "|-------------|-----|-------|",
            ])
            for fi in prog_analysis['float_immediates']:
                lines.append(
                    f"| {fi['instruction']} | {fi['raw']} | {fi['value']} |"
                )
            lines.append("")

    # Architecture notes
    lines.extend([
        "## Architecture Notes",
        "",
        "VU1 micro memory is 16KB (2048 instruction slots). Each instruction pair",
        "is 8 bytes: lower 32 bits (integer/branch) + upper 32 bits (FMAC/float).",
        "",
        "The DVP overlay mechanism splits programs into 2KB chunks that are loaded",
        "into VU1 micro memory via DMA. Each program has:",
        "- A small init overlay at VMA 0x0000 (vector table / startup code)",
        "- A main overlay also at VMA 0x0000 (overwrites init during normal operation)",
        "- Continuation overlays at VMA 0x0800, 0x1000, ... stepping through micro memory",
        "",
        "The overlay sections in the ELF are BSS-like (zeroed). Actual code resides at",
        "the LMA (load memory address), which falls in `.vutext` (RasterMicro) or",
        "`.srs` (BillboardMicro).",
        "",
        "Upload functions in the EE code (UploadRasterMicro, UploadBillboardMicro) DMA",
        "these fragments from main RAM into VU1 micro memory at the target VMA offsets.",
    ])

    summary_path = output_dir / 'summary.md'
    with open(summary_path, 'w') as out:
        out.write('\n'.join(lines) + '\n')
    print(f"Summary written to {summary_path}")


if __name__ == '__main__':
    main()
