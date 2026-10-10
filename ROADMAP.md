# Research Roadmap

The public research foundation was established on **2026-09-12**, and the MoE direction was documented on **2026-09-19**. Those historical dates and their corresponding commits remain unchanged.

**Active execution restarts on 2026-10-10 (Day 1 of the new execution cycle).** The earlier planning windows were not completed on schedule. Milestones close through reproducible evidence, not elapsed days or GitHub activity alone.

## Execution schedule (targets, not completed work)

| Milestone | Planning window | Evidence required |
| --- | --- | --- |
| M0 — Freeze first reproducible baseline | Oct 10–16, 2026 | Exact model/tokenizer revision, device/runtime config, environment capture, initial full/reference measurements and repeatable command |
| M1 — Quantized baseline and measurement harness | Oct 17–30 | Compare established baseline paths under equivalent conditions, record memory, TTFT, throughput, repeated runs and failures |
| M2 — Evaluation reliability | Oct 31–Nov 13 | Frozen evaluation protocol, dev/held-out isolation, per-domain scores and run uncertainty |
| M3 — MoE routing and sensitivity profiling | Nov 14–27 | Expert activation, sensitivity and transfer profiles measured across workload slices |
| M4 — Mixed precision and residency baselines | Nov 28–Dec 11 | Uniform / frequency-only comparisons, runtime memory and latency evidence, negative results |
| M5 — Joint precision + residency search | Dec 12–25 | Reproducible candidate policy, constrained search and frozen candidate before final evaluation |
| M6 — Validation and v0.1 technical report | Dec 26–Jan 16, 2027 | Attempt multiple architecture variants, locked evaluation and reproducibility bundle |

The dates are **provisional** and may change with hardware access and actual results. Do not label a stage completed until its evidence is committed or immutably referenced.

## First seven days (Oct 10–16)

1. Review the measurement metadata validator in [PR #7](https://github.com/Tre-Up/quantization-lab/pull/7). Its synthetic tests check contracts, not model performance.
2. Identify and pin a feasible first open-weight model, its tokenizer, revision and license.
3. Freeze the Apple Silicon / 16 GB machine and runtime configuration, workload, seeds and decoding rules.
4. Run a real reference baseline locally and preserve raw metrics and logs.
5. If supported by the chosen runtime, reproduce an established quantized baseline under comparable settings.
6. Write a short report including failures and limitations, and verify it from a clean checkout.
7. Review the next experiments based on measured evidence. **No benchmark result is assumed in advance.**

## Principles

- Keep historical plans in Git history; do not rewrite their dates to imply earlier execution.
- Keep experimental reports honest about actual hardware and unmeasured fields.
- Distinguish weight size, resident/peak memory, latency, throughput and measured capability.
- Do not tune against the locked final held-out evaluation.
- Separate research targets from demonstrated outcomes.
