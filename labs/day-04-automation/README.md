# Day 4 - Configuration Automation

Outcomes
- Run a multi-vendor playbook with safe checks.
- Review diffs and capture evidence.

Lab 1 - Basic show playbook
1. Install collections:
   - `ansible-galaxy collection install cisco.ios junipernetworks.junos arista.eos`
2. Ensure Ansible is installed:
   - `pip install ansible-core`
3. Update `docs/lab-topology.yml` with your lab IPs and creds.
4. Run `python3 scripts/generate_inventory.py` to refresh `examples/inventory.ini`.
5. Run: `ansible-playbook -i examples/inventory.ini examples/basic_show.yml`.

Lab 2 - Deeper practice (optional)
- Use `modules/gan_clean` playbooks for a larger topology.
- Use `modules/day4-teaching-kit-v2` for guided labs and slides.

Safety and rollback
- Run in check mode first and review diffs before changes.
- Capture a pre-change snapshot (show commands or config backups).
- Define a rollback plan and validate it in a safe window.
- Limit blast radius with `--limit` or `serial`.

Evidence
- Playbook output and any diffs collected in check mode.

Student checklist
- Inventory updated with real IPs and creds.
- Playbook completed without fatal errors.
- Output saved or pasted into notes.
- One improvement idea captured.
- Rollback plan noted.
