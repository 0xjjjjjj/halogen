#!/usr/bin/env python3
"""PCSX2 GS dump parser — extracts rendering statistics from .gs dump files.

Parses the binary GS dump format produced by PCSX2's GS debugger and extracts
per-frame rendering statistics including draw call counts, primitive types,
vertex counts, register write frequencies, transfer sizes, and texture uploads.

GS Dump Binary Format (PCSX2 new format):
    Header: [0xFFFFFFFF magic][header_size:u32][GSDumpHeader:36 bytes]
            [serial string][screenshot RGBA][GS state][GSPrivRegSet:8192 bytes]
    Packets: sequential stream of typed packets:
        Type 0 (Transfer): [path:u8][size:u32][data...]
        Type 1 (VSync):    [field:u8]
        Type 2 (ReadFIFO2):[size:u32]
        Type 3 (Registers):[8192 bytes]

Transfer data contains GIF packets with GIFTags (128-bit headers) that describe
GS register writes. Draw kicks occur on XYZ2/XYZF2 register writes.

Usage:
    python parse-gs-dump.py <dump.gs>                 # Human-readable report
    python parse-gs-dump.py <dump.gs> --json           # JSON output
    python parse-gs-dump.py <dump.gs> -o stats.json    # JSON to file
    python parse-gs-dump.py <dump.gs> -v               # Verbose (show GIFTags)
    python parse-gs-dump.py --create-test-dump test.gs # Create synthetic dump
"""

import argparse
import collections
import json
import os
import struct
import sys


# ─── Constants ───

# GS dump packet types
PKT_TRANSFER = 0
PKT_VSYNC = 1
PKT_READFIFO2 = 2
PKT_REGISTERS = 3

# GIFTag FLG modes
FLG_PACKED = 0
FLG_REGLIST = 1
FLG_IMAGE = 2

# GS primitive types (PRIM register bits [2:0])
PRIM_TYPES = {
    0: "Point",
    1: "Line",
    2: "LineStrip",
    3: "Tri",
    4: "TriStrip",
    5: "TriFan",
    6: "Sprite",
    7: "Reserved",
}

# GS register IDs (4-bit, used in GIFTag REGS field)
GIF_REG_NAMES = {
    0x00: "PRIM",
    0x01: "RGBAQ",
    0x02: "ST",
    0x03: "UV",
    0x04: "XYZF2",
    0x05: "XYZ2",
    0x06: "TEX0_1",
    0x07: "TEX0_2",
    0x08: "CLAMP_1",
    0x09: "CLAMP_2",
    0x0A: "FOG",
    0x0C: "XYZF3",
    0x0D: "XYZ3",
    0x0E: "A+D",
    0x0F: "NOP",
}

# A+D register addresses (8-bit, inside A+D data)
AD_REG_NAMES = {
    0x00: "PRIM",
    0x01: "RGBAQ",
    0x02: "ST",
    0x04: "XYZF2",
    0x05: "XYZ2",
    0x06: "TEX0_1",
    0x07: "TEX0_2",
    0x08: "CLAMP_1",
    0x09: "CLAMP_2",
    0x0D: "XYZ3",
    0x14: "TEX1_1",
    0x15: "TEX1_2",
    0x16: "TEX2_1",
    0x17: "TEX2_2",
    0x18: "XYOFFSET_1",
    0x19: "XYOFFSET_2",
    0x1A: "PRMODECONT",
    0x1B: "PRMODE",
    0x22: "SCISSOR_1",
    0x23: "SCISSOR_2",
    0x34: "ALPHA_1",
    0x35: "ALPHA_2",
    0x3A: "DIMX",
    0x3D: "DTHE",
    0x3F: "COLCLAMP",
    0x40: "TEST_1",
    0x41: "TEST_2",
    0x42: "PABE",
    0x44: "FBA_1",
    0x45: "FRAME_1",
    0x46: "ZBUF_1",
    0x47: "BITBLTBUF",
    0x48: "TRXPOS",
    0x49: "TRXREG",
    0x4A: "TRXDIR",
    0x4C: "HWREG",
    0x61: "SIGNAL",
    0x62: "FINISH",
    0x63: "LABEL",
}

