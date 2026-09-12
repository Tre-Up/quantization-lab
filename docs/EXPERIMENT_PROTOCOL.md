# Experiment Protocol

Every serious experiment should be boring to reproduce. Boring is good; it means the result is less likely to be an accident.

## Before the run

Record:

- experiment ID;
- date;
- hypothesis;
- model name and exact revision;
- quantization method/backend;
- candidate settings;
- calibration/search data identity;
- evaluation split identity;
- hardware;
- software/runtime versions;
- decoding settings.

## During the run

Capture machine-readable outputs for:

- weight size;
- load success/failure;
- peak runtime memory;
- latency;
- throughput;
- benchmark scores;
- warnings/errors;
- random seed where relevant.

## After the run

Write:

- result;
- whether the hypothesis was supported;
- what failed;
- what changed versus the previous run;
- the next experiment justified by the result.

## One-variable principle

When diagnosing a mechanism, change one meaningful variable at a time whenever possible. If multiple settings change together, label the run as a system-level comparison rather than pretending to know which change caused the effect.

## Search discipline

The automatic optimizer may use development/calibration data. It may not query the final held-out battery while searching.

## Failed runs

A failed run is still data. Keep the record if it teaches something or changes the next decision.

Do not delete failed evidence merely because the README would look prettier without it.

## Naming

Recommended experiment ID:

```text
YYYYMMDD-model-method-purpose-NNN
```

Example:

```text
20260919-smallqwen-int4-baseline-001
```

## Promotion rule

An experiment result may become a README/headline claim only after:

1. reproduction from a clean config;
2. held-out evaluation;
3. runtime measurement;
4. review for accidental data leakage;
5. raw artifacts are committed or linked immutably where size prevents committing them.
