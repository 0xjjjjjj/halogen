#!/usr/bin/env python3
"""DWARF1 struct layout parser for PS2 Metrowerks CodeWarrior debug info.

Reads .debug section from a PS2 ELF and extracts struct/class/union/enum
definitions with member names, byte offsets, and sizes. Outputs JSON.

DWARF1 format: each DIE is [4-byte length][2-byte tag][attributes...].
Attributes are [2-byte name] where low 4 bits = form, upper 12 bits = attr ID.
"""

import struct
import json
import sys
from pathlib import Path

# Tags
TAG_CLASS_TYPE = 0x02
TAG_ENUMERATION_TYPE = 0x04
TAG_FORMAL_PARAMETER = 0x05
TAG_MEMBER = 0x0d
TAG_STRUCTURE_TYPE = 0x13
TAG_TYPEDEF = 0x16
TAG_UNION_TYPE = 0x17
TAG_INHERITANCE = 0x1c

TAG_NAMES = {
    0x00: "padding", 0x01: "array_type", 0x02: "class_type", 0x03: "entry_point",
    0x04: "enumeration_type", 0x05: "formal_parameter", 0x06: "global_subroutine",
    0x07: "global_variable", 0x0a: "label", 0x0b: "lexical_block",
    0x0c: "local_variable", 0x0d: "member", 0x0f: "pointer_type",
    0x10: "reference_type", 0x11: "compile_unit", 0x12: "string_type",
    0x13: "structure_type", 0x14: "subroutine", 0x15: "subroutine_type",
    0x16: "typedef", 0x17: "union_type", 0x18: "unspecified_parameters",
    0x19: "variant", 0x1a: "common_block", 0x1c: "inheritance",
    0x1d: "inlined_subroutine", 0x1e: "module", 0x1f: "ptr_to_member_type",
    0x20: "set_type", 0x21: "subrange_type",
}

# Attributes
AT_SIBLING = 0x001
AT_LOCATION = 0x002
AT_NAME = 0x003
AT_FUND_TYPE = 0x005
AT_MOD_FUND_TYPE = 0x006
AT_USER_DEF_TYPE = 0x007
AT_MOD_U_D_TYPE = 0x008
AT_BYTE_SIZE = 0x00b
AT_BIT_OFFSET = 0x00c
AT_BIT_SIZE = 0x00d
AT_ELEMENT_LIST = 0x00f
AT_VIRTUAL = 0x030
AT_PRIVATE = 0x024
AT_PROTECTED = 0x026
AT_PUBLIC = 0x028

# Forms
FORM_ADDR = 1
FORM_REF = 2
FORM_BLOCK2 = 3
FORM_BLOCK4 = 4
FORM_DATA2 = 5
FORM_DATA4 = 6
FORM_DATA8 = 7
FORM_STRING = 8

# Fundamental types
FUND_TYPES = {
    0x0001: "char", 0x0002: "signed char", 0x0003: "unsigned char",
    0x0004: "short", 0x0005: "signed short", 0x0006: "unsigned short",
    0x0007: "int", 0x0008: "signed int", 0x0009: "unsigned int",
    0x000a: "long", 0x000b: "signed long", 0x000c: "unsigned long",
    0x000d: "void*", 0x000e: "float", 0x000f: "double",
    0x0010: "long double", 0x0014: "void", 0x0015: "bool",
    0x8008: "long long", 0x8108: "signed long long", 0x8208: "unsigned long long",
}

MOD_POINTER = 0x01
MOD_REFERENCE = 0x02
MOD_CONST = 0x03
MOD_VOLATILE = 0x04


def parse_attribute(data, offset):
    """Parse one DWARF1 attribute. Returns (attr_id, form, value, new_offset)."""
    raw = struct.unpack_from('<H', data, offset)[0]
    offset += 2
    form = raw & 0xf
    attr_id = raw >> 4

    if form == FORM_ADDR:
        val = struct.unpack_from('<I', data, offset)[0]; offset += 4
    elif form == FORM_REF:
        val = struct.unpack_from('<I', data, offset)[0]; offset += 4
    elif form == FORM_BLOCK2:
        sz = struct.unpack_from('<H', data, offset)[0]; offset += 2
        val = bytes(data[offset:offset+sz]); offset += sz
    elif form == FORM_BLOCK4:
        sz = struct.unpack_from('<I', data, offset)[0]; offset += 4
        val = bytes(data[offset:offset+sz]); offset += sz
    elif form == FORM_DATA2:
        val = struct.unpack_from('<H', data, offset)[0]; offset += 2
    elif form == FORM_DATA4:
        val = struct.unpack_from('<I', data, offset)[0]; offset += 4
    elif form == FORM_DATA8:
        val = struct.unpack_from('<Q', data, offset)[0]; offset += 8
    elif form == FORM_STRING:
        end = data.index(b'\0', offset)
        val = data[offset:end].decode('utf-8', errors='replace'); offset = end + 1
    else:
        raise ValueError(f"Unknown form 0x{form:x} at 0x{offset-2:x}")

    return attr_id, form, val, offset


