#!/usr/bin/env python3
"""Enrich NetBox CSVs with Junos evidence logs."""
import argparse
import csv
import re
from pathlib import Path


def read_csv(path: Path) -> tuple[list[str], list[dict]]:
    with path.open("r", newline="", encoding="ascii") as fh:
        reader = csv.DictReader(fh)
        return reader.fieldnames or [], list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    with path.open("w", newline="", encoding="ascii") as fh:
        writer = csv.DictWriter(fh, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            writer.writerow({k: row.get(k, "") for k in fieldnames})


def parse_show_version(path: Path) -> dict:
    data = {"hostname": "", "model": "", "junos": ""}
    for line in path.read_text(encoding="ascii", errors="ignore").splitlines():
        if line.startswith("Hostname:"):
            data["hostname"] = line.split(":", 1)[1].strip()
        elif line.startswith("Model:"):
            data["model"] = line.split(":", 1)[1].strip()
        elif line.startswith("Junos:"):
            data["junos"] = line.split(":", 1)[1].strip()
    return data


def parse_chassis_serial(path: Path) -> str:
    for line in path.read_text(encoding="ascii", errors="ignore").splitlines():
        if line.startswith("Chassis"):
            rest = line[len("Chassis"):].strip()
            parts = rest.split()
            if parts:
                return parts[0]
    return ""


def parse_lldp_chassis_id(path: Path) -> str:
    for line in path.read_text(encoding="ascii", errors="ignore").splitlines():
        match = re.match(r"^Chassis ID\s*:\s*(\S+)", line)
        if match:
            return match.group(1)
    return ""


def update_comment(comment: str, updates: dict) -> str:
    parts = [p.strip() for p in comment.split(";") if p.strip()]
    kept = []
    for part in parts:
        if "=" in part:
            key = part.split("=", 1)[0].strip()
            if key in updates:
                continue
        kept.append(part)
    for key, value in updates.items():
        if value:
            kept.append(f"{key}={value}")
    return "; ".join(kept)


def ensure_device_type(netbox_dir: Path, manufacturer: str, model: str) -> None:
    path = netbox_dir / "device_types.csv"
    fields, rows = read_csv(path)
    if not fields:
        raise SystemExit(f"Empty CSV: {path}")
    for row in rows:
        if row.get("manufacturer") == manufacturer and row.get("model") == model:
            return
    rows.append({"manufacturer": manufacturer, "model": model, "slug": slugify(f"{manufacturer}-{model}")})
    write_csv(path, fields, rows)


def ensure_manufacturer(netbox_dir: Path, manufacturer: str) -> None:
    path = netbox_dir / "manufacturers.csv"
    fields, rows = read_csv(path)
    if not fields:
        raise SystemExit(f"Empty CSV: {path}")
    for row in rows:
        if row.get("name") == manufacturer:
            return
    rows.append({"name": manufacturer, "slug": slugify(manufacturer)})
    write_csv(path, fields, rows)


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "unknown"


def main() -> None:
    parser = argparse.ArgumentParser(description="Enrich NetBox CSVs with Junos evidence logs.")
    parser.add_argument("--evidence", default="evidence/logs", help="Directory with evidence logs.")
    parser.add_argument("--netbox", default="netbox", help="NetBox CSV directory.")
    args = parser.parse_args()

    evidence_dir = Path(args.evidence)
    netbox_dir = Path(args.netbox)

    version_files = sorted(evidence_dir.glob("*_show-version.txt"))
    hostname_by_ip = {}
    host_data = {}

    for path in version_files:
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)_show-version\.txt", path.name)
        if not match:
            continue
        ip = match.group(1)
        data = parse_show_version(path)
        if data["hostname"]:
            hostname_by_ip[ip] = data["hostname"]
            host_data.setdefault(data["hostname"], {})
            host_data[data["hostname"]].update(data)

    for path in evidence_dir.glob("*_show-hostname.txt"):
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)_show-hostname\.txt", path.name)
        if not match:
            continue
        ip = match.group(1)
        text = path.read_text(encoding="ascii", errors="ignore")
        match_host = re.search(r"set system host-name\s+(\S+)", text)
        if match_host:
            hostname_by_ip[ip] = match_host.group(1)

    for path in evidence_dir.glob("*_show-chassis-hardware.txt"):
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)_show-chassis-hardware\.txt", path.name)
        if not match:
            continue
        ip = match.group(1)
        hostname = hostname_by_ip.get(ip)
        if not hostname:
            continue
        serial = parse_chassis_serial(path)
        if serial:
            host_data.setdefault(hostname, {})["serial"] = serial

    for path in evidence_dir.glob("*_show-lldp-local-information.txt"):
        match = re.match(r"(\d+\.\d+\.\d+\.\d+)_show-lldp-local-information\.txt", path.name)
        if not match:
            continue
        ip = match.group(1)
        hostname = hostname_by_ip.get(ip)
        if not hostname:
            continue
        chassis_id = parse_lldp_chassis_id(path)
        if chassis_id:
            host_data.setdefault(hostname, {})["lldp_chassis_id"] = chassis_id

    if not host_data:
        raise SystemExit("No Junos evidence found to enrich.")

    # Ensure Juniper manufacturer/device type exists
    ensure_manufacturer(netbox_dir, "Juniper")
    ensure_device_type(netbox_dir, "Juniper", "vMX")

    devices_path = netbox_dir / "devices.csv"
    fields, rows = read_csv(devices_path)
    if not fields:
        raise SystemExit(f"Empty CSV: {devices_path}")

    if "serial" not in fields:
        fields.append("serial")

    for row in rows:
        name = row.get("name", "")
        if name not in host_data:
            continue
        data = host_data[name]
        row["device_type"] = "vMX"
        row["platform"] = "junos"
        if data.get("serial"):
            row["serial"] = data["serial"]
        updates = {
            "model": data.get("model", ""),
            "junos": data.get("junos", ""),
            "lldp_chassis_id": data.get("lldp_chassis_id", ""),
        }
        row["comments"] = update_comment(row.get("comments", ""), updates)

    write_csv(devices_path, fields, rows)


if __name__ == "__main__":
    main()
