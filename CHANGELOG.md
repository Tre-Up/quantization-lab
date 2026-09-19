# Changelog

All notable project changes are documented here.

## Unreleased

### Changed
- Refocused the research question from dense quantization alone to **device-aware MoE quantization + expert residency/offload**.
- Replaced the week-based public roadmap with evidence-driven research milestones.
- Expanded architecture to include routing profiling, expert sensitivity, cost modeling, residency/offload, and joint policy search.
- Updated success criteria to separate primary evidence from stretch outcomes.
- Extended hardware standards to report resident memory, expert transfers, cache behavior, and sustained repeated-run performance.
- Extended failure modes for workload-specific routing, cache thrashing, prefetch errors, storage bottlenecks, and proxy failure.
- Reframed public learning-oriented documentation as technical prerequisites/provenance rather than personal progress tracking.

### Added
- `experiments/` for reproducible experiment records.
- `configs/` for frozen machine-readable configurations.
- `results/` for compact versioned result summaries.
- Explicit prior-art discipline before novelty claims.

### Existing foundation
- Evaluation, runtime-memory, experiment, reproducibility, provenance, and security standards.
- Minimal Python package skeleton with `qlab doctor`.

## 0.0.0 — 2026-09-12

- Repository created.
- Initial quantization research foundation established.
