# Getting Started

Prereqs
- Python 3.10+
- Git
- GNS3 access and a jump host (if your lab requires it)

Setup
1. From the repo root, run `./scripts/bootstrap.sh`.
2. Run `./scripts/sync_modules.sh` to pull optional lab modules.
3. Open `docs/lab-topology.md` and confirm device access details.
4. Start Day 1 in `labs/day-01-foundations/README.md`.

Tip
- If you already have an `autocon4-lab` hub in `/home/gns3/Documents`, the sync script will link to those modules instead of cloning.
