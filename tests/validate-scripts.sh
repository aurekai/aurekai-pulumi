#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "$0")/.." && pwd)"
PASS=0; FAIL=0

for f in "$ROOT/__main__.py"; do
  if python3 -m py_compile "$f" 2>/dev/null; then
    echo "  v $(basename "$f")"; PASS=$((PASS+1))
  else
    echo "  x $(basename "$f")"; FAIL=$((FAIL+1))
  fi
done

for f in "$ROOT/Pulumi.yaml" "$ROOT/Pulumi.dev.yaml"; do
  if python3 -c "import yaml,sys; yaml.safe_load(open(sys.argv[1]))" "$f" 2>/dev/null; then
    echo "  v $(basename "$f")"; PASS=$((PASS+1))
  else
    echo "  x $(basename "$f")"; FAIL=$((FAIL+1))
  fi
done

echo; echo "Pulumi files: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ]
