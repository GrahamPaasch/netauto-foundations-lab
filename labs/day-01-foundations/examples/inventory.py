import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINES = ROOT / "baselines" / "devices.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

with BASELINES.open() as f:
    devices = json.load(f)

csv_path = OUTPUTS / "inventory.csv"
md_path = OUTPUTS / "inventory.md"

fieldnames = ["hostname", "role", "mgmt_ip", "vendor"]

with csv_path.open("w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(devices)

with md_path.open("w") as f:
    f.write("| " + " | ".join(fieldnames) + " |\n")
    f.write("| " + " | ".join(["---"] * len(fieldnames)) + " |\n")
    for d in devices:
        f.write("| " + " | ".join(str(d[h]) for h in fieldnames) + " |\n")

print(f"Wrote {csv_path} and {md_path}")
