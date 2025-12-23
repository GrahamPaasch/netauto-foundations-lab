# Netauto Foundations Lab

A first-principles network automation course that uses the local GNS3 lab to practice real workflows.

What you'll learn
- Build inventory and connectivity from the live lab.
- Collect and normalize data with SNMP, syslog, and APIs.
- Automate multi-vendor changes with Ansible.
- Express intent and review plan/apply evidence.

Course map
- Day 0: setup and lab access
- Day 1: foundations and connectivity
- Day 2: observability basics
- Day 3: APIs and data modeling
- Day 4: configuration automation
- Day 5: intent capstone

Quick start
1. Run `./scripts/bootstrap.sh`.
2. Run `./scripts/verify.sh`.
3. Read `docs/getting-started.md`.
4. Start Day 1 in `labs/day-01-foundations/README.md`.

Lab integration
- `docs/lab-topology.md` is the source of truth.
- After updating topology, run `python3 scripts/generate_inventory.py`.
- Optional lab modules live under `modules/` (use `./scripts/sync_modules.sh`).

Instructor and evidence
- Instructor flow: `docs/instructor-quickstart.md`.
- Evidence checklist: `docs/assessment.md`.

Repo layout
- `docs/` course docs and instructor notes.
- `labs/` day-by-day lab guides.
- `modules/` optional lab modules (cloned or symlinked).
- `scripts/` bootstrap and helpers.
- `assets/` diagrams and supporting files.
