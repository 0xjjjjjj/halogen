"""Tests for tools/parse-gs-dump.py — PCSX2 GS dump parser.

Uses synthetic GS dumps built from known binary structures to validate
parsing logic without requiring real PCSX2 captures.
"""

import importlib.util
import json
import struct
import sys
import tempfile
import os
from pathlib import Path
from io import BytesIO

import pytest

# Import the module from tools/ path
TOOLS_DIR = Path(__file__).parent.parent / "tools"
spec = importlib.util.spec_from_file_location("parse_gs_dump", TOOLS_DIR / "parse-gs-dump.py")
parse_gs_dump = importlib.util.module_from_spec(spec)
spec.loader.exec_module(parse_gs_dump)


# ─── Helper: Build binary structures ───


def build_giftag(nloop, eop, pre, prim, flg, nreg, regs_list):
    """Build a 128-bit (16 byte) GIFTag.

    Args:
        nloop: 15-bit loop count
        eop: 1-bit end of packet
        pre: 1-bit PRIM field enable
        prim: 11-bit PRIM register value
        flg: 2-bit format (0=PACKED, 1=REGLIST, 2=IMAGE)
        nreg: 4-bit register count (0 means 16)
        regs_list: list of 4-bit register IDs (up to 16)
    Returns:
        16 bytes
    """
    # Lower 64 bits: NLOOP[14:0] | EOP[15] | pad[45:16] | PRE[46] | PRIM[57:47] | FLG[59:58] | NREG[63:60]
    lo = nloop & 0x7FFF
    lo |= (eop & 1) << 15
    # bits 16-45 = pad (0)
    lo |= (pre & 1) << 46
    lo |= (prim & 0x7FF) << 47
    lo |= (flg & 3) << 58
    lo |= (nreg & 0xF) << 60

    # Upper 64 bits: 16 x 4-bit register descriptors
    hi = 0
    for i, reg in enumerate(regs_list):
        hi |= (reg & 0xF) << (i * 4)

    return struct.pack("<QQ", lo, hi)


def build_gs_header(serial=b"SLUS-20565", crc=0xAABBCCDD, width=512, height=448):
    """Build a new-format GS dump header (magic + header struct + serial + screenshot + state + privreg)."""
    serial_size = len(serial)
    screenshot_size = width * height * 4
    serial_offset = 36  # sizeof GSDumpHeader
    screenshot_offset = serial_offset + serial_size
    state_size = 128  # minimal fake GS state

    # GSDumpHeader struct (36 bytes, packed)
    header_struct = struct.pack("<IIIIIIIII",
        9,                   # state_version
        state_size,          # state_size
        serial_offset,       # serial_offset (always 36)
        serial_size,         # serial_size
        crc,                 # crc
        width,               # screenshot_width
        height,              # screenshot_height
        screenshot_offset,   # screenshot_offset
        screenshot_size,     # screenshot_size
    )

    header_size = len(header_struct) + serial_size + screenshot_size

    buf = bytearray()
    # Magic
    buf += struct.pack("<I", 0xFFFFFFFF)
    # Header size
    buf += struct.pack("<I", header_size)
    # Header struct
    buf += header_struct
    # Serial
    buf += serial
    # Screenshot (zeroes)
    buf += b'\x00' * screenshot_size
    # GS state data (zeroes, state_size bytes)
    buf += b'\x00' * state_size
    # GSPrivRegSet (8192 bytes)
    buf += b'\x00' * 8192

    return bytes(buf)


def build_transfer_packet(path_id, data):
    """Build a Transfer packet: [0x00][path:u8][size:u32LE][data]."""
    return struct.pack("<BBI", 0x00, path_id, len(data)) + data


def build_vsync_packet(field=0):
    """Build a VSync packet: [0x01][field:u8]."""
    return struct.pack("<BB", 0x01, field)


def build_registers_packet():
    """Build a Registers packet: [0x03][8192 bytes]."""
    return struct.pack("<B", 0x03) + b'\x00' * 8192


def build_readfifo2_packet(size=16):
    """Build a ReadFIFO2 packet: [0x02][size:u32LE]."""
    return struct.pack("<BI", 0x02, size)


def build_ad_data(value, addr):
    """Build 16-byte A+D register data: 64-bit value + 64-bit where low 8 bits = addr."""
    return struct.pack("<QQ", value, addr & 0xFF)


