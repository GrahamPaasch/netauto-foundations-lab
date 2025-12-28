# Getting Started

Prereqs
- Python 3.10+
- Git
- GNS3 access and a jump host (if your lab requires it)
- tcpdump (or Wireshark/tshark for analysis)

Live lab required
- This course is live-lab only. If you cannot reach devices or capture traffic, pause and fix the lab.
- Minimum checks: ping one device and confirm you can see SNMP or syslog traffic on the collector.
  - Example: `sudo tcpdump -i <iface> port 161 or port 514`

Credential handling
- Keep real credentials out of version control. Treat `docs/lab-topology.yml` as local-only.
- If you must share the repo, replace usernames/passwords with placeholders first.
- Prefer environment variables or a password manager for long-lived secrets.

Setup
1. From the repo root, run `./scripts/bootstrap.sh`.
2. Run `./scripts/sync_modules.sh` to pull optional lab modules.
3. Run `./scripts/sanity_check.sh`.
4. Open `docs/lab-topology.yml` and confirm device access details (then regenerate `docs/lab-topology.md`).
5. Start Day 1 in `labs/day-01-foundations/README.md`.

Course-wide practices
- Read `docs/lab-practices.md` before starting Day 1.

Tip
- If you already have an `autocon4-lab` hub in `/home/gns3/Documents`, the sync script will link to those modules instead of cloning.
