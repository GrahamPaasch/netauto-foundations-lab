# Syllabus

Course goals
- Build confidence with Python for network tasks.
- Produce repeatable workflows for inventory, connectivity, and config changes.
- Learn to plan, validate, and apply changes with evidence.

Course-wide practices
- Use safe change workflows with pre-checks and rollback plans.
- Handle credentials safely and keep secrets out of version control.
- Capture logs and evidence for every lab run.
- Apply a test mindset: unit-style checks before live integration.
- Choose the right concurrency model for I/O tasks.

Day 0 - Setup
- Environment bootstrap
- Lab access checks

Day 1 - Foundations and connectivity
- Build an inventory dataset
- Validate reachability with live tests
- Use asyncio to run concurrent reachability checks
- Deliverable: inventory CSV and connectivity report

Day 2 - Observability basics (SNMP and syslog)
- Poll SNMP and parse syslog samples
- Deliverable: metrics summary and alert rules

Day 3 - APIs and data modeling
- Call REST endpoints and normalize data
- Deliverable: normalized device data in JSON and a small report

Day 4 - Configuration automation (Ansible)
- Build multi-vendor playbooks with safety checks
- Deliverable: check mode diff and apply plan

Day 5 - Intent capstone
- Express intent, generate plan, review evidence, and apply
- Deliverable: plan/apply artifacts and a short recap
