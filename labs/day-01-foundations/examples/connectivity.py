import argparse
import csv
import json
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ROOT / "baselines" / "devices.json"
BASELINE = ROOT / "baselines" / "ping_baseline.csv"
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


def baseline_results():
    with BASELINE.open() as f:
        return list(csv.DictReader(f))


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
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", action="store_true", help="use baseline snapshot")
    parser.add_argument("--offline", action="store_true", help=argparse.SUPPRESS)
    args = parser.parse_args()

    rows = baseline_results() if (args.baseline or args.offline) else live_results()
    out_path = OUTPUTS / "connectivity.csv"
    write_report(rows, out_path)
    print(f"Wrote {out_path}")