# Draw kick registers (writes that trigger primitive assembly)
DRAW_KICK_REGS = {"XYZ2", "XYZF2"}

# Vertex registers (all XYZ variants)
VERTEX_REGS = {"XYZ2", "XYZF2", "XYZ3", "XYZF3"}

# Texture upload registers
TEXTURE_UPLOAD_REGS = {"BITBLTBUF", "TRXPOS", "TRXREG", "TRXDIR"}


# ─── GIFTag Parsing ───


def parse_giftag(data):
    """Parse a 128-bit GIFTag from 16 bytes.

    Returns dict with fields:
        nloop, eop, pre, prim, flg, nreg, regs, data_size,
        prim_type, prim_iip, prim_tme, prim_fge, prim_abe,
        prim_aa1, prim_fst, prim_ctxt, prim_fix
    """
    lo, hi = struct.unpack_from("<QQ", data, 0)

    nloop = lo & 0x7FFF
    eop = (lo >> 15) & 1
    pre = (lo >> 46) & 1
    prim = (lo >> 47) & 0x7FF
    flg = (lo >> 58) & 3
    nreg_raw = (lo >> 60) & 0xF
    nreg = 16 if nreg_raw == 0 else nreg_raw

    regs = []
    for i in range(nreg):
        regs.append((hi >> (i * 4)) & 0xF)

    # Calculate data size after the tag
    if flg == FLG_PACKED:
        data_size = nloop * nreg * 16
    elif flg == FLG_REGLIST:
        data_size = nloop * nreg * 8
    elif flg == FLG_IMAGE:
        data_size = nloop * 16
    else:
        data_size = 0

    # Parse PRIM field
    prim_type = prim & 0x7
    prim_iip = (prim >> 3) & 1
    prim_tme = (prim >> 4) & 1
    prim_fge = (prim >> 5) & 1
    prim_abe = (prim >> 6) & 1
    prim_aa1 = (prim >> 7) & 1
    prim_fst = (prim >> 8) & 1
    prim_ctxt = (prim >> 9) & 1
    prim_fix = (prim >> 10) & 1

    return {
        'nloop': nloop,
        'eop': eop,
        'pre': pre,
        'prim': prim,
        'flg': flg,
        'nreg': nreg,
        'regs': regs,
        'data_size': data_size,
        'prim_type': prim_type,
        'prim_iip': prim_iip,
        'prim_tme': prim_tme,
        'prim_fge': prim_fge,
        'prim_abe': prim_abe,
        'prim_aa1': prim_aa1,
        'prim_fst': prim_fst,
        'prim_ctxt': prim_ctxt,
        'prim_fix': prim_fix,
    }


# ─── Packet Parsing ───


def parse_packet(data, offset):
    """Parse a single packet from the stream at the given offset.

    Returns dict with type-specific fields and 'total_size' (bytes consumed).
    """
    if offset >= len(data):
        return None

    pkt_type = data[offset]

    if pkt_type == PKT_TRANSFER:
        if offset + 6 > len(data):
            return {'type': pkt_type, 'name': 'Transfer', 'error': 'truncated header',
                    'total_size': len(data) - offset}
        path = data[offset + 1]
        size = struct.unpack_from("<I", data, offset + 2)[0]
        total = 1 + 1 + 4 + size
        return {
            'type': pkt_type,
            'name': 'Transfer',
            'path': path,
            'size': size,
            'data_offset': offset + 6,
            'total_size': total,
        }

    elif pkt_type == PKT_VSYNC:
        if offset + 2 > len(data):
            return {'type': pkt_type, 'name': 'VSync', 'error': 'truncated',
                    'total_size': len(data) - offset}
        field = data[offset + 1]
        return {
            'type': pkt_type,
            'name': 'VSync',
            'field': field,
            'total_size': 2,
        }

    elif pkt_type == PKT_READFIFO2:
        if offset + 5 > len(data):
            return {'type': pkt_type, 'name': 'ReadFIFO2', 'error': 'truncated',
                    'total_size': len(data) - offset}
        size = struct.unpack_from("<I", data, offset + 1)[0]
        return {
            'type': pkt_type,
            'name': 'ReadFIFO2',
            'size': size,
            'total_size': 5,
        }

    elif pkt_type == PKT_REGISTERS:
        total = 1 + 8192
        return {
            'type': pkt_type,
            'name': 'Registers',
            'total_size': total,
        }

    else:
        return {
            'type': pkt_type,
            'name': 'Unknown',
            'error': 'unknown packet type 0x{:02X}'.format(pkt_type),
            'total_size': 1,  # skip 1 byte and try to recover
        }


