import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FIXTURE = ROOT / "fixtures" / "api_response.json"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)


def load_offline():
    return json.loads(FIXTURE.read_text())


def load_live(url):
    try:
        import requests
    except ImportError:
        print("requests is not installed. Run offline mode or install requirements.")
        return None
    resp = requests.get(url, timeout=5)
    resp.raise_for_status()
    return resp.json()


def normalize(data):
    interfaces = []
    for iface in data.get("interfaces", []):
        interfaces.append({
            "name": iface.get("name"),
            "admin_up": iface.get("admin") == "up",
            "oper_up": iface.get("oper") == "up",
            "ip": iface.get("ip"),
        })
    return {"device": data.get("device"), "interfaces": interfaces}


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="optional live API endpoint")
    args = parser.parse_args()

    raw = load_live(args.url) if args.url else load_offline()
    if raw is None:
        raise SystemExit(1)
    normalized = normalize(raw)

    out_path = OUTPUTS / "api_normalized.json"
    out_path.write_text(json.dumps(normalized, indent=2))
    print(f"Wrote {out_path}")
