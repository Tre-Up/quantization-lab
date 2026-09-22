# Technical Provenance

This file records the technical evolution of `quantization-lab` without turning the repository into a personal learning diary.

The public record is milestone-based. Entries are added only when a technical artifact, experiment, measurement capability, or research boundary materially changes. Personal assessments, study notes, application material, and private ownership evidence remain outside the public repository.

## Provenance rules

- Record facts that are verifiable from the repository or a linked immutable artifact.
- Reference the commit that introduced the technical change when possible.
- Do not rewrite historical entries to imply results that did not exist at the time.
- Do not use `Day N`, `Week N`, motivational, admissions, or personal-progress language.
- Negative results and failed approaches remain part of the technical record when they affect interpretation.
- Claims about compression, quality retention, runtime, or memory require measured evidence under the repository standards.

## Milestones

| Date | Technical state | Evidence |
| --- | --- | --- |
| 2026-09-12 | Research repository foundation established. The project had a charter, standards, experiment template, and minimal `qlab doctor` CLI, but no implemented quantization method, benchmark implementation, or validated compression/quality-retention result. | `4d513480a4bc82baee1cade052668ce9d4339b0e`, `research/foundation-record.md` |
| 2026-09-19 | Public research surface refocused on device-aware MoE inference: joint quantization precision and expert residency/offload, reproducible experiment/config/result structure, MoE-specific measurement standards, and prior-art discipline. | `82e2233d078310dc6d917a9184a4a313d7d04e90` |

## Next entry rule

The next provenance entry should be added only after a concrete technical artifact lands, for example:

- a tested theoretical weight-memory utility integrated into the package;
- a versioned device/environment metadata schema;
- a reproducible baseline on an exact model revision;
- an automated experiment or evaluation harness;
- a routing/sensitivity profiler;
- a residency/offload baseline;
- a joint precision-residency policy with measured results.

The Git history, experiment records, frozen configs, and result artifacts are the primary evidence. This file is only an index of meaningful transitions.
