# Ghidra + ghidra-emotionengine-reloaded Setup

## Current State (2026-02-20)

- **Java:** Not installed. Need Java 17+ (OpenJDK recommended).
- **Ghidra:** Not installed. Need to download from https://ghidra-sre.org/
- **Extension:** Cloned to `vendor/ghidra-emotionengine-reloaded/`
- **Extension version:** Supports Ghidra 12.0.3

## Setup Steps

### 1. Install Java 17+

```bash
sudo apt install openjdk-17-jdk
java -version  # verify
```

### 2. Install Ghidra

```bash
# Download latest from https://ghidra-sre.org/
# As of 2026-02, latest is Ghidra 12.0.x
wget https://github.com/NationalSecurityAgency/ghidra/releases/download/Ghidra_12.0.3_build/ghidra_12.0.3_PUBLIC_20250210.zip
unzip ghidra_12.0.3_PUBLIC_20250210.zip -d /opt/
ln -s /opt/ghidra_12.0.3_PUBLIC/ghidraRun /usr/local/bin/ghidraRun
```

### 3. Install ghidra-emotionengine-reloaded

**Option A: Pre-built release (recommended)**

Download from: https://github.com/chaoticgd/ghidra-emotionengine-reloaded/releases

Install via Ghidra: File → Install Extensions → select .zip

**Option B: Build from source**

```bash
cd vendor/ghidra-emotionengine-reloaded
# Requires gradle
gradle -PGHIDRA_INSTALL_DIR=/opt/ghidra_12.0.3_PUBLIC buildExtension
# Output: dist/ghidra_12.0.3_PUBLIC_*.zip
```

### 4. Loading a PS2 ELF

1. File → Import File → select BASLUS_20565.ELF
2. Format: ELF
3. Language: MIPS R5900 (provided by extension)
4. Let auto-analysis run (takes a few minutes)
5. Check Window → Symbol Table for debug symbols

### Tips from extension README

- If decompilation fails: disable "Decompiler Parameter ID" analyzer
- If symbols aren't demangled: enable "Use Deprecated Demangler" in Demangler GNU settings
- PCSX2 save states: use Deflate64 compression (not zstd) for Ghidra compatibility

## Features We'll Use

- `.mdebug` section recovery → original function/variable names
- EE-specific instruction sets (MMI, VU0 macro mode)
- PCSX2 save state import for runtime cross-referencing
- MIPS-R5900 Constant Reference Analyzer for global variable tracking