# ─── Header Parsing ───


def parse_header(data):
    """Parse GS dump header. Returns dict with serial, crc, dimensions, packet_offset."""
    if len(data) < 4:
        return {'format': 'invalid', 'packet_offset': 0}

    magic = struct.unpack_from("<I", data, 0)[0]

    if magic != 0xFFFFFFFF:
        # Legacy format
        return {'format': 'legacy', 'packet_offset': 0, 'serial': '', 'crc': 0,
                'width': 0, 'height': 0}

    if len(data) < 8:
        return {'format': 'invalid', 'packet_offset': 0}

    header_size = struct.unpack_from("<I", data, 4)[0]

    if len(data) < 8 + 36:
        return {'format': 'invalid', 'packet_offset': 0}

    # GSDumpHeader struct at offset 8 (after magic + header_size)
    (state_version, state_size, serial_offset, serial_size,
     crc, width, height, screenshot_offset, screenshot_size) = struct.unpack_from(
        "<IIIIIIIII", data, 8
    )

    # Serial string
    serial_start = 8 + serial_offset
    serial = ''
    if serial_start + serial_size <= len(data):
        serial = data[serial_start:serial_start + serial_size].decode('ascii', errors='replace')

    # Packet stream starts after: magic(4) + header_size_field(4) + header_data(header_size) + state(state_size) + privreg(8192)
    packet_offset = 4 + 4 + header_size + state_size + 8192

    return {
        'format': 'new',
        'state_version': state_version,
        'serial': serial,
        'crc': crc,
        'width': width,
        'height': height,
        'screenshot_size': screenshot_size,
        'state_size': state_size,
        'packet_offset': packet_offset,
    }


# ─── Frame Statistics ───


def new_frame_stats():
    """Create a fresh per-frame statistics dict."""
    return {
        'draw_calls': 0,
        'vertex_count': 0,
        'prim_histogram': collections.Counter(),
        'register_histogram': collections.Counter(),
        'transfer_bytes': collections.defaultdict(int),  # path_id -> bytes
        'texture_uploads': 0,
        'transfer_count': 0,
        'giftag_count': 0,
    }


def finalize_frame_stats(frame):
    """Convert Counters/defaultdicts to plain dicts for JSON serialization."""
    return {
        'draw_calls': frame['draw_calls'],
        'vertex_count': frame['vertex_count'],
        'prim_histogram': dict(frame['prim_histogram']),
        'register_histogram': dict(frame['register_histogram']),
        'transfer_bytes': dict(frame['transfer_bytes']),
        'texture_uploads': frame['texture_uploads'],
        'transfer_count': frame['transfer_count'],
        'giftag_count': frame['giftag_count'],
    }


# ─── GIF Packet Processing ───


