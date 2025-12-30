# NetBox Import Data (from Nmap)

These CSVs are generated from Nmap XML or the summary markdown and are intended for NetBox's CSV import.

Import order (recommended):
1. sites.csv
2. manufacturers.csv
3. device_roles.csv
4. device_types.csv
5. platforms.csv
6. prefixes.csv
7. ip_addresses.csv
8. devices.csv

Notes:
- IP addresses are imported unassigned. Assign them to interfaces later in NetBox.
- Device roles/types/platforms are best-effort based on OS guesses and hostnames.
- Junos enrichment adds `serial` and augments device comments with model/Junos/LLDP chassis ID.
- Rerun with a different site or prefix:
  python3 scripts/nmap_to_netbox.py --xml /path/to/scan.xml --out netbox --site YOUR-SITE --prefix 10.0.0.0/16
  python3 scripts/nmap_to_netbox.py --md docs/nmap-inventory.md --out netbox --site YOUR-SITE --prefix 10.0.0.0/16

Enrichment (Junos evidence logs):
  python3 scripts/enrich_netbox_from_junos.py --evidence evidence/logs --netbox netbox
