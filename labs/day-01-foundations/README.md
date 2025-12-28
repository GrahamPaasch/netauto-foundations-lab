# Day 1 - Foundations and Connectivity

Outcomes
- Build an inventory from live lab data.
- Validate connectivity against the live lab.
- Compare sequential and asyncio-based reachability checks.
- Capture evidence for review.

Lab 1 - Inventory
1. Update `docs/lab-topology.yml` with current lab IPs and creds.
2. Run `python3 scripts/generate_inventory.py`.
3. Run the example: `python3 examples/inventory.py`.
4. Check outputs in `outputs/`.

Lab 2 - Connectivity
1. Run: `python3 examples/connectivity.py`.
2. Review `outputs/connectivity.csv`.

Lab 3 - Asyncio connectivity (optional)
1. Run: `python3 examples/connectivity_asyncio.py`.
2. Review `outputs/connectivity_asyncio.csv`.
3. Compare results with `outputs/connectivity.csv`.

Performance notes
- Sequential: simplest; best for small sets or debugging.
- Asyncio: best for high-latency I/O with many devices (tune `CONCURRENCY`).
- Threaded: best for blocking libraries that lack async support; cap threads.

Evidence
- Save `outputs/inventory.csv` and `outputs/connectivity.csv`.
- Optional: save `outputs/connectivity_asyncio.csv`.
- Write a short recap: what worked, what failed, and what you need for Day 2.

Student checklist
- Inventory generated from live lab data.
- Connectivity run against the live lab.
- Evidence saved in `outputs/`.
- Two issues or questions noted for Day 2.
- Optional: asyncio connectivity report generated.