def process_transfer_data(data, frame, current_prim_type, verbose=False):
    """Process GIF transfer data, extracting GIFTags and counting register writes.

    Args:
        data: raw transfer data bytes
        frame: current frame stats dict (mutated)
        current_prim_type: list with single element [current_prim_type_name] for A+D tracking
        verbose: print GIFTag details

    Returns:
        list of error strings (empty if no errors)
    """
    errors = []
    offset = 0

    while offset + 16 <= len(data):
        tag = parse_giftag(data[offset:offset + 16])
        frame['giftag_count'] += 1
        offset += 16  # skip past the tag itself

        if verbose:
            reg_names = [GIF_REG_NAMES.get(r, '0x{:X}'.format(r)) for r in tag['regs']]
            print("    GIFTag: NLOOP={} FLG={} NREG={} PRE={} PRIM=0x{:03X} regs={}".format(
                tag['nloop'], tag['flg'], tag['nreg'], tag['pre'], tag['prim'], reg_names))

        # Track PRIM from GIFTag PRE field
        if tag['pre']:
            prim_name = PRIM_TYPES.get(tag['prim_type'], 'Unknown')
            current_prim_type[0] = prim_name

        if tag['flg'] == FLG_PACKED:
            # PACKED mode: NLOOP iterations, each writes NREG registers, 16 bytes per write
            for loop in range(tag['nloop']):
                for reg_idx in range(tag['nreg']):
                    reg_id = tag['regs'][reg_idx]
                    reg_data_offset = offset + (loop * tag['nreg'] + reg_idx) * 16

                    if reg_id == 0x0E:
                        # A+D register: parse the actual target register
                        if reg_data_offset + 16 <= len(data):
                            _process_ad_write(data, reg_data_offset, frame, current_prim_type, verbose)
                        else:
                            errors.append("truncated A+D data at offset {}".format(reg_data_offset))
                    else:
                        reg_name = GIF_REG_NAMES.get(reg_id, 'REG_0x{:X}'.format(reg_id))
                        frame['register_histogram'][reg_name] += 1

                        if reg_name in DRAW_KICK_REGS:
                            frame['draw_calls'] += 1
                            if current_prim_type[0]:
                                frame['prim_histogram'][current_prim_type[0]] += 1

                        if reg_name in VERTEX_REGS:
                            frame['vertex_count'] += 1

            expected = tag['nloop'] * tag['nreg'] * 16
            if offset + expected > len(data):
                errors.append("truncated PACKED data at offset {}: expected {} bytes, {} available".format(
                    offset, expected, len(data) - offset))
                break
            offset += expected

        elif tag['flg'] == FLG_REGLIST:
            # REGLIST mode: NLOOP iterations, NREG registers, 8 bytes per write
            for loop in range(tag['nloop']):
                for reg_idx in range(tag['nreg']):
                    reg_id = tag['regs'][reg_idx]
                    reg_name = GIF_REG_NAMES.get(reg_id, 'REG_0x{:X}'.format(reg_id))
                    frame['register_histogram'][reg_name] += 1

                    if reg_name in DRAW_KICK_REGS:
                        frame['draw_calls'] += 1
                        if current_prim_type[0]:
                            frame['prim_histogram'][current_prim_type[0]] += 1

                    if reg_name in VERTEX_REGS:
                        frame['vertex_count'] += 1

            expected = tag['nloop'] * tag['nreg'] * 8
            if offset + expected > len(data):
                errors.append("truncated REGLIST data at offset {}: expected {} bytes, {} available".format(
                    offset, expected, len(data) - offset))
                break
            offset += expected

        elif tag['flg'] == FLG_IMAGE:
            # IMAGE mode: raw pixel data, no register writes
            expected = tag['nloop'] * 16
            if offset + expected > len(data):
                errors.append("truncated IMAGE data at offset {}: expected {} bytes, {} available".format(
                    offset, expected, len(data) - offset))
                break
            offset += expected

        if tag['eop']:
            break

    return errors


def _process_ad_write(data, offset, frame, current_prim_type, verbose=False):
    """Process a single A+D register write (16 bytes: 64-bit value + 64-bit addr)."""
    value, addr_full = struct.unpack_from("<QQ", data, offset)
    addr = addr_full & 0xFF

    reg_name = AD_REG_NAMES.get(addr, 'AD_0x{:02X}'.format(addr))
    frame['register_histogram'][reg_name] += 1

    if verbose:
        print("      A+D: {} (0x{:02X}) = 0x{:016X}".format(reg_name, addr, value))

    # Draw kick detection
    if reg_name in DRAW_KICK_REGS:
        frame['draw_calls'] += 1
        if current_prim_type[0]:
            frame['prim_histogram'][current_prim_type[0]] += 1

    # Vertex counting
    if reg_name in VERTEX_REGS:
        frame['vertex_count'] += 1

    # PRIM register write — update current primitive type
    if reg_name == 'PRIM':
        prim_type_val = value & 0x7
        current_prim_type[0] = PRIM_TYPES.get(prim_type_val, 'Unknown')

    # Texture upload detection (TRXDIR triggers the upload)
    if reg_name == 'TRXDIR':
        frame['texture_uploads'] += 1


