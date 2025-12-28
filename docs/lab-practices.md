# Lab Practices

Credential handling
- Keep real credentials out of version control. Treat `docs/lab-topology.yml` as local-only.
- If you must share the repo, replace usernames/passwords with placeholders first.
- Prefer environment variables or a password manager for long-lived secrets.

Safety and rollback
- Run pre-checks and check mode before making changes.
- Capture a pre-change snapshot (show commands or config backups).
- Define a rollback plan and validate it in a safe window.

Logging and evidence
- Keep a run log with timestamp, command, targets, and result.
- Store logs under `evidence/logs/` (or `outputs/logs/` if you stay in lab folders).
- Link artifacts in your daily recap.

Test mindset
- Unit-style checks validate your environment without touching devices.
- Integration checks validate the lab against live devices.
- Run `./scripts/sanity_check.sh` before Day 1 and after major changes.

Performance choices
- Sequential: simplest; best for small sets or debugging.
- Asyncio: best for high-latency I/O with many devices.
- Threaded: best for blocking libraries that lack async support; cap concurrency.
