# Baseline manifest contract (v1)

This small validator is part of preparing a reproducible first local baseline (M0/M1). It is **not** a benchmark runner, a quantization result, or evidence that any model has been measured.

## Validate a real measurement record

After you have recorded a baseline on your own device, store the measurement fields in a JSON record and run:

```bash
python -m quantization_lab.baseline path/to/baseline.json
```

Or from Python:

```python
from quantization_lab.baseline import load_and_validate_manifest

record = load_and_validate_manifest("path/to/baseline.json")
```

The record must include:

| Section | Required fields |
| --- | --- |
| root | schema_version (1), experiment_id, timestamp_utc, source_commit |
| model | id, revision, tokenizer_revision, license |
| device | name, memory_bytes |
| runtime | name, version, quantization_format |
| workload | dataset_id, dataset_revision, decoding_config_id, context_tokens, generated_tokens, seed |
| metrics | weight_storage_bytes, resident_memory_bytes, peak_memory_bytes, ttft_ms, tokens_per_second, repetitions |

Numbers must be finite and non-negative where appropriate. Peak memory may not be smaller than resident memory. Model and runtime revision fields are mandatory to reduce accidental incomparable results.

## Scope and research integrity

- A structurally valid record is **not evidence** that a measurement was performed.
- No placeholder or synthetic test value should be represented as a real device result.
- The test suite uses fake data strictly to check validation behavior.
- The validator cannot verify the truth of timestamps, revisions, licenses, runtime measurements, tokenizer behavior, or hardware statistics.
- Record raw run logs, command lines, environment versions, and exact upstream model revisions with any real experiment.
- The next milestone remains a frozen baseline on the target Apple Silicon device and a fair, separately measured quantized comparison.

This contract is meant to prevent incomplete measurement records, not substitute for execution and external reproducibility.
