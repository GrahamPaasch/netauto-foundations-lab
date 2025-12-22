# Netauto Foundations Lab

A clean, beginner-friendly course that builds from first principles and uses the local GNS3 lab to practice real automation workflows.

What this is
- A day-by-day course with clear outcomes and hands-on labs.
- Designed for this teaching lab system (GNS3 + jump host + multi-vendor devices).
- Uses local modules for capstone and deeper practice when available.

Quick start
1. Read `docs/getting-started.md`.
2. Run `./scripts/bootstrap.sh`.
3. Run `./scripts/verify.sh`.
4. Open `docs/syllabus.md` and follow Day 1.

Lab integration
- Optional lab modules live under `modules/`.
- Run `./scripts/sync_modules.sh` to clone or link them.
- Topology and access details are in `docs/lab-topology.md`.

Repo layout
- `docs/` course docs, setup, and instructor notes.
- `labs/` day-by-day lab guides.
- `modules/` optional lab modules (cloned or symlinked).
- `scripts/` bootstrap and helper scripts.
- `assets/` diagrams and supporting files.
