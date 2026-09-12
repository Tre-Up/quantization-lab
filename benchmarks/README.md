# Benchmarks

This directory will contain benchmark configuration, adapters, and small metadata files. Large datasets should not be blindly copied into the repository.

## Separation policy

Keep three classes of evaluation distinct:

```text
calibration/
development/
held_out/
```

The final held-out battery is not available to the quantization search logic.

## Planned result format

Each benchmark run should eventually emit machine-readable records containing:

- benchmark name/version;
- split;
- item count;
- baseline score;
- candidate score;
- absolute delta;
- retention;
- confidence interval where applicable;
- model revision;
- quantization policy ID;
- runtime/environment metadata.

## Data licensing

Before adding or downloading any dataset as part of the project, record:

- source;
- license/terms;
- allowed redistribution;
- version/date;
- checksum or immutable identifier where practical.

A benchmark we cannot legally or reproducibly describe is a bad benchmark for a public research repo.