# ─── Main Parser ───


def parse_gs_dump(filepath, verbose=False):
    """Parse a PCSX2 GS dump file and return statistics dict.

    Args:
        filepath: path to .gs dump file
        verbose: print detailed parsing info

    Returns:
        dict with keys: format, serial, crc, width, height, frame_count,
                        frames (list of per-frame stats), total_draw_calls,
                        total_vertices, errors
    """
    with open(filepath, 'rb') as f:
        raw = f.read()

    header = parse_header(raw)
    errors = []

    if header['format'] == 'legacy':
        errors.append("Legacy format detected. Only new format (0xFFFFFFFF magic) is fully supported.")
        return {
            'format': 'legacy',
            'serial': '',
            'crc': 0,
            'width': 0,
            'height': 0,
            'frame_count': 0,
            'frames': [],
            'total_draw_calls': 0,
            'total_vertices': 0,
            'errors': errors,
        }

    if verbose:
        print("Header: format={} serial={} crc=0x{:08X} {}x{}".format(
            header['format'], header['serial'], header['crc'],
            header['width'], header['height']))
        print("Packet stream at offset: {}".format(header['packet_offset']))

    # Parse packet stream
    offset = header['packet_offset']
    frames = []
    current_frame = new_frame_stats()
    current_prim_type = [None]  # mutable container for A+D PRIM tracking

    while offset < len(raw):
        pkt = parse_packet(raw, offset)
        if pkt is None:
            break

        if 'error' in pkt and pkt['name'] == 'Unknown':
            errors.append("offset {}: {}".format(offset, pkt['error']))
            offset += pkt['total_size']
            continue

        if pkt['type'] == PKT_TRANSFER:
            current_frame['transfer_count'] += 1
            current_frame['transfer_bytes'][pkt['path']] += pkt['size']

            # Extract transfer data and process GIFTags
            data_start = pkt['data_offset']
            data_end = data_start + pkt['size']
            if data_end <= len(raw):
                transfer_data = raw[data_start:data_end]
                if verbose:
                    print("  Transfer: path={} size={} bytes".format(pkt['path'], pkt['size']))
                xfer_errors = process_transfer_data(transfer_data, current_frame,
                                                     current_prim_type, verbose)
                errors.extend(xfer_errors)
            else:
                errors.append("offset {}: transfer data extends past EOF".format(offset))

        elif pkt['type'] == PKT_VSYNC:
            if verbose:
                print("  VSync: field={}".format(pkt['field']))
            frames.append(finalize_frame_stats(current_frame))
            current_frame = new_frame_stats()
            current_prim_type = [None]

        elif pkt['type'] == PKT_READFIFO2:
            if verbose:
                print("  ReadFIFO2: size={}".format(pkt['size']))

        elif pkt['type'] == PKT_REGISTERS:
            if verbose:
                print("  Registers: 8192 bytes")

        offset += pkt['total_size']

    # Calculate totals
    total_draw_calls = sum(f['draw_calls'] for f in frames)
    total_vertices = sum(f['vertex_count'] for f in frames)

    return {
        'format': header['format'],
        'serial': header['serial'],
        'crc': header['crc'],
        'width': header['width'],
        'height': header['height'],
        'frame_count': len(frames),
        'frames': frames,
        'total_draw_calls': total_draw_calls,
        'total_vertices': total_vertices,
        'errors': errors if errors else [],
    }


# ─── Output Formatting ───