def build_minimal_dump(packets):
    """Build a complete GS dump with header + packet stream."""
    header = build_gs_header()
    return header + b''.join(packets)


def write_dump_to_file(data):
    """Write binary data to a temp file and return the path."""
    fd, path = tempfile.mkstemp(suffix=".gs")
    os.write(fd, data)
    os.close(fd)
    return path


# ─── Tests ───


class TestGIFTagParsing:
    """Test GIFTag parsing from 128-bit binary data."""

    def test_packed_giftag_basic(self):
        """Parse a PACKED GIFTag with NLOOP=1, NREG=1, register=RGBAQ."""
        tag_bytes = build_giftag(nloop=1, eop=1, pre=1, prim=0x04, flg=0, nreg=1, regs_list=[0x01])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['nloop'] == 1
        assert tag['eop'] == 1
        assert tag['pre'] == 1
        assert tag['prim'] == 0x04
        assert tag['flg'] == 0
        assert tag['nreg'] == 1
        assert tag['regs'] == [0x01]

    def test_nreg_zero_means_16(self):
        """NREG=0 in GIFTag means 16 registers."""
        regs = list(range(16))
        tag_bytes = build_giftag(nloop=1, eop=1, pre=0, prim=0, flg=0, nreg=0, regs_list=regs)
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['nreg'] == 16
        assert len(tag['regs']) == 16

    def test_packed_data_size(self):
        """PACKED mode: data = NLOOP * NREG * 16 bytes."""
        tag_bytes = build_giftag(nloop=3, eop=0, pre=0, prim=0, flg=0, nreg=2, regs_list=[0x01, 0x05])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['data_size'] == 3 * 2 * 16  # 96 bytes

    def test_reglist_data_size(self):
        """REGLIST mode: data = NLOOP * NREG * 8 bytes."""
        tag_bytes = build_giftag(nloop=4, eop=0, pre=0, prim=0, flg=1, nreg=3, regs_list=[0x01, 0x02, 0x05])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['data_size'] == 4 * 3 * 8  # 96 bytes

    def test_image_data_size(self):
        """IMAGE mode: data = NLOOP * 16 bytes."""
        tag_bytes = build_giftag(nloop=10, eop=0, pre=0, prim=0, flg=2, nreg=0, regs_list=[])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['data_size'] == 10 * 16  # 160 bytes

    def test_prim_type_extraction(self):
        """PRIM bits [2:0] define the primitive type."""
        # TriStrip = 4
        tag_bytes = build_giftag(nloop=1, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['prim_type'] == 4  # TriStrip

    def test_prim_flags(self):
        """PRIM register flags: IIP, TME, FGE, ABE, etc."""
        # prim = 0b00011011_100 = type=4(TriStrip) | IIP=1 | TME=1 | FGE=0 | ABE=1
        prim_val = 4 | (1 << 3) | (1 << 4) | (0 << 5) | (1 << 6)
        tag_bytes = build_giftag(nloop=1, eop=1, pre=1, prim=prim_val, flg=0, nreg=1, regs_list=[0x05])
        tag = parse_gs_dump.parse_giftag(tag_bytes)
        assert tag['prim_type'] == 4   # TriStrip
        assert tag['prim_iip'] == 1    # Gouraud
        assert tag['prim_tme'] == 1    # Texture
        assert tag['prim_fge'] == 0    # No fog
        assert tag['prim_abe'] == 1    # Alpha blend


class TestPacketParsing:
    """Test individual packet type parsing."""

    def test_transfer_packet(self):
        """Parse Transfer packet: type 0, path ID, size, data."""
        data = b'\xAA' * 64
        pkt = build_transfer_packet(path_id=3, data=data)
        result = parse_gs_dump.parse_packet(pkt, 0)
        assert result['type'] == 0
        assert result['name'] == 'Transfer'
        assert result['path'] == 3
        assert result['size'] == 64
        assert result['total_size'] == 1 + 1 + 4 + 64  # type + path + size_field + data

    def test_vsync_packet(self):
        """Parse VSync packet: type 1, field byte."""
        pkt = build_vsync_packet(field=1)
        result = parse_gs_dump.parse_packet(pkt, 0)
        assert result['type'] == 1
        assert result['name'] == 'VSync'
        assert result['field'] == 1
        assert result['total_size'] == 2

    def test_readfifo2_packet(self):
        """Parse ReadFIFO2 packet: type 2, size."""
        pkt = build_readfifo2_packet(size=32)
        result = parse_gs_dump.parse_packet(pkt, 0)
        assert result['type'] == 2
        assert result['name'] == 'ReadFIFO2'
        assert result['size'] == 32
        assert result['total_size'] == 5

    def test_registers_packet(self):
        """Parse Registers packet: type 3, 8192 bytes."""
        pkt = build_registers_packet()
        result = parse_gs_dump.parse_packet(pkt, 0)
        assert result['type'] == 3
        assert result['name'] == 'Registers'
        assert result['total_size'] == 1 + 8192


class TestHeaderParsing:
    """Test GS dump header parsing."""

    def test_new_format_magic(self):
        """Detect new format via 0xFFFFFFFF magic."""
        header_data = build_gs_header(serial=b"SLUS-20565", crc=0xAABBCCDD)
        result = parse_gs_dump.parse_header(header_data)
        assert result['format'] == 'new'
        assert result['serial'] == 'SLUS-20565'
        assert result['crc'] == 0xAABBCCDD
        assert result['width'] == 512
        assert result['height'] == 448

    def test_legacy_format_detection(self):
        """First 4 bytes != 0xFFFFFFFF means legacy format."""
        # Legacy format: state_version is a small number (e.g., 9)
        legacy_data = struct.pack("<I", 9) + b'\x00' * 100
        result = parse_gs_dump.parse_header(legacy_data)
        assert result['format'] == 'legacy'

    def test_header_packet_offset(self):
        """Header parsing returns correct offset where packet stream begins."""
        header_data = build_gs_header()
        result = parse_gs_dump.parse_header(header_data)
        # The packet stream starts after header + state_data + GSPrivRegSet
        assert result['packet_offset'] > 0
        assert isinstance(result['packet_offset'], int)


class TestDrawCallCounting:
    """Test draw call detection from register writes."""

    def test_xyz2_in_packed_giftag(self):
        """XYZ2 (0x05) in GIFTag REGS triggers a draw kick per NLOOP."""
        # GIFTag: NLOOP=5, PACKED, NREG=2, regs=[RGBAQ, XYZ2]
        # PRE=1, PRIM=TriStrip(4)
        tag = build_giftag(nloop=5, eop=1, pre=1, prim=4, flg=0, nreg=2, regs_list=[0x01, 0x05])
        # Data: 5 loops * 2 regs * 16 bytes = 160 bytes
        data = tag + b'\x00' * (5 * 2 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            # 5 draw kicks (one per NLOOP iteration writing XYZ2)
            assert stats['frames'][0]['draw_calls'] == 5
        finally:
            os.unlink(path)

    def test_xyzf2_in_packed_giftag(self):
        """XYZF2 (0x04) also triggers draw kicks."""
        tag = build_giftag(nloop=3, eop=1, pre=1, prim=3, flg=0, nreg=1, regs_list=[0x04])
        data = tag + b'\x00' * (3 * 1 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['draw_calls'] == 3
        finally:
            os.unlink(path)

    def test_ad_xyz2_write(self):
        """A+D (0x0E) write to XYZ2 address (0x05) counts as draw kick."""
        # GIFTag: NLOOP=1, PACKED, NREG=1, regs=[A+D]
        tag = build_giftag(nloop=1, eop=1, pre=0, prim=0, flg=0, nreg=1, regs_list=[0x0E])
        # A+D data: 64-bit value + 64-bit addr (low byte = 0x05 = XYZ2)
        ad_data = build_ad_data(value=0x1234, addr=0x05)
        data = tag + ad_data
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['draw_calls'] == 1
        finally:
            os.unlink(path)

    def test_xyz3_not_draw_kick(self):
        """XYZ3 (0x0D) and XYZF3 (0x0C) are vertex writes but NOT draw kicks."""
        tag = build_giftag(nloop=2, eop=1, pre=1, prim=3, flg=0, nreg=1, regs_list=[0x0D])
        data = tag + b'\x00' * (2 * 1 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['draw_calls'] == 0
        finally:
            os.unlink(path)


class TestPrimitiveHistogram:
    """Test primitive type counting."""

    def test_prim_from_giftag_pre(self):
        """PRIM type from GIFTag PRE=1 field."""
        # TriStrip packets
        tag1 = build_giftag(nloop=1, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        data1 = tag1 + b'\x00' * 16
        # Sprite packets
        tag2 = build_giftag(nloop=1, eop=1, pre=1, prim=6, flg=0, nreg=1, regs_list=[0x05])
        data2 = tag2 + b'\x00' * 16

        pkt1 = build_transfer_packet(path_id=3, data=data1)
        pkt2 = build_transfer_packet(path_id=3, data=data2)
        dump = build_minimal_dump([pkt1, pkt2, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            hist = stats['frames'][0]['prim_histogram']
            assert hist.get('TriStrip', 0) >= 1
            assert hist.get('Sprite', 0) >= 1
        finally:
            os.unlink(path)

    def test_prim_from_ad_write(self):
        """PRIM type from A+D write to register 0x00 (PRIM)."""
        # A+D write: PRIM register, value = Tri(3)
        tag = build_giftag(nloop=2, eop=1, pre=0, prim=0, flg=0, nreg=1, regs_list=[0x0E])
        # First A+D: set PRIM to Tri(3)
        ad_prim = build_ad_data(value=3, addr=0x00)
        # Second A+D: write XYZ2 (draw kick)
        ad_xyz2 = build_ad_data(value=0x1234, addr=0x05)
        data = tag + ad_prim + ad_xyz2
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            hist = stats['frames'][0]['prim_histogram']
            assert hist.get('Tri', 0) >= 1
        finally:
            os.unlink(path)


class TestVertexCounting:
    """Test vertex count tracking."""

    def test_vertex_count_xyz2(self):
        """XYZ2 writes count as vertices."""
        tag = build_giftag(nloop=10, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        data = tag + b'\x00' * (10 * 1 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['vertex_count'] >= 10
        finally:
            os.unlink(path)

    def test_vertex_count_includes_xyz3(self):
        """XYZ3 writes are also vertices (just without draw kick)."""
        tag = build_giftag(nloop=5, eop=1, pre=1, prim=4, flg=0, nreg=2, regs_list=[0x05, 0x0D])
        data = tag + b'\x00' * (5 * 2 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            # 5 XYZ2 + 5 XYZ3 = 10 vertices
            assert stats['frames'][0]['vertex_count'] >= 10
        finally:
            os.unlink(path)


class TestTransferStats:
    """Test per-path transfer size tracking."""

    def test_path3_transfer_size(self):
        """PATH3 transfer bytes tracked correctly."""
        data = b'\xAA' * 256
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['transfer_bytes'][3] == 256
        finally:
            os.unlink(path)

    def test_multiple_paths(self):
        """Transfers on different paths tracked separately."""
        pkt1 = build_transfer_packet(path_id=1, data=b'\x00' * 100)
        pkt2 = build_transfer_packet(path_id=2, data=b'\x00' * 200)
        pkt3 = build_transfer_packet(path_id=3, data=b'\x00' * 300)
        dump = build_minimal_dump([pkt1, pkt2, pkt3, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            frame = stats['frames'][0]
            assert frame['transfer_bytes'][1] == 100
            assert frame['transfer_bytes'][2] == 200
            assert frame['transfer_bytes'][3] == 300
        finally:
            os.unlink(path)


class TestTextureUploadDetection:
    """Test texture upload detection via BITBLTBUF/TRXDIR A+D writes."""

    def test_texture_upload_sequence(self):
        """A+D writes to BITBLTBUF(0x47) + TRXREG(0x49) + TRXDIR(0x4A) = texture upload."""
        tag = build_giftag(nloop=3, eop=1, pre=0, prim=0, flg=0, nreg=1, regs_list=[0x0E])
        # BITBLTBUF
        ad1 = build_ad_data(value=0x0, addr=0x47)
        # TRXREG (width=64, height=64 packed)
        ad2 = build_ad_data(value=(64 | (64 << 32)), addr=0x49)
        # TRXDIR (0 = host-to-local upload)
        ad3 = build_ad_data(value=0x0, addr=0x4A)
        data = tag + ad1 + ad2 + ad3
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['texture_uploads'] >= 1
        finally:
            os.unlink(path)


class TestFrameCounting:
    """Test frame boundary detection via VSync packets."""

    def test_single_frame(self):
        """One VSync = one frame."""
        dump = build_minimal_dump([build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frame_count'] == 1
        finally:
            os.unlink(path)

    def test_multiple_frames(self):
        """Multiple VSyncs = multiple frames."""
        packets = []
        for _ in range(5):
            tag = build_giftag(nloop=1, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
            data = tag + b'\x00' * 16
            packets.append(build_transfer_packet(path_id=3, data=data))
            packets.append(build_vsync_packet())
        dump = build_minimal_dump(packets)
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frame_count'] == 5
            assert len(stats['frames']) == 5
        finally:
            os.unlink(path)

    def test_per_frame_stats_independent(self):
        """Each frame has independent draw call counts."""
        packets = []
        # Frame 1: 3 draw calls
        tag1 = build_giftag(nloop=3, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        data1 = tag1 + b'\x00' * (3 * 16)
        packets.append(build_transfer_packet(path_id=3, data=data1))
        packets.append(build_vsync_packet())
        # Frame 2: 7 draw calls
        tag2 = build_giftag(nloop=7, eop=1, pre=1, prim=6, flg=0, nreg=1, regs_list=[0x05])
        data2 = tag2 + b'\x00' * (7 * 16)
        packets.append(build_transfer_packet(path_id=3, data=data2))
        packets.append(build_vsync_packet())

        dump = build_minimal_dump(packets)
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['draw_calls'] == 3
            assert stats['frames'][1]['draw_calls'] == 7
        finally:
            os.unlink(path)


class TestRegisterHistogram:
    """Test GS register write frequency tracking."""

    def test_register_write_counts(self):
        """Track all register writes from GIFTag REGS."""
        # NLOOP=4, NREG=3, regs=[RGBAQ, ST, XYZ2]
        tag = build_giftag(nloop=4, eop=1, pre=1, prim=4, flg=0, nreg=3, regs_list=[0x01, 0x02, 0x05])
        data = tag + b'\x00' * (4 * 3 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            reg_hist = stats['frames'][0]['register_histogram']
            assert reg_hist.get('RGBAQ', 0) == 4
            assert reg_hist.get('ST', 0) == 4
            assert reg_hist.get('XYZ2', 0) == 4
        finally:
            os.unlink(path)

    def test_ad_register_writes(self):
        """A+D writes tracked by resolved register address."""
        tag = build_giftag(nloop=2, eop=1, pre=0, prim=0, flg=0, nreg=1, regs_list=[0x0E])
        ad1 = build_ad_data(value=0, addr=0x06)  # TEX0_1
        ad2 = build_ad_data(value=0, addr=0x45)  # FRAME_1
        data = tag + ad1 + ad2
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            reg_hist = stats['frames'][0]['register_histogram']
            assert reg_hist.get('TEX0_1', 0) == 1
            assert reg_hist.get('FRAME_1', 0) == 1
        finally:
            os.unlink(path)


class TestReglistMode:
    """Test REGLIST GIFTag mode parsing."""

    def test_reglist_register_counts(self):
        """REGLIST mode: NLOOP * NREG writes, 8 bytes each."""
        # REGLIST: NLOOP=2, NREG=2, regs=[RGBAQ, XYZ2]
        tag = build_giftag(nloop=2, eop=1, pre=1, prim=4, flg=1, nreg=2, regs_list=[0x01, 0x05])
        data = tag + b'\x00' * (2 * 2 * 8)  # 32 bytes of register data
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frames'][0]['draw_calls'] == 2  # 2 XYZ2 writes
            reg_hist = stats['frames'][0]['register_histogram']
            assert reg_hist.get('RGBAQ', 0) == 2
            assert reg_hist.get('XYZ2', 0) == 2
        finally:
            os.unlink(path)


class TestImageMode:
    """Test IMAGE GIFTag mode (texture upload data)."""

    def test_image_no_register_writes(self):
        """IMAGE mode has no register writes, just raw pixel data."""
        tag = build_giftag(nloop=8, eop=1, pre=0, prim=0, flg=2, nreg=0, regs_list=[])
        data = tag + b'\x00' * (8 * 16)  # 128 bytes image data
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            # No register writes from IMAGE mode
            assert stats['frames'][0]['draw_calls'] == 0
        finally:
            os.unlink(path)


class TestOutputFormats:
    """Test JSON and human-readable output generation."""

    def test_json_output_structure(self):
        """JSON output has required top-level keys."""
        dump = build_minimal_dump([build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert 'serial' in stats
            assert 'crc' in stats
            assert 'frame_count' in stats
            assert 'frames' in stats
            assert 'width' in stats
            assert 'height' in stats
        finally:
            os.unlink(path)

    def test_json_serializable(self):
        """Stats dict is JSON-serializable."""
        tag = build_giftag(nloop=2, eop=1, pre=1, prim=4, flg=0, nreg=2, regs_list=[0x01, 0x05])
        data = tag + b'\x00' * (2 * 2 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            json_str = json.dumps(stats)
            parsed = json.loads(json_str)
            assert parsed['frame_count'] == 1
        finally:
            os.unlink(path)

    def test_human_readable_output(self):
        """Human-readable formatter produces non-empty string with key sections."""
        tag = build_giftag(nloop=5, eop=1, pre=1, prim=4, flg=0, nreg=2, regs_list=[0x01, 0x05])
        data = tag + b'\x00' * (5 * 2 * 16)
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            report = parse_gs_dump.format_report(stats)
            assert 'GS Dump Analysis' in report
            assert 'Draw calls' in report
            assert 'Frame' in report
        finally:
            os.unlink(path)


class TestCreateTestDump:
    """Test the --create-test-dump flag."""

    def test_create_test_dump(self):
        """--create-test-dump creates a parseable GS dump file."""
        fd, path = tempfile.mkstemp(suffix=".gs")
        os.close(fd)
        try:
            parse_gs_dump.create_test_dump(path)
            # Parse the generated dump
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frame_count'] >= 1
            assert stats['frames'][0]['draw_calls'] > 0
        finally:
            os.unlink(path)


class TestErrorHandling:
    """Test robustness against malformed data."""

    def test_truncated_transfer_packet(self):
        """Truncated transfer data reported but parsing continues."""
        tag = build_giftag(nloop=10, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        # Only provide partial data (should be 10*16=160, give 32)
        data = tag + b'\x00' * 32
        pkt = build_transfer_packet(path_id=3, data=data)
        dump = build_minimal_dump([pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            # Should still produce stats (possibly partial)
            assert stats['frame_count'] == 1
            assert 'errors' in stats or stats['frames'][0]['draw_calls'] >= 0
        finally:
            os.unlink(path)

    def test_empty_dump_after_header(self):
        """Empty packet stream (just header) produces zero frames."""
        header = build_gs_header()
        path = write_dump_to_file(header)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['frame_count'] == 0
        finally:
            os.unlink(path)

    def test_unknown_packet_type(self):
        """Unknown packet type byte reported and skipped."""
        # Packet type 0xFF is invalid
        bad_pkt = struct.pack("<B", 0xFF)
        dump = build_minimal_dump([bad_pkt, build_vsync_packet()])
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            # Should have recorded an error but still counted the vsync
            assert stats['frame_count'] >= 0
            assert len(stats.get('errors', [])) > 0
        finally:
            os.unlink(path)


class TestTotalStats:
    """Test aggregate statistics across all frames."""

    def test_total_draw_calls(self):
        """Total draw calls summed across frames."""
        packets = []
        # Frame 1: 3 draw calls
        tag1 = build_giftag(nloop=3, eop=1, pre=1, prim=4, flg=0, nreg=1, regs_list=[0x05])
        packets.append(build_transfer_packet(path_id=3, data=tag1 + b'\x00' * (3 * 16)))
        packets.append(build_vsync_packet())
        # Frame 2: 2 draw calls
        tag2 = build_giftag(nloop=2, eop=1, pre=1, prim=6, flg=0, nreg=1, regs_list=[0x05])
        packets.append(build_transfer_packet(path_id=3, data=tag2 + b'\x00' * (2 * 16)))
        packets.append(build_vsync_packet())

        dump = build_minimal_dump(packets)
        path = write_dump_to_file(dump)
        try:
            stats = parse_gs_dump.parse_gs_dump(path)
            assert stats['total_draw_calls'] == 5
            assert stats['total_vertices'] >= 5
        finally:
            os.unlink(path)
