# Project Context

Status: In progress
Sensitivity: Low (synthetic data only, no real datasets or systems)
Project purpose: Build a small, reproducible data-analysis pipeline that
summarizes a synthetic demo dataset and produces a chart.
Current state: Pipeline drafted; runs end-to-end on `demo_batch_A.csv` and
outputs a summary table. Chart step is stubbed.
Next action: Implement the chart step, then review reproducibility before
sharing the notebook.

## Active decisions

- Use only **synthetic** inputs (`demo_batch_A.csv`, `demo_batch_B.csv`). No real
  data enters this demo.
- Pin the random seed so results are reproducible.
- Outputs: one summary table (CSV) and one chart (PNG).

## Boundaries

- In scope: load → clean → summarize → chart on synthetic data.
- Out of scope: real datasets, external data sources, model training, any
  network fetches.
- No identifiers of real samples, instruments, servers, or people.

## Source pointers

- Synthetic inputs: `data/demo_batch_A.csv`, `data/demo_batch_B.csv` (generated)
- Pipeline: `pipeline/run.py` (fictional path)
- Generator for the synthetic data: `tools/make_demo_data.py` (fictional path)

## Open questions

- Should the summary include medians as well as means? (Cheap to add.)
- One combined chart or one per batch? Leaning combined.

## Unresolved high-consequence items

- None. All data is synthetic and nothing is published or sent. This stays
  low-consequence unless real data is ever substituted — which is out of scope.
