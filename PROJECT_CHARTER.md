# Project Charter

## Problem

Large open-weight language models are increasingly capable, but local inference is constrained by more than model-file size. Real deployments are limited by resident memory, peak memory, memory bandwidth, expert transfers, latency, throughput, energy, and sustained thermal behavior.

Quantization reduces representation cost, while Mixture-of-Experts (MoE) architectures reduce active computation by routing tokens through a subset of experts. These mechanisms solve different parts of the deployment problem and are often configured independently.

## Research question

**Can a device-aware system jointly select quantization precision and expert residency from measured sensitivity, routing behavior, and hardware constraints to reduce real MoE inference cost while preserving baseline capability as tightly as possible?**

## Research window

- Start: **2026-09-20**
- v0.1 target: **2026-12-19**
- Focused effort budget: roughly **20–25 hours per week**

Calendar time is not evidence. Milestones close only when the required measurements and artifacts exist.

## Scope for v0.1

In scope:

- post-training quantization of open-weight models;
- MoE models and expert-level profiling;
- Apple Silicon as the primary constrained-device target;
- reproducible quality, memory, latency, throughput, and expert-transfer measurements;
- established quantization and MoE baselines before custom policy search;
- expert/tensor sensitivity analysis;
- routing-frequency measurement;
- mixed-bit / mixed-precision policies;
- expert residency, cache, and offload experiments;
- automatic search under explicit memory and quality constraints;
- validation across multiple model families or architecture variants where feasible.

Out of scope for v0.1:

- claiming that quantization reduces parameter count;
- converting arbitrary dense models into competitive MoE models as a primary objective;
- training frontier-scale models from scratch;
- claiming universal equivalence across every prompt;
- proving datacenter economics from laptop experiments;
- hiding SSD traffic, temporary buffers, KV-cache cost, or dequantization overhead;
- claiming novelty before a serious prior-art review.

## North-star outcome

A user should eventually be able to provide:

- a supported open-weight MoE model;
- a target device or memory budget;
- an allowed measured quality-loss threshold;

and receive a validated deployment policy describing, where supported:

- expert/tensor bit width;
- group size or quantization scheme;
- expert residency / offload policy;
- cache or prefetch decisions;
- expected storage and runtime-memory cost;
- measured quality and runtime evidence.

## Scientific standard

A publishable headline result must satisfy all of the following:

1. baseline configuration is frozen before comparison;
2. calibration/search data is separated from final held-out evaluation;
3. exact model/tokenizer revisions are recorded;
4. hardware and software versions are recorded;
5. raw per-domain scores are preserved;
6. peak and resident memory are measured under fixed workloads;
7. transfer/offload behavior is reported when it materially affects the result;
8. latency and throughput are repeated rather than taken from one favorable run;
9. experiments are reproducible from committed code/configuration;
10. negative results are retained when they affect interpretation.

## Working hypothesis

The project will test, rather than assume, that expert-level heterogeneity is useful for deployment. A candidate joint policy may benefit from signals such as:

```text
expert sensitivity
× routing frequency
× storage / transfer cost
× device memory budget
```

Examples of possible policy decisions include keeping a frequently used sensitive expert resident at higher precision while storing a rarely used tolerant expert at lower precision and loading it on demand.

This is a hypothesis, not a result.

## Long-term direction

If v0.1 establishes a credible signal, later work may explore:

- predictive expert prefetch;
- cross-model transfer of sensitivity or routing priors;
- KV-cache quantization and context-aware budgeting;
- lower-bit regimes;
- custom Metal/CUDA kernels;
- server-scale inference;
- hardware-aware learned policies;
- IP protection for genuinely novel mechanisms before disclosure.
