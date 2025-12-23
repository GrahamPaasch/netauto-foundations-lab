# Day 1 - Foundations and Connectivity

Outcomes
- Build an inventory from structured data.
- Validate connectivity with baselines and then live.
- Capture evidence for review.

About baselines
- Baselines are sample datasets used for practice or when the lab is unavailable.
- In the live GNS3 lab, treat baselines as a quick check or skip baseline mode after you confirm access.

Lab 1 - Inventory
1. Review baselines in `baselines/devices.json`.
2. If you updated `docs/lab-topology.md`, run `python3 scripts/generate_baselines.py`.
3. Run the example: `python3 examples/inventory.py`.
4. Check outputs in `outputs/`.
5. Update `baselines/devices.json` with your lab IPs and rerun.

Lab 2 - Connectivity
1. Run baseline mode: `python3 examples/connectivity.py --baseline`.
2. Review `outputs/connectivity.csv`.
3. Run live mode: `python3 examples/connectivity.py`.
4. Compare live results to the baseline snapshot.

Evidence
- Save `outputs/inventory.csv` and `outputs/connectivity.csv`.
- Write a short recap: what worked, what failed, and what you need for Day 2.

Student checklist
- Inventory generated from baselines or live data.
- Connectivity run in baseline mode and live mode.
- Evidence saved in `outputs/`.
- Two issues or questions noted for Day 2.
