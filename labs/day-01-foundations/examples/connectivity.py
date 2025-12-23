import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ROOT / "data" / "devices.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def ping(ip):
    result = subprocess.run(
        ["ping", "-c", "2", ip],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


def live_results():
    with DEVICES.open() as f:
        devices = json.load(f)
    results = []
    for d in devices:
        reachable = "yes" if ping(d["mgmt_ip"]) else "no"
        results.append({
            "hostname": d["hostname"],
            "mgmt_ip": d["mgmt_ip"],
            "reachable": reachable,
        })
    return results


def write_report(rows, out_path):
    fieldnames = ["hostname", "mgmt_ip", "reachable"]
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

if __name__ == "__main__":
    rows = live_results()
    out_path = OUTPUTS / "connectivity.csv"
    write_report(rows, out_path)
    print(f"Wrote {out_path}")
