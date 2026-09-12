# quantization-lab

A 13-week open research build focused on one question:

> **How far can an open-weight language model be compressed for local inference before measurable capability meaningfully degrades?**

The project starts on **2026-09-12** and targets a first serious public release on **2026-12-12**.

## Mission

Build a reproducible, device-aware quantization system that reduces the real memory cost of running large language models while preserving as much baseline capability as possible.

The project is deliberately not defined as “make every model 4-bit.” The long-term system should inspect a model, measure what is sensitive, search for a safe compression plan, validate the result against the original model, and export something people can actually run on constrained local hardware.

## 13-week target

The primary research target for v0.1 is:

- support **at least 3 open-weight model families**;
- demonstrate **~4× weight-storage compression** against FP16/BF16 baselines where the architecture permits it;
- target **≥99% measured quality retention** on a predefined held-out evaluation battery;
- measure **peak runtime memory**, not just file size;
- report latency and throughput alongside quality;
- produce reproducible results on Apple Silicon, with a **MacBook Air M4 / 16 GB unified memory** as the main constrained-device target;
- make every published result reproducible from scripts and frozen configs.

### Stretch target

**≥5× compression with ≥99.9% measured quality retention** on the locked evaluation protocol.

That is a research target, not a promised result. If the experiments do not support it, the repository will report the failure rather than manufacture a victory.

## What “quality” means here

“99.9% quality” does **not** mean the model is 99.9% factually correct or identical on every possible prompt. It means the quantized model retains 99.9% of the original model’s measured score on a frozen, diverse, held-out evaluation protocol.

See [`docs/EVALUATION_STANDARD.md`](docs/EVALUATION_STANDARD.md).

## What counts as compression

We report several numbers separately:

1. **Weight storage**: bytes used by model weights.
2. **Peak runtime memory**: highest measured memory while running a fixed workload.
3. **Latency**: time to first token and end-to-end response time.
4. **Throughput**: generated tokens per second under a fixed setup.
5. **Measured quality retention**: quantized score relative to the original baseline.

A tiny model file that expands into an unusable runtime is not considered a success.

## Research principles

- Baseline first. No custom method is trusted until existing methods are reproduced.
- Held-out evaluation. Search/calibration data must not be reused as final evidence.
- No cherry-picking. Failed experiments stay in the log.
- No fake precision. Confidence intervals and raw per-domain scores accompany headline numbers.
- Device reality matters. Disk size alone is not a deployment metric.
- Reproducibility beats screenshots.

## Repository map

```text
quantization-lab/
├── README.md
├── PROJECT_CHARTER.md
├── GOALS.md
├── ROADMAP.md
├── SUCCESS_CRITERIA.md
├── CONTRIBUTING.md
├── SECURITY.md
├── CHANGELOG.md
├── pyproject.toml
├── docs/
│   ├── ARCHITECTURE.md
│   ├── BENCHMARK_PLAN.md
│   ├── EVALUATION_STANDARD.md
│   ├── EXPERIMENT_PROTOCOL.md
│   ├── FAILURE_MODES.md
│   ├── HARDWARE_STANDARD.md
│   ├── IP_AND_LICENSING.md
│   ├── LEARNING_PATH.md
│   ├── OSS_GROWTH.md
│   ├── READING_LIST.md
│   └── REPRODUCIBILITY.md
├── research/
│   ├── README.md
│   ├── experiment-template.md
│   └── week-01.md
├── benchmarks/
│   └── README.md
├── src/quantization_lab/
│   ├── __init__.py
│   ├── __main__.py
│   └── cli.py
└── tests/
    └── test_smoke.py
```

## Current status

**Week 0 / foundation.** No compression result is claimed yet. The first milestone is to establish a clean baseline and measurement harness on a small open model before attempting any original quantization method.

## Development command

Once installed in editable mode, the initial utility is:

```bash
qlab doctor
```

It reports the local environment and hardware basics. Quantization commands will only be added after their behavior is implemented and tested.

## Licensing

No final software license has been selected yet. This is intentional while the project evaluates a long-term model that keeps individual/research use broadly accessible while preserving options for commercial licensing and future IP protection. See [`docs/IP_AND_LICENSING.md`](docs/IP_AND_LICENSING.md).

---

**Rule for this repository:** results earn claims. Claims do not earn results.
