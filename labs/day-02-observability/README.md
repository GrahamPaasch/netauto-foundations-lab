# Day 2 - Observability Basics

Outcomes
- Pull SNMP data and summarize it.
- Parse syslog into structured records.

Lab 1 - SNMP pull
1. Run against your lab inventory: `python3 examples/snmp_pull.py`.
2. Review `outputs/snmp_summary.json`.
3. If needed, target a specific device: `python3 examples/snmp_pull.py --target 10.0.0.11`.

Live traffic capture and analysis (required)
1. Create an output folder if needed: `mkdir -p outputs`.
2. Identify the capture interface: `ip -br link` and pick the interface that sees lab traffic.
3. Start a capture (SNMP + syslog): `sudo tcpdump -i <iface> -w outputs/obs_traffic.pcap 'port 161 or port 514'`.
4. Generate traffic: run the SNMP pull and trigger a syslog event on a device.
5. Stop the capture (Ctrl+C), then summarize:
   - `tcpdump -nn -r outputs/obs_traffic.pcap > outputs/obs_traffic_summary.txt`
   - Optional: `tshark -r outputs/obs_traffic.pcap -q -z io,phs`

Lab 2 - Syslog parse
1. Export logs from your syslog server to a file (or use `/var/log/syslog` if that is your lab collector).
2. Run `python3 examples/syslog_parse.py --path /path/to/syslog.log`.
3. Review `outputs/syslog_parsed.json`.
4. Add one extra regex pattern for a new message type.

Evidence
- `outputs/snmp_summary.json`
- `outputs/syslog_parsed.json`
- `outputs/obs_traffic.pcap`
- `outputs/obs_traffic_summary.txt`

Student checklist
- SNMP summary created from live devices.
- Syslog parsed into structured JSON.
- One new pattern added and verified.
- Traffic capture saved and summarized.
- One alert idea written down.
