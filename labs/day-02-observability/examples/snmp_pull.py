import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BASELINE_PATH = ROOT / "baselines" / "snmp_sample.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def baseline():
    data = json.loads(BASELINE_PATH.read_text())
    out_path = OUTPUTS / "snmp_summary.json"
    out_path.write_text(json.dumps(data, indent=2))
    print(f"Wrote {out_path}")


def live(target, community):
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
        print("pysnmp is not installed. Run this in baseline mode or install requirements.")
        return

    iterator = getCmd(
        SnmpEngine(),
        CommunityData(community),
        UdpTransportTarget((target, 161), timeout=2, retries=1),
        ContextData(),
        ObjectType(ObjectIdentity("1.3.6.1.2.1.1.3.0")),  # sysUpTime.0
    )
    error_indication, error_status, error_index, var_binds = next(iterator)
    if error_indication:
        print(f"SNMP error: {error_indication}")
        return
    if error_status:
        print(f"SNMP error: {error_status.prettyPrint()}")
        return

    result = {"device": target, "metrics": {"sysUpTime": str(var_binds[0][1])}}
    out_path = OUTPUTS / "snmp_summary.json"
    out_path.write_text(json.dumps(result, indent=2))
    print(f"Wrote {out_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--baseline", action="store_true")
    parser.add_argument("--offline", action="store_true", help=argparse.SUPPRESS)
    parser.add_argument("--target", default="10.0.0.11")
    parser.add_argument("--community", default="public")
    args = parser.parse_args()

    if args.baseline or args.offline:
        baseline()
    else:
        live(args.target, args.community)
