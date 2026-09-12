# Contributing

Thank you for helping improve quantization-lab.

This project values **reproducible evidence over confident claims**.

## Before opening a pull request

Please include:

- what problem you are solving;
- model + exact revision used;
- hardware/runtime information where relevant;
- a reproducible command/config;
- before/after measurements for behavior-changing work;
- tests for code paths that can be tested cheaply;
- limitations or cases you did not validate.

## Research contributions

For a new quantization idea or benchmark result, prefer an experiment record containing:

- hypothesis;
- baseline;
- candidate settings;
- raw metrics;
- interpretation;
- possible confounders;
- reproduction instructions.

## Claims

Do not describe a result as:

- “lossless,”
- “same intelligence,”
- “5× cheaper,”
- “works for every model,”

unless the repository contains evidence whose scope actually supports that wording.

Narrow honest claims are more useful than impressive fiction.

## Code style

For the initial Python codebase:

- Python 3.11+;
- type hints for public interfaces;
- small functions with explicit inputs/outputs;
- machine-readable configs/results;
- deterministic behavior where feasible;
- tests around metric calculations and experiment metadata.

Formatting/linting tooling will be locked once the first implementation work begins.

## Large files

Do not commit model weights, benchmark dumps, or large binary artifacts directly to Git.

Use an appropriate model/artifact host and commit immutable identifiers/checksums instead.

## Security

Please follow [`SECURITY.md`](SECURITY.md) for security-sensitive reports instead of opening a public exploit issue.
