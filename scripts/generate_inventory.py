import json
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
TOPOLOGY_YAML = ROOT / "docs" / "lab-topology.yml"
TOPOLOGY_MD = ROOT / "docs" / "lab-topology.md"
DEVICES_JSON = ROOT / "labs" / "day-01-foundations" / "data" / "devices.json"
ANSIBLE_INI = ROOT / "labs" / "day-04-automation" / "examples" / "inventory.ini"

LAB_TOPOLOGY_HEADER = """# Lab Topology

This file is generated from `docs/lab-topology.yml`. Edit that file and re-run `python3 scripts/generate_inventory.py`.

This course expects a small multi-vendor lab with a jump host.

If you synced modules, look here for topology assets:
- `modules/introduction_to_python_for_networking_five_day_course/click_me_09_gns3_assets/gns3/topology-diagram.png`
- `modules/introduction_to_python_for_networking_five_day_course/click_me_09_gns3_assets/gns3/login-table.md`

Fill in the table below for quick reference.
"""

ANSIBLE_DEFAULTS = {
    "ios": {"group": "ios", "network_os": "ios", "connection": "network_cli"},
    "junos": {"group": "junos", "network_os": "junos", "connection": "netconf"},
    "eos": {"group": "eos", "network_os": "eos", "connection": "network_cli"},
}


def load_topology():
    if not TOPOLOGY_YAML.exists():
        raise SystemExit(f"Missing {TOPOLOGY_YAML}")
    data = yaml.safe_load(TOPOLOGY_YAML.read_text()) or {}
    devices = data.get("devices") or []
    if not isinstance(devices, list):
        raise SystemExit("Expected 'devices' to be a list in docs/lab-topology.yml")
    return devices


def validate_devices(devices):
    errors = []
    for idx, device in enumerate(devices, start=1):
        for key in ("hostname", "platform", "mgmt_ip"):
            if not device.get(key):
                errors.append(f"Device {idx} missing '{key}'")
    if errors:
        print("Invalid lab topology:", file=sys.stderr)
        for error in errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def write_devices_json(devices):
    payload = []
    for device in devices:
        payload.append({
            "hostname": device["hostname"],
            "role": device.get("role") or device.get("notes") or "",
            "mgmt_ip": device["mgmt_ip"],
            "vendor": device["platform"],
        })
    DEVICES_JSON.parent.mkdir(parents=True, exist_ok=True)
    DEVICES_JSON.write_text(json.dumps(payload, indent=2))


def write_lab_topology_md(devices):
    lines = [
        LAB_TOPOLOGY_HEADER.strip(),
        "",
        "| Hostname | Platform | Mgmt IP | Username | Password | Notes |",
        "| --- | --- | --- | --- | --- | --- |",
    ]
    for device in devices:
        notes = device.get("notes") or device.get("role") or ""
        lines.append(
            "| {hostname} | {platform} | {mgmt_ip} | {username} | {password} | {notes} |".format(
                hostname=device["hostname"],
                platform=device["platform"],
                mgmt_ip=device["mgmt_ip"],
                username=device.get("username") or "",
                password=device.get("password") or "",
                notes=notes,
            )
        )
    lines.append("")
    lines.append(
        "After updating the source of truth, run `python3 scripts/generate_inventory.py` "
        "to refresh generated files."
    )
    lines.append("")
    TOPOLOGY_MD.write_text("\n".join(lines))


def ansible_settings(device):
    defaults = ANSIBLE_DEFAULTS.get(device.get("platform"), {})
    ansible = device.get("ansible") or {}
    group = (
        device.get("ansible_group")
        or ansible.get("group")
        or defaults.get("group")
    )
    network_os = (
        device.get("ansible_network_os")
        or ansible.get("network_os")
        or defaults.get("network_os")
    )
    connection = (
        device.get("ansible_connection")
        or ansible.get("connection")
        or defaults.get("connection")
    )
    if not group or not network_os:
        return None
    return group, network_os, connection


def write_ansible_inventory(devices):
    groups = {}
    for device in devices:
        settings = ansible_settings(device)
        if not settings:
            continue
        group, network_os, connection = settings
        groups.setdefault(group, []).append((device, network_os, connection))

    lines = []
    for group, entries in groups.items():
        lines.append(f"[{group}]")
        for device, network_os, connection in entries:
            attrs = [f"ansible_host={device['mgmt_ip']}"]
            username = device.get("username")
            password = device.get("password")
            if username:
                attrs.append(f"ansible_user={username}")
            if password:
                attrs.append(f"ansible_password={password}")
            attrs.append(f"ansible_network_os={network_os}")
            if connection:
                attrs.append(f"ansible_connection={connection}")
            lines.append(f"{device['hostname']} " + " ".join(attrs))
        lines.append("")

    ANSIBLE_INI.parent.mkdir(parents=True, exist_ok=True)
    ANSIBLE_INI.write_text("\n".join(lines).rstrip() + "\n")


def main():
    devices = load_topology()
    validate_devices(devices)
    write_devices_json(devices)
    write_lab_topology_md(devices)
    write_ansible_inventory(devices)
    print(f"Wrote {DEVICES_JSON}")
    print(f"Wrote {TOPOLOGY_MD}")
    print(f"Wrote {ANSIBLE_INI}")


if __name__ == "__main__":
    main()
