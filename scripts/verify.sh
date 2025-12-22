#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT_DIR"

missing=0

check_path() {
  local path="$1"
  if [ ! -e "$path" ]; then
    echo "missing: $path"
    missing=1
  fi
}

check_path "docs/syllabus.md"
check_path "labs/day-01-foundations/README.md"
check_path "labs/day-02-observability/README.md"
check_path "labs/day-03-apis-data/README.md"
check_path "labs/day-04-automation/README.md"
check_path "labs/day-05-capstone/README.md"

if [ $missing -eq 0 ]; then
  echo "verify ok"
else
  echo "verify failed"
fi
