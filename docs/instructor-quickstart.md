# Instructor Quickstart

Before class (30-60 min)
- Verify GNS3 lab is up and reachable.
- Test one login per vendor using `docs/lab-topology.md`.
- Update `docs/lab-topology.md` with any changes.
- Run `python3 scripts/generate_baselines.py` to refresh Day 1 baselines.
- Run `./scripts/verify.sh` to confirm repo health.
- (Day 4) Preinstall Ansible collections: `cisco.ios`, `junipernetworks.junos`, `arista.eos`.

Day-of flow (suggested)
- 10-15 min concept intro
- 45-60 min lab time
- 10-15 min review and evidence check

Live demo path
- Day 1: inventory + connectivity (baseline then live)
- Day 2: parse syslog + SNMP pull
- Day 3: normalize API data
- Day 4: run multi-vendor playbook
- Day 5: plan/apply in netintent-ops

Backup plan if lab is down
- Use baseline datasets in `labs/*/baselines/`.
- Keep the same lab flow and capture evidence from baseline runs.

After class
- Spot-check evidence in `docs/assessment.md`.
- Capture common issues and update `docs/troubleshooting.md`.
