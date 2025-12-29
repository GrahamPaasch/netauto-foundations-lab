#!/usr/bin/env python3
"""Convert Nmap XML to NetBox CSV imports."""
import argparse
import csv
import re
import xml.etree.ElementTree as ET
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "unknown"


def normalize_name(hostname: str, ip: str) -> str:
    name = (hostname or "").strip()
    if name and name != "-":
        name = name.split(".")[0]
    name = name.strip("_")
    if not name:
        name = f"host-{ip.replace('.', '-') }"
    return name


def role_for_name(name: str) -> str:
    upper = name.upper()
    if "OOB" in upper or "ADMIN" in upper or "MGMT" in upper:
        return "oob"
    if "GATEWAY" in upper or upper.startswith("GW") or "-GW-" in upper:
        return "gateway"
    if "WAN" in upper:
        return "wan"
    if "CORE" in upper:
        return "core"
    if "DIST" in upper:
        return "distribution"
    if "ACCESS" in upper or "LS" in upper:
        return "access"
    return "unknown"


def classify_host(os_name: str, os_vendor: str) -> tuple[str, str, str]:
    name_upper = (os_name or "").upper()
    vendor = os_vendor or ""
    if "JUNIPER" in name_upper or vendor == "Juniper" or "JUNOS" in name_upper:
        return "Juniper", "junos", "Juniper Generic"
    if "CISCO" in name_upper or vendor == "Cisco" or "IOS" in name_upper:
        return "Cisco", "ios", "Cisco IOS Device"
    if "LINUX" in name_upper or vendor == "Linux":
        return "Generic", "linux", "Linux Host"
    return "Generic", "unknown", "Unknown Device"


ROLE_LABELS = {
    "core": "Core",
    "distribution": "Distribution",
    "access": "Access",
    "wan": "WAN",
    "gateway": "Gateway",
    "oob": "OOB",
    "unknown": "Unknown",
}


def role_label(role: str) -> str:
    return ROLE_LABELS.get(role, role.title())


def parse_markdown_summary(path: Path) -> list[dict]:
    lines = path.read_text(encoding="ascii").splitlines()
    header_idx = None
    for idx, line in enumerate(lines):
        if line.strip().startswith("| IP | Hostnames |"):
            header_idx = idx
            break
    if header_idx is None:
        raise ValueError("Summary table not found in markdown.")

    records = []
    for line in lines[header_idx + 2 :]:
        if not line.strip().startswith("|"):
            break
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 8:
            continue
        ip, hostnames, status, mac, os_guess, _distance, _uptime, open_ports = parts[:8]
        hostname = hostnames.replace(" (PTR)", "").strip()
        if hostname == "-":
            hostname = ""
        os_name = re.sub(r"\s*\(\d+\)$", "", os_guess).strip()
        if os_name == "-":
            os_name = ""
        os_vendor = ""
        if "Juniper" in os_name or "JUNOS" in os_name:
            os_vendor = "Juniper"
        elif "Cisco" in os_name or "IOS" in os_name:
            os_vendor = "Cisco"
        elif "Linux" in os_name:
            os_vendor = "Linux"

        records.append(
            {
                "ip": ip,
                "hostname": hostname,
                "os_name": os_name,
                "os_vendor": os_vendor,
                "mac": mac if mac != "-" else "",
                "open_ports": int(open_ports) if open_ports.isdigit() else 0,
            }
        )
    return records


def parse_nmap_xml(path: Path) -> list[dict]:
    root = ET.parse(path).getroot()
    records = []
    for host in root.findall("host"):
        status = host.find("status")
        if status is None or status.get("state") != "up":
            continue
        addr = host.find("address[@addrtype='ipv4']")
        ip = addr.get("addr") if addr is not None else ""
        if not ip:
            continue

        hostname = ""
        hn = host.find("hostnames")
        if hn is not None:
            h = hn.find("hostname")
            if h is not None:
                hostname = h.get("name") or ""

        os_name = ""
        os_vendor = ""
        os_elem = host.find("os")
        if os_elem is not None:
            osmatch = os_elem.find("osmatch")
            if osmatch is not None:
                os_name = osmatch.get("name") or ""
                osclass = osmatch.find("osclass")
                if osclass is not None:
                    os_vendor = osclass.get("vendor") or ""

        mac = ""
        mac_addr = host.find("address[@addrtype='mac']")
        if mac_addr is not None:
            mac = mac_addr.get("addr") or ""

        open_ports = 0
        ports_elem = host.find("ports")
        if ports_elem is not None:
            for p in ports_elem.findall("port"):
                state = p.find("state")
                if state is not None and state.get("state") == "open":
                    open_ports += 1

        records.append(
            {
                "ip": ip,
                "hostname": hostname,
                "os_name": os_name,
                "os_vendor": os_vendor,
                "mac": mac,
                "open_ports": open_ports,
            }
        )
    return records


