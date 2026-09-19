# Research Roadmap

This roadmap is evidence-driven. A milestone closes only when its acceptance criteria are present in the repository and can be reproduced from committed code/configuration.

Research window: **2026-09-20 → 2026-12-19**

## M0 — Baseline contract and instrumentation
**Target window:** Sep 20–Oct 02

Objectives:
- select the first supported model/runtime path;
- freeze baseline prompt, context, decoding, and hardware settings;
- record exact model/tokenizer revisions and licenses;
- measure weight storage, resident memory, peak memory, TTFT, and throughput;
- reproduce at least one established quantized baseline.

Acceptance:
- environment capture is machine-readable;
- baseline run is reproducible from a committed config;
- a side-by-side baseline table exists;
- no adaptive policy work begins before this closes.

## M1 — Quantization reproduction and measurement harness
**Target window:** Oct 03–Oct 16

Objectives:
- reproduce simple 8-bit / 4-bit behavior with an established backend;
- compare at least two relevant quantization approaches or runtime formats where feasible;
- automate experiment execution and result capture;
- validate storage calculations against real artifacts.

Acceptance:
- machine-readable result schema;
- repeatable runtime-memory measurement;
- deterministic or explicitly stochastic decoding rules;
- first documented failure analysis.

## M2 — Evaluation reliability
**Target window:** Oct 17–Oct 30

Objectives:
- separate calibration/search data from final held-out evidence;
- build the development evaluation battery;
- freeze initial baseline scores;
- quantify repeated-run variance and scoring uncertainty;
- document deterministic vs judge-based metrics.

Acceptance:
- evaluation version is frozen;
- per-domain reporting works;
- confidence/uncertainty method is documented;
- final held-out data is not reachable from policy search code paths.

## M3 — MoE profiling and expert characterization
**Target window:** Oct 31–Nov 13

Objectives:
- instrument expert routing;
- record expert activation frequency under defined workloads;
- measure expert storage and transfer cost;
- estimate expert/tensor quantization sensitivity;
- identify architecture-specific assumptions.

Acceptance:
- routing-frequency profile;
- sensitivity profile;
- expert cost table;
- at least one visualization or ranked analysis;
- results reproduced on more than one workload slice.

## M4 — Adaptive precision and residency baselines
**Target window:** Nov 14–Nov 27

Objectives:
- establish uniform-bit baseline;
- establish naive/frequency-only residency baseline;
- test mixed-bit expert policies;
- test resident vs offloaded expert policies;
- retain negative results.

Acceptance:
- quality-vs-memory frontier;
- transfer/stall measurements where offload is used;
- direct comparison against simpler baselines;
- no final held-out access during tuning.

## M5 — Joint policy search
**Target window:** Nov 28–Dec 08

Objectives:
- implement automatic candidate generation;
- optimize under explicit memory and measured-quality constraints;
- combine sensitivity, routing frequency, bit-width, and residency choices;
- save the complete search trace for each run.

Acceptance:
- policy format is explicit and serializable;
- every candidate maps to a reproducible config;
- search can be rerun without hidden local state;
- the selected candidate is frozen before final evaluation.

## M6 — Generalization, adversarial validation, and release
**Target window:** Dec 09–Dec 19

Objectives:
- attempt at least three model families or architecture variants;
- test hard/edge-case and longer-context workloads where feasible;
- examine regressions rather than averaging them away;
- reproduce from a clean environment;
- run locked held-out evaluation;
- publish v0.1 technical report and reproducibility bundle.

Acceptance:
- headline claims satisfy SUCCESS_CRITERIA.md;
- failures and unsupported cases are documented;
- install/run instructions work from a clean checkout;
- raw result summaries and frozen configs are committed or immutably referenced;
- release notes separate established evidence from open questions.

## Effort budget

Expected focused effort: approximately **20–25 hours per week**.

Hours are not a success metric. Reproducible evidence is.
