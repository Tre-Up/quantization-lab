# 13-Week Roadmap

This roadmap is output-driven. A week is complete only when its evidence exists in the repository.

## Week 1 — Foundations + first baseline

Learn the minimum required concepts, set up the environment, choose a small open model, and produce the first baseline table.

Deliverables:
- environment doctor passes;
- one small model runs locally;
- baseline weight size, peak memory, latency, throughput recorded;
- at least one existing quantized variant measured under the same workload;
- first research log completed.

## Week 2 — Quantization fundamentals in practice

Reproduce simple 8-bit and 4-bit quantization with an established toolchain.

Deliverables:
- reproducible commands/configs;
- side-by-side baseline vs 8-bit vs 4-bit measurements;
- explanation of scales, groups, symmetric/asymmetric quantization in your own words;
- first failure analysis.

## Week 3 — Reproduce established methods

Compare at least two established approaches/backends where feasible.

Deliverables:
- frozen comparison protocol;
- same model, same prompts, same device, same context length;
- quality + runtime table.

## Week 4 — Measurement harness

Stop doing manual measurements.

Deliverables:
- automated experiment runner;
- machine-readable result format;
- repeatable peak-memory measurement;
- deterministic decoding settings;
- environment/version capture.

## Week 5 — Evaluation battery v1

Build the first serious quality test suite.

Deliverables:
- separate calibration/search and held-out splits;
- multiple domains such as math, reasoning, knowledge, coding, and instruction following;
- baseline scores frozen;
- aggregate metric plus per-domain reporting.

## Week 6 — Reliability of the benchmark

Test the test.

Deliverables:
- repeated-run variance analysis;
- scoring bugs checked;
- bootstrap confidence intervals or an equivalent uncertainty report;
- documented judge-based metrics separated from deterministic metrics.

## Week 7 — Sensitivity analysis

Measure which model components tolerate compression and which do not.

Deliverables:
- layer/tensor sensitivity experiment;
- at least one visualization or ranked table;
- hypothesis for mixed-bit allocation.

## Week 8 — Mixed-bit experiments

Test whether selective precision beats uniform quantization at the same memory budget.

Deliverables:
- fixed-bit baseline;
- at least several mixed-bit candidates;
- quality-vs-memory frontier plot/table;
- negative results retained.

## Week 9 — Automatic search v0

Turn manual tuning into an algorithm.

Deliverables:
- candidate-generation/search logic;
- explicit memory budget and quality constraint;
- search trace saved for every run;
- no access to final held-out set during search.

## Week 10 — Generalization

Run the method on additional model families.

Deliverables:
- at least 3 model families attempted;
- failures documented rather than removed;
- model-family-specific assumptions identified.

## Week 11 — Larger model validation

Scale beyond toy models.

Deliverables:
- 7B/9B-class serious validation;
- larger model attempted if compute permits;
- cloud/borrowed hardware used only where local hardware is genuinely insufficient;
- local Apple Silicon deployment tested for the final artifact where feasible.

## Week 12 — Adversarial validation

Try to break the headline claim.

Deliverables:
- hard/edge-case suite;
- long-context check where feasible;
- domain regressions examined;
- independent reproduction attempt from a clean environment.

## Week 13 — v0.1 release

No last-minute benchmark invention.

Deliverables:
- locked results;
- clean install/run instructions;
- technical report;
- changelog and release notes;
- reproducibility bundle;
- clear list of what worked, what failed, and what remains unknown.

## Effort budget

Target: roughly **25 focused hours per week**, around **300–350 focused hours total**.

Hours are not a success metric. Evidence is.
