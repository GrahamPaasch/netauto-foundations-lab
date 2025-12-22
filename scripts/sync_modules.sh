#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
MODULES_DIR="$ROOT_DIR/modules"
LAB_HUB="${LAB_HUB:-$ROOT_DIR/../autocon4-lab}"

mkdir -p "$MODULES_DIR"

link_from_hub() {
  local name="$1"
  local src="$LAB_HUB/modules/$name"
  local dest="$MODULES_DIR/$name"

  if [ -e "$dest" ]; then
    return 0
  fi

  if [ -e "$src" ]; then
    ln -s "$src" "$dest"
    echo "linked: $name"
  fi
}

clone_if_missing() {
  local name="$1"
  local url="$2"
  local dest="$MODULES_DIR/$name"

  if [ -e "$dest" ]; then
    return 0
  fi

  git clone "$url" "$dest"
  echo "cloned: $name"
}

# Try to link from lab hub first
if [ -d "$LAB_HUB/modules" ]; then
  link_from_hub netintent-ops
  link_from_hub day4-teaching-kit-v2
  link_from_hub gan_clean
  link_from_hub grahams_automated_network
  link_from_hub introduction_to_python_for_networking_five_day_course
  link_from_hub netauto-course
  link_from_hub netauto-course-day3
  link_from_hub automate_your_network
  link_from_hub ml4nce
fi

# Clone anything still missing
clone_if_missing netintent-ops https://github.com/GrahamPaasch/netintent-ops.git
clone_if_missing grahams_automated_network https://github.com/GrahamPaasch/grahams_automated_network.git
clone_if_missing introduction_to_python_for_networking_five_day_course \
  https://github.com/GrahamPaasch/introduction_to_python_for_networking_five_day_course.git
clone_if_missing netauto-course https://github.com/GrahamPaasch/netauto-course.git
clone_if_missing netauto-course-day3 https://github.com/GrahamPaasch/netauto-course-day3.git
clone_if_missing automate_your_network https://github.com/GrahamPaasch/automate_your_network.git
clone_if_missing ml4nce https://github.com/GrahamPaasch/ml4nce.git

cat <<'INFO'

Modules synced.
- If you already have autocon4-lab, modules were linked from there.
- Otherwise they were cloned into modules/.
INFO
