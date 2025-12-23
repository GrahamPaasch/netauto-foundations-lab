# Lab Topology

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

After updating this table, run `python3 scripts/generate_baselines.py` to refresh Day 1 baselines.
