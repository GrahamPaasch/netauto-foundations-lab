# Day 2 - Observability Basics

Outcomes
- Pull SNMP data and summarize it.
- Parse syslog into structured records.

Lab 1 - SNMP pull
1. Run baseline mode: `python3 examples/snmp_pull.py --baseline`.
2. Review `outputs/snmp_summary.json`.
3. Run live mode with your device IP and community.

Lab 2 - Syslog parse
1. Run `python3 examples/syslog_parse.py`.
2. Review `outputs/syslog_parsed.json`.
3. Add one extra regex pattern for a new message type.

Evidence
- `outputs/snmp_summary.json`
- `outputs/syslog_parsed.json`

Student checklist
- SNMP summary created (baseline or live).
- Syslog parsed into structured JSON.
- One new pattern added and verified.
- One alert idea written down.
