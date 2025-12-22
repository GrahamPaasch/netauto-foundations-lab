# Troubleshooting

Common issues
- Cannot reach devices: verify VPN or jump host access and confirm IPs in `docs/lab-topology.md`.
- Auth failures: confirm username and password and check device line settings.
- Netconf errors: ensure netconf is enabled on the device.
- Ansible errors: confirm `ansible_network_os` and connection type in inventory.

If stuck
- Capture the error, the command you ran, and device name.
- Ask for help with the smallest reproducible steps.
