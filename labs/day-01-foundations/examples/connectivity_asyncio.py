import asyncio
import csv
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEVICES = ROOT / "data" / "devices.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

CONCURRENCY = 20


async def ping(ip):
    process = await asyncio.create_subprocess_exec(
        "ping",
        "-c",
        "2",
        ip,
        stdout=asyncio.subprocess.DEVNULL,
        stderr=asyncio.subprocess.DEVNULL,
    )
    return await process.wait() == 0


async def ping_limited(sem, ip):
    async with sem:
        return await ping(ip)


async def live_results():
    with DEVICES.open() as f:
        devices = json.load(f)
    sem = asyncio.Semaphore(CONCURRENCY)
    tasks = [asyncio.create_task(ping_limited(sem, d["mgmt_ip"])) for d in devices]
    statuses = await asyncio.gather(*tasks)
    results = []
    for d, ok in zip(devices, statuses):
        results.append({
            "hostname": d["hostname"],
            "mgmt_ip": d["mgmt_ip"],
            "reachable": "yes" if ok else "no",
        })
    return results


def write_report(rows, out_path):
    fieldnames = ["hostname", "mgmt_ip", "reachable"]
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


if __name__ == "__main__":
    rows = asyncio.run(live_results())
    out_path = OUTPUTS / "connectivity_asyncio.csv"
    write_report(rows, out_path)
    print(f"Wrote {out_path}")
