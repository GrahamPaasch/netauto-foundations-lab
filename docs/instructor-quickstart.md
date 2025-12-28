# Instructor Quickstart

Before class (30-60 min)
- Verify GNS3 lab is up and reachable.
- Test one login per vendor using `docs/lab-topology.yml`.
- Update `docs/lab-topology.yml` with any changes.
- Run `python3 scripts/generate_inventory.py` to refresh Day 1 inventory data.
- Run `./scripts/verify.sh` to confirm repo health.
- (Day 4) Preinstall Ansible collections: `cisco.ios`, `junipernetworks.junos`, `arista.eos`.
- Confirm you can capture traffic on the collector or jump host with tcpdump.

Day-of flow (suggested)
- 10-15 min concept intro
- 45-60 min lab time
- 10-15 min review and evidence check

Live demo path
- Day 1: inventory + connectivity (live lab)
- Day 2: capture SNMP/syslog traffic, then parse syslog + SNMP pull
- Day 3: normalize API data
- Day 4: run multi-vendor playbook
- Day 5: plan/apply in netintent-ops

Lab must be live
- This course has no offline path. If the lab is down, pause and restore access first.

After class
- Spot-check evidence in `docs/assessment.md`.
- Capture common issues and update `docs/troubleshooting.md`.
