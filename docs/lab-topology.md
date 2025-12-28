# Lab Topology

This file is generated from `docs/lab-topology.yml`. Edit that file and re-run `python3 scripts/generate_inventory.py`.

This course expects a small multi-vendor lab with a jump host.

If you synced modules, look here for topology assets:
- `modules/introduction_to_python_for_networking_five_day_course/click_me_09_gns3_assets/gns3/topology-diagram.png`
- `modules/introduction_to_python_for_networking_five_day_course/click_me_09_gns3_assets/gns3/login-table.md`

Fill in the table below for quick reference.

| Hostname | Platform | Mgmt IP | Username | Password | Notes |
| --- | --- | --- | --- | --- | --- |
| r1 | ios | 10.0.0.11 | user | pass | edge |
| sw1 | eos | 10.0.0.12 | user | pass | dist |
| j1 | junos | 10.0.0.21 | user | pass | core |
| jump | linux | 10.0.0.5 | user | pass | jump-host |

After updating the source of truth, run `python3 scripts/generate_inventory.py` to refresh generated files.
