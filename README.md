# Netauto Foundations Lab

A first-principles network automation course that uses the local GNS3 lab to practice real workflows.

Live lab required
- This course has no offline or slide-only path. If the lab is down, stop and restore access first.

What you'll learn
- Build inventory and connectivity from the live lab.
- Collect and normalize data with SNMP, syslog, and APIs.
- Capture and analyze live traffic to verify behavior.
- Automate multi-vendor changes with Ansible.
- Express intent and review plan/apply evidence.
- Handle credentials safely and capture evidence for review.
- Choose concurrency models for I/O-heavy tasks.
- Plan safe changes with pre-checks and rollback.

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
4. Read `docs/lab-practices.md`.
5. Start Day 1 in `labs/day-01-foundations/README.md`.

Lab integration
- `docs/lab-topology.yml` is the source of truth (generates `docs/lab-topology.md`).
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