def format_report(stats):
    """Format statistics as human-readable report string."""
    lines = []
    lines.append("=== GS Dump Analysis ===")
    lines.append("Game: {} (CRC: {:08X})".format(stats['serial'] or 'Unknown', stats['crc']))
    lines.append("Frames: {}".format(stats['frame_count']))
    if stats['width'] and stats['height']:
        lines.append("Resolution: {}x{}".format(stats['width'], stats['height']))
    lines.append("")

    for i, frame in enumerate(stats['frames']):
        lines.append("--- Frame {} ---".format(i + 1))
        lines.append("Draw calls: {:,}".format(frame['draw_calls']))
        lines.append("Vertices: {:,}".format(frame['vertex_count']))

        # Primitive histogram
        if frame['prim_histogram']:
            lines.append("Primitives:")
            total_prims = sum(frame['prim_histogram'].values())
            for prim_name, count in sorted(frame['prim_histogram'].items(),
                                            key=lambda x: -x[1]):
                pct = (count / total_prims * 100) if total_prims > 0 else 0
                lines.append("  {:12s} {:6d} ({:.1f}%)".format(prim_name + ":", count, pct))

        # Transfer sizes
        if frame['transfer_bytes']:
            lines.append("Transfers:")
            for path_id in sorted(frame['transfer_bytes'].keys()):
                size = frame['transfer_bytes'][path_id]
                label = "PATH{}".format(path_id)
                lines.append("  {}: {:,} bytes".format(label, size))

        # Register histogram (top 10)
        if frame['register_histogram']:
            reg_sorted = sorted(frame['register_histogram'].items(), key=lambda x: -x[1])
            total_writes = sum(frame['register_histogram'].values())
            lines.append("Register writes: {:,}".format(total_writes))
            top_regs = reg_sorted[:10]
            top_str = ", ".join("{} ({:,})".format(name, count) for name, count in top_regs)
            lines.append("  Top registers: {}".format(top_str))

        # Texture uploads
        if frame['texture_uploads']:
            lines.append("Texture uploads: {}".format(frame['texture_uploads']))

        lines.append("")

    # Totals
    if stats['frame_count'] > 1:
        lines.append("--- Totals ---")
        lines.append("Total draw calls: {:,}".format(stats['total_draw_calls']))
        lines.append("Total vertices: {:,}".format(stats['total_vertices']))
        if stats['frame_count'] > 0:
            lines.append("Avg draw calls/frame: {:.0f}".format(
                stats['total_draw_calls'] / stats['frame_count']))
            lines.append("Avg vertices/frame: {:.0f}".format(
                stats['total_vertices'] / stats['frame_count']))
        lines.append("")

    if stats['errors']:
        lines.append("--- Errors ({}) ---".format(len(stats['errors'])))
        for err in stats['errors'][:20]:  # cap at 20
            lines.append("  {}".format(err))
        if len(stats['errors']) > 20:
            lines.append("  ... and {} more".format(len(stats['errors']) - 20))

    return "\n".join(lines)


# ─── Test Dump Generator ───


def create_test_dump(filepath):
    """Create a minimal synthetic GS dump for testing.

    Generates a dump with:
    - 1 frame (1 VSync)
    - 3 Transfer packets with various GIFTags
    - Known draw call count for verification
    """
    header = _build_test_header()
    packets = []

    # Packet 1: TriStrip, 5 draw calls via PACKED mode
    # GIFTag: NLOOP=5, PRE=1, PRIM=TriStrip(4), PACKED, NREG=2, regs=[RGBAQ, XYZ2]
    tag1 = _build_test_giftag(nloop=5, eop=1, pre=1, prim=4, flg=0, nreg=2,
                               regs_list=[0x01, 0x05])
    data1 = tag1 + b'\x00' * (5 * 2 * 16)
    packets.append(struct.pack("<BBI", PKT_TRANSFER, 3, len(data1)) + data1)

    # Packet 2: Sprite via A+D writes, 2 draw calls
    tag2 = _build_test_giftag(nloop=4, eop=1, pre=0, prim=0, flg=0, nreg=1,
                               regs_list=[0x0E])
    # A+D: PRIM=Sprite(6)
    ad_prim = struct.pack("<QQ", 6, 0x00)
    # A+D: XYZ2 (draw kick 1)
    ad_xyz1 = struct.pack("<QQ", 0x100, 0x05)
    # A+D: RGBAQ
    ad_rgb = struct.pack("<QQ", 0xFF, 0x01)
    # A+D: XYZ2 (draw kick 2)
    ad_xyz2 = struct.pack("<QQ", 0x200, 0x05)
    data2 = tag2 + ad_prim + ad_xyz1 + ad_rgb + ad_xyz2
    packets.append(struct.pack("<BBI", PKT_TRANSFER, 3, len(data2)) + data2)

    # Packet 3: Texture upload via A+D
    tag3 = _build_test_giftag(nloop=3, eop=1, pre=0, prim=0, flg=0, nreg=1,
                               regs_list=[0x0E])
    ad_blt = struct.pack("<QQ", 0x0, 0x47)   # BITBLTBUF
    ad_trx = struct.pack("<QQ", (64 | (64 << 32)), 0x49)  # TRXREG
    ad_dir = struct.pack("<QQ", 0x0, 0x4A)   # TRXDIR
    data3 = tag3 + ad_blt + ad_trx + ad_dir
    packets.append(struct.pack("<BBI", PKT_TRANSFER, 2, len(data3)) + data3)

    # VSync
    packets.append(struct.pack("<BB", PKT_VSYNC, 0))

    with open(filepath, 'wb') as f:
        f.write(header)
        for pkt in packets:
            f.write(pkt)


