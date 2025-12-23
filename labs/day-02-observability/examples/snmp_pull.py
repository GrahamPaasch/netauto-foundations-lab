import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

DEFAULT_INVENTORY = ROOT.parent / "day-01-foundations" / "data" / "devices.json"


def load_inventory(path):
    data = json.loads(Path(path).read_text())
    return [entry["mgmt_ip"] for entry in data if entry.get("mgmt_ip")]


def live(targets, community):
    try:
        from pysnmp.hlapi import (
            CommunityData,
            ContextData,
            ObjectIdentity,
            ObjectType,
            SnmpEngine,
            UdpTransportTarget,
            getCmd,
        )
    except ImportError:
        print("pysnmp is not installed. Install requirements first.")
        return

    results = []
    for target in targets:
        iterator = getCmd(
            SnmpEngine(),
            CommunityData(community),
            UdpTransportTarget((target, 161), timeout=2, retries=1),
            ContextData(),
            ObjectType(ObjectIdentity("1.3.6.1.2.1.1.3.0")),  # sysUpTime.0
        )
        error_indication, error_status, error_index, var_binds = next(iterator)
        if error_indication:
            results.append({"device": target, "error": str(error_indication)})
            continue
        if error_status:
            results.append({"device": target, "error": error_status.prettyPrint()})
            continue
        results.append({"device": target, "metrics": {"sysUpTime": str(var_binds[0][1])}})

    out_path = OUTPUTS / "snmp_summary.json"
    out_path.write_text(json.dumps(results, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--inventory", default=str(DEFAULT_INVENTORY))
    parser.add_argument("--target", action="append")
    parser.add_argument("--community", default="public")
    args = parser.parse_args()

    targets = args.target or []
    if not targets and Path(args.inventory).exists():
        targets = load_inventory(args.inventory)

    if not targets:
        raise SystemExit("No targets provided and inventory not found.")

    live(targets, args.community)