def main() -> None:
    parser = argparse.ArgumentParser(description="Convert Nmap XML to NetBox CSV imports.")
    parser.add_argument("--xml", help="Path to Nmap XML output.")
    parser.add_argument("--md", help="Path to docs/nmap-inventory.md summary.")
    parser.add_argument("--out", default="netbox", help="Output directory for CSV files.")
    parser.add_argument("--site", default="techyes-lab", help="NetBox site name.")
    parser.add_argument("--prefix", default="10.0.0.0/16", help="Prefix to create in NetBox.")
    args = parser.parse_args()

    if not args.xml and not args.md:
        raise SystemExit("Provide --xml or --md.")
    if args.xml and args.md:
        raise SystemExit("Provide only one of --xml or --md.")

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    if args.xml:
        records = parse_nmap_xml(Path(args.xml))
    else:
        records = parse_markdown_summary(Path(args.md))

    devices = []
    ip_addresses = []
    manufacturers = set()
    platforms = set()
    device_types = {}
    roles = set()

    used_names = set()

    for rec in records:
        ip = rec["ip"]
        hostname = rec["hostname"]
        name = normalize_name(hostname, ip)
        base_name = name
        suffix = 2
        while name in used_names:
            name = f"{base_name}-{suffix}"
            suffix += 1
        used_names.add(name)

        os_name = rec["os_name"]
        os_vendor = rec["os_vendor"]

        manufacturer, platform, device_type = classify_host(os_name, os_vendor)
        manufacturers.add(manufacturer)
        platforms.add(platform)
        device_types[(manufacturer, device_type)] = True

        role = role_for_name(name)
        roles.add(role)

        mac = rec["mac"]
        open_ports = rec["open_ports"]

        comments_bits = []
        if os_name:
            comments_bits.append(f"nmap_os_guess={os_name}")
        if mac:
            comments_bits.append(f"mac={mac}")
        comments_bits.append(f"open_tcp_ports={open_ports}")
        comments = "; ".join(comments_bits) if comments_bits else ""

        devices.append({
            "name": name,
            "device_role": role_label(role),
            "device_type": device_type,
            "site": args.site,
            "status": "active",
            "platform": platform,
            "comments": comments,
        })

        if ip:
            if os_name:
                description = f"{name} ({os_name})"
            else:
                description = name
            ip_addresses.append(
                {
                    "address": f"{ip}/32",
                    "status": "active",
                    "dns_name": hostname or "",
                    "description": description,
                }
            )

    site_slug = slugify(args.site)

    # Write CSVs
    def write_csv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
        with path.open("w", newline="", encoding="ascii") as fh:
            writer = csv.DictWriter(fh, fieldnames=fieldnames)
            writer.writeheader()
            for row in rows:
                writer.writerow({k: row.get(k, "") for k in fieldnames})

    write_csv(out_dir / "sites.csv", ["name", "slug"], [{"name": args.site, "slug": site_slug}])

    manufacturer_rows = []
    for m in sorted(manufacturers):
        manufacturer_rows.append({"name": m, "slug": slugify(m)})
    write_csv(out_dir / "manufacturers.csv", ["name", "slug"], manufacturer_rows)

    role_rows = []
    for r in sorted(roles):
        role_rows.append({"name": role_label(r), "slug": slugify(r)})
    write_csv(out_dir / "device_roles.csv", ["name", "slug"], role_rows)

    device_type_rows = []
    for (manufacturer, model) in sorted(device_types.keys()):
        device_type_rows.append({
            "manufacturer": manufacturer,
            "model": model,
            "slug": slugify(f"{manufacturer}-{model}"),
        })
    write_csv(out_dir / "device_types.csv", ["manufacturer", "model", "slug"], device_type_rows)

    platform_rows = []
    for p in sorted(platforms):
        platform_rows.append({"name": p, "slug": slugify(p)})
    write_csv(out_dir / "platforms.csv", ["name", "slug"], platform_rows)

    write_csv(
        out_dir / "devices.csv",
        ["name", "device_role", "device_type", "site", "status", "platform", "comments"],
        devices,
    )

    write_csv(
        out_dir / "ip_addresses.csv",
        ["address", "status", "dns_name", "description"],
        ip_addresses,
    )

    write_csv(
        out_dir / "prefixes.csv",
        ["prefix", "status", "description"],
        [{"prefix": args.prefix, "status": "active", "description": "Nmap discovered"}],
    )

    readme = out_dir / "README.md"
    readme.write_text(
        "# NetBox Import Data (from Nmap)\n"
        "\n"
        "These CSVs are generated from Nmap XML or the summary markdown and are intended for NetBox's CSV import.\n"
        "\n"
        "Import order (recommended):\n"
        "1. sites.csv\n"
        "2. manufacturers.csv\n"
        "3. device_roles.csv\n"
        "4. device_types.csv\n"
        "5. platforms.csv\n"
        "6. prefixes.csv\n"
        "7. ip_addresses.csv\n"
        "8. devices.csv\n"
        "\n"
        "Notes:\n"
        "- IP addresses are imported unassigned. Assign them to interfaces later in NetBox.\n"
        "- Device roles/types/platforms are best-effort based on OS guesses and hostnames.\n"
        "- Rerun with a different site or prefix:\n"
        "  python3 scripts/nmap_to_netbox.py --xml /path/to/scan.xml --out netbox --site YOUR-SITE --prefix 10.0.0.0/16\n"
        "  python3 scripts/nmap_to_netbox.py --md docs/nmap-inventory.md --out netbox --site YOUR-SITE --prefix 10.0.0.0/16\n",
        encoding="ascii",
    )


if __name__ == "__main__":
    main()
