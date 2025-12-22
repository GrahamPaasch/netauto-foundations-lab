import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LOG_PATH = ROOT / "fixtures" / "syslog_sample.log"
OUTPUTS = ROOT / "outputs"
OUTPUTS.mkdir(exist_ok=True)

pattern = re.compile(r"^(\w{3} +\d+ +\d+:\d+:\d+) (\S+) (.*)$")

records = []
for line in LOG_PATH.read_text().splitlines():
    match = pattern.match(line)
    if not match:
        continue
    ts, host, msg = match.groups()
    records.append({"timestamp": ts, "host": host, "message": msg})

out_path = OUTPUTS / "syslog_parsed.json"
out_path.write_text(json.dumps(records, indent=2))
print(f"Wrote {out_path}")