def _build_test_header():
    """Build a header for the test dump."""
    serial = b"SLUS-20565"
    crc = 0x12345678
    width = 512
    height = 448
    serial_size = len(serial)
    screenshot_size = width * height * 4
    serial_offset = 36
    screenshot_offset = serial_offset + serial_size
    state_size = 128

    header_struct = struct.pack("<IIIIIIIII",
        9, state_size, serial_offset, serial_size, crc,
        width, height, screenshot_offset, screenshot_size)

    header_size = len(header_struct) + serial_size + screenshot_size

    buf = bytearray()
    buf += struct.pack("<I", 0xFFFFFFFF)
    buf += struct.pack("<I", header_size)
    buf += header_struct
    buf += serial
    buf += b'\x00' * screenshot_size
    buf += b'\x00' * state_size
    buf += b'\x00' * 8192
    return bytes(buf)


def _build_test_giftag(nloop, eop, pre, prim, flg, nreg, regs_list):
    """Build a GIFTag for test dump generation."""
    lo = nloop & 0x7FFF
    lo |= (eop & 1) << 15
    lo |= (pre & 1) << 46
    lo |= (prim & 0x7FF) << 47
    lo |= (flg & 3) << 58
    lo |= (nreg & 0xF) << 60

    hi = 0
    for i, reg in enumerate(regs_list):
        hi |= (reg & 0xF) << (i * 4)

    return struct.pack("<QQ", lo, hi)


# ─── CLI Entry Point ───


def main():
    parser = argparse.ArgumentParser(
        description="Parse PCSX2 GS dump files and extract rendering statistics.",
        epilog="Examples:\n"
               "  %(prog)s dump.gs                  Human-readable report\n"
               "  %(prog)s dump.gs --json            JSON to stdout\n"
               "  %(prog)s dump.gs -o stats.json     JSON to file\n"
               "  %(prog)s --create-test-dump test.gs Create synthetic dump",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("dump", nargs="?", help="Path to .gs dump file")
    parser.add_argument("--json", action="store_true", help="Output JSON instead of human-readable")
    parser.add_argument("-o", "--output", help="Write JSON output to file")
    parser.add_argument("-v", "--verbose", action="store_true", help="Print every GIFTag parsed")
    parser.add_argument("--create-test-dump", metavar="PATH",
                        help="Create a minimal synthetic GS dump for testing")

    args = parser.parse_args()

    if args.create_test_dump:
        create_test_dump(args.create_test_dump)
        print("Created test dump: {}".format(args.create_test_dump))
        return

    if not args.dump:
        parser.error("dump file path required (or use --create-test-dump)")

    if not os.path.isfile(args.dump):
        print("Error: file not found: {}".format(args.dump), file=sys.stderr)
        sys.exit(1)

    stats = parse_gs_dump(args.dump, verbose=args.verbose)

    if args.output:
        with open(args.output, 'w') as f:
            json.dump(stats, f, indent=2)
        print("Wrote JSON to: {}".format(args.output))
    elif args.json:
        print(json.dumps(stats, indent=2))
    else:
        print(format_report(stats))


if __name__ == '__main__':
    main()
