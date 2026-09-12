# Provenance & Evidence

The repository should make the project timeline and technical progression independently inspectable.

## Why this exists

A final December release is less informative than a chronological record showing how the work evolved from baseline reproduction to original experiments.

## Evidence sources

Use Git-native evidence wherever practical:

- dated commits;
- issues and pull requests;
- weekly research logs;
- experiment IDs;
- immutable model revisions;
- machine-readable benchmark results;
- release tags;
- external reproduction issues/PRs.

## Research-origin baseline

Project research window begins **2026-09-12**.

At foundation time:

- no original quantization algorithm is claimed;
- no 4×/5× quality result is claimed;
- the repository starts with methodology, learning, and baseline infrastructure;
- custom-method claims must emerge from later committed experiments.

This baseline matters. Do not backfill future understanding into old research logs.

## Weekly evidence standard

Each week should leave at least one durable artifact such as:

- code;
- experiment results;
- a benchmark change;
- a research note tied to evidence;
- a documented failed hypothesis;
- a reproducibility improvement.

## External validation

When an external user reproduces a result, record:

- public issue/PR/discussion reference;
- hardware;
- model revision;
- result/config;
- whether the reproduction matched expected tolerance.

Do not fabricate or privately self-report external validation.

## Release evidence

For v0.1, preserve:

- release tag;
- release commit;
- frozen evaluation protocol;
- headline result artifacts;
- exact documentation used by external reproducers.

The goal is simple: a skeptical technical reviewer should be able to trace a headline claim backward to its raw evidence.
