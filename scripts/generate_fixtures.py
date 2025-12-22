import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TOPOLOGY = ROOT / "docs" / "lab-topology.md"
OUTPUT = ROOT / "labs" / "day-01-foundations" / "fixtures" / "devices.json"


def parse_table(markdown):
    lines = [line.strip() for line in markdown.splitlines() if line.strip()]
    table_lines = [line for line in lines if line.startswith("|")]
    if len(table_lines) < 3:
        return []

    header = [h.strip().lower() for h in table_lines[0].strip("|").split("|")]
    rows = []
    for line in table_lines[2:]:
        cols = [c.strip() for c in line.strip("|").split("|")]
        if len(cols) != len(header):
            continue
        row = dict(zip(header, cols))
        rows.append(row)
    return rows


def main():
    data = parse_table(TOPOLOGY.read_text())
    devices = []
    for row in data:
        if row.get("hostname", "").startswith("r") or row.get("hostname"):
            devices.append({
                "hostname": row.get("hostname"),
                "role": row.get("notes") or "",
                "mgmt_ip": row.get("mgmt ip"),
                "vendor": row.get("platform"),
            })

    OUTPUT.write_text(json.dumps(devices, indent=2))
    print(f"Wrote {OUTPUT}")


if __name__ == "__main__":
    main()