def parse_die(data, offset):
    """Parse a DIE. Returns (die_offset, tag, attrs_dict, die_end) or None for padding."""
    if offset + 4 > len(data):
        return None
    length = struct.unpack_from('<I', data, offset)[0]
    if length < 8:
        # Padding entry — return with tag=None so caller can advance correctly.
        skip = max(length, 4)
        return (offset, None, {}, offset + skip)

    tag = struct.unpack_from('<H', data, offset + 4)[0]
    attrs = {}
    pos = offset + 6
    die_end = offset + length

    while pos < die_end:
        try:
            attr_id, form, val, pos = parse_attribute(data, pos)
            attrs[attr_id] = val
        except (struct.error, ValueError, IndexError):
            break

    return (offset, tag, attrs, die_end)


def location_to_offset(block):
    """Extract byte offset from a DWARF1 location description."""
    if isinstance(block, (bytes, bytearray)) and len(block) >= 5:
        op = block[0]
        if op in (0x03, 0x04):  # OP_ADDR, OP_CONST
            return struct.unpack_from('<I', block, 1)[0]
    return None


def resolve_type_name(attrs, types_by_offset):
    """Resolve a type from DWARF1 attributes to a human-readable name."""
    if AT_USER_DEF_TYPE in attrs:
        ref = attrs[AT_USER_DEF_TYPE]
        return types_by_offset.get(ref, {}).get('name', f'type@0x{ref:x}')

    if AT_MOD_U_D_TYPE in attrs:
        block = attrs[AT_MOD_U_D_TYPE]
        if len(block) >= 4:
            ref = struct.unpack_from('<I', block, len(block) - 4)[0]
            mods = list(block[:len(block) - 4])
            name = types_by_offset.get(ref, {}).get('name', f'type@0x{ref:x}')
            return _apply_modifiers(name, mods)

    if AT_FUND_TYPE in attrs:
        return FUND_TYPES.get(attrs[AT_FUND_TYPE], f'ft_0x{attrs[AT_FUND_TYPE]:x}')

    if AT_MOD_FUND_TYPE in attrs:
        block = attrs[AT_MOD_FUND_TYPE]
        if len(block) >= 2:
            ft = struct.unpack_from('<H', block, len(block) - 2)[0]
            mods = list(block[:len(block) - 2])
            return _apply_modifiers(FUND_TYPES.get(ft, f'ft_0x{ft:x}'), mods)

    return None


def _apply_modifiers(name, modifiers):
    """Apply DWARF1 type modifiers (read left-to-right = English order)."""
    for m in modifiers:
        if m == MOD_POINTER:
            name += '*'
        elif m == MOD_REFERENCE:
            name += '&'
        elif m == MOD_CONST:
            name = 'const ' + name
        elif m == MOD_VOLATILE:
            name = 'volatile ' + name
    return name


def parse_enum_elements(block):
    """Parse a DWARF1 enumeration element list block."""
    constants = []
    offset = 0
    while offset + 4 < len(block):
        val = struct.unpack_from('<i', block, offset)[0]  # signed
        offset += 4
        try:
            end = block.index(b'\0', offset)
            name = block[offset:end].decode('utf-8', errors='replace')
            offset = end + 1
            constants.append({'name': name, 'value': val})
        except (ValueError, IndexError):
            break
    return constants


def get_access(attrs):
    if AT_PRIVATE in attrs:
        return 'private'
    if AT_PROTECTED in attrs:
        return 'protected'
    if AT_PUBLIC in attrs:
        return 'public'
    return None


