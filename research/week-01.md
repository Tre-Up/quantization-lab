# Week 01 — Foundations + First Baseline

**Dates:** 2026-09-12 → 2026-09-18

## Goal

By the end of this week, quantization must stop being an abstract idea. We need one small open model, one clean baseline, one quantized comparison, and one reproducible measurement table.

## Learning targets

Be able to explain plainly:

- bit vs byte;
- FP32, FP16/BF16, INT8, INT4;
- why 16-bit weights to 4-bit weights suggests about 4× theoretical weight compression;
- why actual runtime memory is not equal to file size;
- scale / zero-point;
- symmetric vs asymmetric quantization;
- per-tensor vs per-channel/per-group quantization;
- group size;
- quantization error;
- model weights vs KV cache;
- what a transformer linear layer is doing at a high level.

## Build targets

- [ ] local Python environment working;
- [ ] `qlab doctor` runs;
- [ ] choose one small open-weight model that comfortably fits the M4/16 GB machine;
- [ ] record exact model revision and license;
- [ ] run the baseline model locally;
- [ ] record baseline weight size;
- [ ] record peak runtime memory under a fixed prompt/workload;
- [ ] record latency and tokens/sec;
- [ ] run at least one established quantized variant under the same workload;
- [ ] create the first side-by-side result table;
- [ ] write one experiment log using the template.

## First table

Do not fill this from guesses.

| Variant | Weight size | Peak RAM | TTFT | tok/s | Quality smoke test |
|---|---:|---:|---:|---:|---:|
| Baseline | TBD | TBD | TBD | TBD | TBD |
| Quantized A | TBD | TBD | TBD | TBD | TBD |

## Week 1 quality test

Do **not** build the full 10k+ evaluation suite this week.

Use a small smoke set only to detect catastrophic regressions while the measurement tooling is being built. The serious benchmark begins later.

## End-of-week acceptance gate

Week 1 is complete only if another person can look at the repository and answer:

1. Which model did we test?
2. Which exact version?
3. How large was the baseline?
4. How much RAM did it really use?
5. What quantized version did we compare?
6. Was the comparison run under the same settings?
7. Can the experiment be repeated?

## Forbidden distractions this week

- patent strategy deep dives;
- 120B/800B model fantasies;
- inventing a custom quantizer before understanding the baseline;
- buying new hardware;
- spending hours polishing launch graphics;
- chasing GitHub stars.

Week 1 has one job: **measure reality correctly.**
