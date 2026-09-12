# Project Charter

## Problem

Large open-weight language models are often technically downloadable but practically unusable on consumer hardware because of memory, bandwidth, and runtime constraints. Existing quantization methods reduce storage and memory, but low-bit compression can degrade capability unevenly across models, layers, tasks, and devices.

## Research question

**Can a device-aware quantization system automatically find a compression plan that meaningfully lowers real runtime memory while preserving almost all measurable baseline capability?**

## First research window

- Start: **2026-09-12**
- v0.1 target: **2026-12-12**
- Planned focused effort: roughly **300–350 hours** across 13 weeks

## Scope for v0.1

In scope:

- post-training quantization of open-weight language models;
- Apple Silicon as the primary local target;
- reproducible quality, memory, latency, and throughput measurements;
- reproducing established methods before proposing new ones;
- sensitivity analysis and mixed-precision / mixed-bit experiments;
- automatic search for a safe compression configuration;
- support for several transformer model families.

Out of scope for v0.1:

- claiming universal guarantees across every model and every prompt;
- quantizing closed-weight APIs such as hosted proprietary models;
- training frontier-scale models from scratch;
- proving datacenter cost reductions from laptop experiments;
- claiming that parameter count has been reduced when only representation size changed;
- pretending disk compression equals runtime-memory compression.

## North-star outcome

A user should eventually be able to provide:

- an open-weight model,
- a target device or memory budget,
- an allowed quality-loss threshold,

and receive a validated quantized model plus a report showing exactly what changed.

Conceptually:

```text
open model
   ↓
profile model + device
   ↓
search candidate quantization plans
   ↓
validate quality and runtime
   ↓
select smallest safe candidate
   ↓
export + reproducible report
```

## Scientific standard

A result is publishable in this repository only if:

1. the baseline is frozen before comparison;
2. calibration/search data is separated from held-out final evaluation;
3. hardware and software versions are recorded;
4. raw domain-level scores are preserved;
5. memory is measured at runtime under a fixed workload;
6. the experiment can be repeated from committed code/configuration;
7. negative results are not silently removed.

## Long-term direction

If v0.1 establishes a credible signal, later work may explore:

- better automatic bit allocation;
- model-family transfer of sensitivity information;
- larger-scale server inference;
- 2–3 bit regimes;
- enterprise deployment tooling;
- IP protection for genuinely novel methods before public disclosure.

The 13-week build is a foundation, not a claim that the general quantization problem has been solved.