def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <elf_path> [output.json]", file=sys.stderr)
        sys.exit(1)

    elf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    # Read .debug section using pyelftools
    from elftools.elf.elffile import ELFFile
    with open(elf_path, 'rb') as f:
        elf = ELFFile(f)
        debug_section = None
        for section in elf.iter_sections():
            if section.name == '.debug':
                debug_section = section
                break
        if not debug_section:
            print("No .debug section found", file=sys.stderr)
            sys.exit(1)
        debug_data = debug_section.data()

    print(f"Parsing {len(debug_data):,} bytes of DWARF1 debug data...", file=sys.stderr)

    # Pass 1: Parse all DIEs, index type definitions by offset
    dies = []
    types_by_offset = {}
    offset = 0
    while offset < len(debug_data):
        result = parse_die(debug_data, offset)
        if result is None:
            break  # end of data
        die_off, tag, attrs, die_end = result
        if tag is None:
            offset = die_end  # skip padding
            continue
        dies.append(result)

        name = attrs.get(AT_NAME)
        if tag in (TAG_STRUCTURE_TYPE, TAG_CLASS_TYPE, TAG_UNION_TYPE,
                   TAG_ENUMERATION_TYPE, TAG_TYPEDEF):
            types_by_offset[die_off] = {
                'name': name or f'anon@0x{die_off:x}',
                'tag': TAG_NAMES.get(tag, f'0x{tag:x}'),
            }

        offset = die_end

    print(f"Pass 1: {len(dies):,} DIEs, {len(types_by_offset):,} named types", file=sys.stderr)

    # Pass 2: Extract struct/class/union with members, enums, typedefs
    structs = []
    enums = []
    typedefs = []

    i = 0
    while i < len(dies):
        die_off, tag, attrs, die_end = dies[i]

        if tag in (TAG_STRUCTURE_TYPE, TAG_CLASS_TYPE, TAG_UNION_TYPE):
            kind = {TAG_STRUCTURE_TYPE: 'struct', TAG_CLASS_TYPE: 'class',
                    TAG_UNION_TYPE: 'union'}[tag]
            info = {
                'name': attrs.get(AT_NAME),
                'kind': kind,
                'byte_size': attrs.get(AT_BYTE_SIZE),
                'members': [],
                'base_classes': [],
            }

            sibling = attrs.get(AT_SIBLING)

            # Walk children
            j = i + 1
            while j < len(dies):
                c_off, c_tag, c_attrs, c_end = dies[j]
                if sibling is not None and c_off >= sibling:
                    break

                if c_tag == TAG_MEMBER:
                    m = {
                        'name': c_attrs.get(AT_NAME),
                        'type': resolve_type_name(c_attrs, types_by_offset),
                    }
                    if AT_LOCATION in c_attrs:
                        off = location_to_offset(c_attrs[AT_LOCATION])
                        if off is not None:
                            m['offset'] = off
                    if AT_BYTE_SIZE in c_attrs:
                        m['size'] = c_attrs[AT_BYTE_SIZE]
                    if AT_BIT_SIZE in c_attrs:
                        m['bit_size'] = c_attrs[AT_BIT_SIZE]
                    if AT_BIT_OFFSET in c_attrs:
                        m['bit_offset'] = c_attrs[AT_BIT_OFFSET]
                    access = get_access(c_attrs)
                    if access:
                        m['access'] = access
                    info['members'].append(m)

                elif c_tag == TAG_INHERITANCE:
                    base = {
                        'type': resolve_type_name(c_attrs, types_by_offset),
                    }
                    if AT_LOCATION in c_attrs:
                        off = location_to_offset(c_attrs[AT_LOCATION])
                        if off is not None:
                            base['offset'] = off
                    if AT_VIRTUAL in c_attrs:
                        base['virtual'] = True
                    access = get_access(c_attrs)
                    if access:
                        base['access'] = access
                    info['base_classes'].append(base)

                j += 1

            structs.append(info)

        elif tag == TAG_ENUMERATION_TYPE:
            info = {
                'name': attrs.get(AT_NAME),
                'byte_size': attrs.get(AT_BYTE_SIZE),
                'constants': [],
            }
            if AT_ELEMENT_LIST in attrs:
                info['constants'] = parse_enum_elements(attrs[AT_ELEMENT_LIST])
            enums.append(info)

        elif tag == TAG_TYPEDEF:
            typedefs.append({
                'name': attrs.get(AT_NAME),
                'type': resolve_type_name(attrs, types_by_offset),
            })

        i += 1

    print(f"Pass 2: {len(structs)} structs/classes/unions, "
          f"{len(enums)} enums, {len(typedefs)} typedefs", file=sys.stderr)

    result = {'structs': structs, 'enums': enums, 'typedefs': typedefs}
    output = json.dumps(result, indent=2)

    if output_path:
        Path(output_path).write_text(output)
        print(f"Written to {output_path}", file=sys.stderr)
    else:
        print(output)


if __name__ == '__main__':
    main()
