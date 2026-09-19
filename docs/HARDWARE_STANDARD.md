# Hardware & Runtime Measurement Standard

The project is deployment-oriented. File size alone is never enough.

## Primary constrained device

Main local development target:

- Apple Silicon
- MacBook Air M4
- 16 GB unified memory

Larger hardware may be used for baselines or experiments that cannot fit locally, but cross-device comparisons must be labeled clearly.

## Required runtime measurements

For every serious comparison, record where measurable:

1. **total model weight bytes on disk**;
2. **expert-weight bytes** for MoE models;
3. **resident memory after load**;
4. **peak runtime memory** under a fixed workload;
5. **time to first token (TTFT)**;
6. **generation throughput** in tokens/second;
7. **context length**;
8. **prompt length**;
9. **generated-token count**;
10. **runtime/backend version**;
11. **OS and hardware metadata**;
12. **expert transfer bytes / load count** when offloading is used;
13. **cache hit rate** when expert caching is used;
14. **repeated-run variation**.

Energy/power/temperature measurements may be added when a trustworthy method is available. They must not be inferred from chassis temperature or subjective touch.

## Fixed-workload rule

Baseline and candidate configurations must use equivalent:

- prompt/workload set;
- context length;
- generation length;
- batch/concurrency setting;
- decoding configuration;
- scorer;
- runtime backend where the comparison is intended to be direct;
- thermal/power assumptions as far as practical.

If a backend must differ, state that explicitly and do not attribute all differences to quantization or residency policy.

## Compression and memory ratios

Report these separately:

```text
total_weight_compression =
    baseline_total_weight_bytes / candidate_total_weight_bytes

expert_weight_compression =
    baseline_expert_weight_bytes / candidate_expert_weight_bytes

peak_memory_compression =
    baseline_peak_memory / candidate_peak_memory

resident_memory_compression =
    baseline_resident_memory / candidate_resident_memory
```

Do not merge them into one headline number.

## MoE offload reporting

When experts are not all resident, include:

- resident expert set or policy;
- storage tier used for offloaded experts;
- transferred bytes;
- expert load count;
- cache hit/miss rate where applicable;
- measured stalls or latency impact.

An apparently tiny resident footprint that causes unusable transfer latency is not a deployment win.

## When the baseline cannot fit locally

For a baseline too large for the target device:

- measure it on hardware that can hold it;
- clearly mark any cross-device comparison;
- do not imply a precise local memory ratio that was never measured;
- still test whether the final candidate can run on the target device.

## Thermal and repeatability note

Fanless laptop inference can vary with temperature, background processes, and prior workload. Serious latency/throughput results should use repeated runs, report median plus variation, and distinguish cold-start from warmed sustained behavior.

A single favorable screenshot is not a benchmark.
