import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

pattern = re.compile(r"^(\w{3} +\d+ +\d+:\d+:\d+) (\S+) (.*)$")

def parse_file(path):
    records = []
    for line in Path(path).read_text().splitlines():
        match = pattern.match(line)
        if not match:
            continue
        ts, host, msg = match.groups()
        records.append({"timestamp": ts, "host": host, "message": msg})
    return records


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--path", required=True, help="path to syslog file")
    args = parser.parse_args()

    records = parse_file(args.path)
    out_path = OUTPUTS / "syslog_parsed.json"
    out_path.write_text(json.dumps(records, indent=2))
    print(f"Wrote {out_path}")
