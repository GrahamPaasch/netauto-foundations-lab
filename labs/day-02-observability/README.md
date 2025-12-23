# Day 2 - Observability Basics

Outcomes
- Pull SNMP data and summarize it.
- Parse syslog into structured records.

Lab 1 - SNMP pull
1. Run against your lab inventory: `python3 examples/snmp_pull.py`.
2. Review `outputs/snmp_summary.json`.
3. If needed, target a specific device: `python3 examples/snmp_pull.py --target 10.0.0.11`.

Live traffic check (required)
- Confirm SNMP or syslog packets are visible on the collector or jump host.
- Example: `sudo tcpdump -i <iface> port 161 or port 514`

Lab 2 - Syslog parse
1. Export logs from your syslog server to a file (or use `/var/log/syslog` if that is your lab collector).
2. Run `python3 examples/syslog_parse.py --path /path/to/syslog.log`.
3. Review `outputs/syslog_parsed.json`.
4. Add one extra regex pattern for a new message type.

Evidence
- `outputs/snmp_summary.json`
- `outputs/syslog_parsed.json`

Student checklist
- SNMP summary created from live devices.
- Syslog parsed into structured JSON.
- One new pattern added and verified.
- One alert idea written down.
