# History Log

| Date | Event | What changed | What it replaced/superseded | Source pointer |
|---|---|---|---|---|
| 2026-06-08 | Generated synthetic data | Created `demo_batch_A.csv` and `demo_batch_B.csv` | Replaced placeholder empty files | `tools/make_demo_data.py` |
| 2026-06-09 | Drafted load + clean steps | Pipeline reads and normalizes the demo batches | — | `pipeline/run.py` |
| 2026-06-11 | Added summary step | Produces a summary table (means per column) | Replaced manual spreadsheet step | `pipeline/run.py` |
| 2026-06-13 | Decision: pin random seed | Fixed seed for reproducible output | Superseded non-deterministic runs | This file |
