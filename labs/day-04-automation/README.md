# Day 4 - Configuration Automation

Outcomes
- Run a multi-vendor playbook with safe checks.
- Review diffs and capture evidence.

Lab 1 - Basic show playbook
1. Install collections:
   - `ansible-galaxy collection install cisco.ios junipernetworks.junos arista.eos`
2. Ensure Ansible is installed:
   - `pip install ansible-core`
3. Update `examples/inventory.ini` with your lab IPs and creds.
4. Run: `ansible-playbook -i examples/inventory.ini examples/basic_show.yml`.

Lab 2 - Deeper practice (optional)
- Use `modules/gan_clean` playbooks for a larger topology.
- Use `modules/day4-teaching-kit-v2` for guided labs and slides.

Evidence
- Playbook output and any diffs collected in check mode.
