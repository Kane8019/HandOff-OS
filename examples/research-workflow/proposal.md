# Proposal

## Goal

Add a chart step to the synthetic-data pipeline so a reader can see the per-batch
summary at a glance, and make the whole pipeline reproducible from a clean
checkout.

## Decision needed

Approval of the chart approach (one combined chart vs. one per batch) and the
output format before implementing.

## Scope

- Add a chart step that renders the existing summary table to a PNG.
- Use only the synthetic inputs `demo_batch_A.csv` and `demo_batch_B.csv`.
- Keep the pinned random seed so output is identical across runs.

## Out of scope

- Any real dataset.
- External data sources or network fetches.
- Statistical modeling beyond simple summaries.

## Reversibility

Fully reversible — it's local code producing local files. Delete the output and
re-run. No outside party involved.

## Risks

- Low. Worst case is an ugly chart, fixed by re-running. The only real risk to
  guard against is accidentally pointing the pipeline at non-synthetic data,
  which is explicitly out of scope.

## Requested approval

Owner approval of the combined-chart approach and PNG output.

## Execution notes

Implement the chart step, run end-to-end on the synthetic batches, confirm the
output is byte-stable across two runs (seed pinned), then log the result.
