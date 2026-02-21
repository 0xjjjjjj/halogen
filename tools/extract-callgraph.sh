#!/bin/bash
# Extract call graph from PS2Recomp output using ast-grep
# Usage: ./extract-callgraph.sh <class-pattern> [recomp-dir]
#
# Examples:
#   ./extract-callgraph.sh VIAtmosphere
#   ./extract-callgraph.sh VIRaster /path/to/recomp/output
#   ./extract-callgraph.sh 'VIH\?Sprite'  # glob pattern

set -euo pipefail

PATTERN="${1:?Usage: extract-callgraph.sh <class-pattern> [recomp-dir]}"
RECOMP_DIR="${2:-output/champions-of-norrath}"

if ! command -v ast-grep &>/dev/null; then
    echo "ERROR: ast-grep not found. Install with: npm install -g @ast-grep/cli" >&2
    exit 1
fi

echo "# Call Graph: $PATTERN"
echo "# Source: $RECOMP_DIR"
echo "# Generated: $(date -Iseconds)"
echo ""

for f in "$RECOMP_DIR"/*"$PATTERN"*.cpp; do
    [ -f "$f" ] || continue
    caller=$(basename "$f" | sed 's/_0x[0-9a-f]*\.cpp//')
    callees=$(ast-grep --lang cpp --pattern '$FUNC(rdram, ctx, runtime)' "$f" 2>/dev/null \
        | grep -oP '\s+(\w+__\w+|\w+_0x[0-9a-f]+)\(' \
        | grep -oP '\w+' \
        | sort -u)
    if [ -n "$callees" ]; then
        echo "=== $caller ==="
        echo "$callees"
        echo ""
    fi
done
