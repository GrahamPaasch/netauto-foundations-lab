#!/usr/bin/env python3
"""Collect inventory data over SSH using key-based auth."""
import argparse
import re
import subprocess
from pathlib import Path


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9]+", "-", value)
    value = value.strip("-")
    return value or "command"


def run_ssh(host: str, user: str, cmd: str, known_hosts: str, timeout: int) -> tuple[int, str, str]:
    args = [
        "ssh",
        "-o",
        "BatchMode=yes",
        "-o",
        "StrictHostKeyChecking=accept-new",
        "-o",
        f"UserKnownHostsFile={known_hosts}",
        "-o",
        f"ConnectTimeout={timeout}",
        f"{user}@{host}",
        cmd,
    ]
    try:
        proc = subprocess.run(args, capture_output=True, text=True, timeout=timeout + 5)
    except subprocess.TimeoutExpired:
        return 124, "", "TIMEOUT"
    return proc.returncode, proc.stdout, proc.stderr


def write_logs(out_dir: Path, host: str, label: str, stdout: str, stderr: str) -> None:
    base = out_dir / f"{host}_{label}"
    Path(str(base) + ".txt").write_text(stdout, encoding="ascii", errors="ignore")
    Path(str(base) + ".err").write_text(stderr, encoding="ascii", errors="ignore")


def parse_hosts_from_md(path: Path) -> list[str]:
    lines = path.read_text(encoding="ascii").splitlines()
    hosts = []
    for line in lines:
        if not line.startswith("|"):
            continue
        parts = [p.strip() for p in line.strip().strip("|").split("|")]
        if len(parts) < 1:
            continue
        ip = parts[0]
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", ip):
            hosts.append(ip)
    return hosts


def parse_hosts_from_file(path: Path) -> list[str]:
    hosts = []
    for line in path.read_text(encoding="ascii", errors="ignore").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        if re.match(r"^\d+\.\d+\.\d+\.\d+$", line):
            hosts.append(line)
    return hosts


def detect_os(host: str, user: str, known_hosts: str, timeout: int, out_dir: Path) -> tuple[str, str]:
    # Try Junos first.
    rc, out, err = run_ssh(host, user, "show version | no-more", known_hosts, timeout)
    write_logs(out_dir, host, "detect-show-version-no-more", out, err)
    if "JUNOS" in out or "Junos" in out:
        return "junos", out

    # Try generic show version for IOS or Junos.
    rc, out, err = run_ssh(host, user, "show version", known_hosts, timeout)
    write_logs(out_dir, host, "detect-show-version", out, err)
    if "JUNOS" in out or "Junos" in out:
        return "junos", out
    if "Cisco IOS" in out or "IOS XE" in out or "NX-OS" in out or "Cisco" in out:
        return "ios", out

    # Try Linux.
    rc, out, err = run_ssh(host, user, "uname -a", known_hosts, timeout)
    write_logs(out_dir, host, "detect-uname", out, err)
    if out.strip():
        return "linux", out

    return "unknown", ""


def main() -> None:
    parser = argparse.ArgumentParser(description="Collect inventory data via SSH.")
    parser.add_argument("--user", default="gpaasch", help="SSH username.")
    parser.add_argument("--inventory-md", default="docs/nmap-inventory.md", help="Inventory markdown.")
    parser.add_argument("--hosts-file", default="/tmp/nmap-10.0.0.0_16-fullscan.hosts", help="Optional hosts file.")
    parser.add_argument("--out", default="evidence/logs", help="Output directory.")
    parser.add_argument("--known-hosts", default="/tmp/known_hosts", help="SSH known_hosts file.")
    parser.add_argument("--timeout", type=int, default=8, help="SSH connect timeout seconds.")
    parser.add_argument("--exclude", action="append", default=[], help="IP to exclude (repeatable).")
    parser.add_argument("--enable-lldp", action="store_true", help="Enable LLDP where possible.")
    args = parser.parse_args()

    out_dir = Path(args.out)
    out_dir.mkdir(parents=True, exist_ok=True)

    hosts = set()
    md_path = Path(args.inventory_md)
    if md_path.exists():
        hosts.update(parse_hosts_from_md(md_path))
    hosts_path = Path(args.hosts_file)
    if hosts_path.exists():
        hosts.update(parse_hosts_from_file(hosts_path))

    for ip in args.exclude:
        hosts.discard(ip)

    hosts = sorted(hosts, key=lambda x: list(map(int, x.split("."))))
    if not hosts:
        raise SystemExit("No hosts found.")

    summary_lines = []

    for host in hosts:
        os_type, _ = detect_os(host, args.user, args.known_hosts, args.timeout, out_dir)
        summary_lines.append(f"{host} os={os_type}")

        if os_type == "junos":
            cmds = [
                "show version | no-more",
                "show chassis hardware | no-more",
                "show interfaces terse | no-more",
                "show lldp local-information | no-more",
                "show lldp neighbors | no-more",
                "show lldp statistics | no-more",
                "show configuration protocols lldp | display set",
                "show configuration | display set | match \"set system host-name\"",
                "show system uptime | no-more",
            ]
            if args.enable_lldp:
                cmds.insert(0, "configure; set protocols lldp interface all; commit and-quit")
        elif os_type == "ios":
            cmds = [
                "terminal length 0; show version",
                "terminal length 0; show inventory",
                "terminal length 0; show ip interface brief",
                "terminal length 0; show interfaces status",
                "terminal length 0; show lldp neighbors",
                "terminal length 0; show lldp neighbors detail",
                "terminal length 0; show cdp neighbors detail",
                "terminal length 0; show run | include hostname",
            ]
            if args.enable_lldp:
                cmds.insert(0, "configure terminal; lldp run; end; write memory")
        elif os_type == "linux":
            cmds = [
                "uname -a",
                "ip -br addr",
                "ip -br link",
                "lldpctl",
                "lldpcli show neighbors",
            ]
        else:
            cmds = ["show version", "uname -a"]

        for cmd in cmds:
            label = slugify(cmd)
            rc, out, err = run_ssh(host, args.user, cmd, args.known_hosts, args.timeout)
            write_logs(out_dir, host, label, out, err)

    summary_path = out_dir / "ssh_collect_summary.txt"
    summary_path.write_text("\n".join(summary_lines) + "\n", encoding="ascii")


if __name__ == "__main__":
    main()
