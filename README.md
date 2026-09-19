# quantization-lab

Research tooling for **device-aware quantization and efficient Mixture-of-Experts (MoE) inference on constrained hardware**.

The project investigates a systems question:

> **Can quantization precision and expert residency be selected jointly from model sensitivity, routing behavior, and device constraints to reduce real inference cost without materially degrading measured capability?**

The primary target device is Apple Silicon with a **16 GB unified-memory budget**. The repository treats storage size, resident/peak memory, latency, throughput, and measured capability as separate quantities. A smaller file is not considered a deployment win if runtime behavior gets worse.

## Research direction

The working hypothesis is that uniform quantization leaves useful structure on the table. In an MoE model, experts differ in at least three ways that may matter for constrained-device inference:

- **quantization sensitivity** — how much measured behavior changes when an expert is compressed;
- **routing frequency** — how often an expert is selected under a defined workload;
- **residency cost** — how expensive it is to keep or fetch that expert on a target device.

The project will test whether those signals can support a joint policy:

```text
model + device budget
        ↓
runtime / routing profile
        ↓
expert sensitivity profile
        ↓
candidate bit-width + residency policies
        ↓
development evaluation
        ↓
frozen candidate
        ↓
held-out evaluation + runtime validation
        ↓
reproducible artifact and report
```

No novelty claim is made by the existence of this pipeline. Novelty, if any, must be established against prior work and supported by experiments.

## v0.1 research targets

The v0.1 program aims to demonstrate:

- reproducible baselines for established quantization and MoE inference paths;
- validation across **at least three open-weight model families or architecture variants**, where technically appropriate;
- **≥3× expert-weight storage compression** relative to FP16/BF16 baselines for the headline configuration;
- **≥99% aggregate measured quality retention** on a locked held-out evaluation protocol;
- lower **peak/resident memory** than a comparable uniform-quantized MoE baseline;
- real-device measurements on **Apple Silicon / 16 GB unified memory**;
- an automatic policy that can consider both **precision** and **expert residency** under an explicit device budget;
- reproducible configs, raw metrics, software versions, hardware metadata, and negative results.

### Stretch targets

Stretch outcomes include:

- approximately **4× or better expert-weight compression** while retaining **≥99.9% measured quality** on the locked protocol;
- measurable energy or sustained-thermal improvement under a fixed workload;
- useful expert prefetch/cache behavior without unacceptable latency;
- independent reproduction on another machine.

These are research targets, not promised outcomes.

## Measurement standard

Headline results separate:

1. weight storage;
2. resident and peak runtime memory;
3. time to first token;
4. generation throughput;
5. expert load / transfer behavior where applicable;
6. measured quality retention;
7. uncertainty and per-domain scores.

The final held-out battery is never used to tune bit widths, group sizes, residency decisions, cache rules, or search termination.

See [Evaluation Standard](docs/EVALUATION_STANDARD.md), [Hardware Standard](docs/HARDWARE_STANDARD.md), and [Experiment Protocol](docs/EXPERIMENT_PROTOCOL.md).

## Repository structure

```text
quantization-lab/
├── README.md
├── PROJECT_CHARTER.md
├── GOALS.md
├── ROADMAP.md
├── SUCCESS_CRITERIA.md
├── CHANGELOG.md
├── CONTRIBUTING.md
├── SECURITY.md
├── pyproject.toml
│
├── src/quantization_lab/   # implementation
├── tests/                  # cheap deterministic tests
├── benchmarks/             # benchmark definitions and adapters
├── configs/                # frozen experiment / model / device configs
├── experiments/            # experiment records and reproduction commands
├── results/                # compact machine-readable result summaries
├── research/               # hypotheses, experiment index, negative results
└── docs/                   # architecture, evaluation, runtime and methodology
```

Large model weights and bulky benchmark artifacts do not belong in Git. Immutable model revisions, checksums, configs, and artifact references do.

## Current status

**Foundation / instrumentation.**

The repository currently contains the research contract, evaluation standards, experiment protocol, and a minimal `qlab doctor` utility. It does **not** yet claim a new quantization method, a compression result, a memory win, or a quality-retention result.

The next milestone is a frozen, reproducible baseline on the target device before adaptive MoE policies are attempted.

See [Current Status](docs/CURRENT_STATUS.md) and [Roadmap](ROADMAP.md).

## Development

```bash
python -m pip install -e ".[dev]"
qlab doctor
pytest
```

## Research rule

> **Results earn claims. Claims do not earn results.**
