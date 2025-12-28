#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

missing=0
python_ok=1

check_cmd() {
  local cmd="$1"
  if ! command -v "$cmd" >/dev/null 2>&1; then
    echo "missing command: $cmd"
    missing=1
    if [ "$cmd" = "python3" ]; then
      python_ok=0
    fi
  fi
}

check_path() {
  local path="$1"
  if [ ! -s "$path" ]; then
    echo "missing or empty: $path"
    missing=1
  fi
}

check_cmd python3
check_cmd ping

check_path "docs/lab-topology.yml"
check_path "scripts/generate_inventory.py"
check_path "labs/day-01-foundations/examples/connectivity.py"

if [ $python_ok -eq 1 ] && ! python3 - <<'PY'
import sys

version = sys.version_info[:2]
if version < (3, 10):
    print(f"python3 >= 3.10 required, found {sys.version.split()[0]}")
    raise SystemExit(1)
print(f"python ok: {sys.version.split()[0]}")
PY
then
  missing=1
fi

if [ $missing -eq 0 ]; then
  echo "sanity ok"
else
  echo "sanity failed"
fi
