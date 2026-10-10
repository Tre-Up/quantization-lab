# Current Status

Last reviewed: **2026-10-10**

## Historical foundation and execution restart

The repository was established on 2026-09-12; the MoE focus was documented on 2026-09-19. Earlier milestone dates were plans, not evidence of completed experiments.

**2026-10-10 is Day 1 of a new execution cycle.** Prior inactivity is not represented as completed work. See [ROADMAP.md](../ROADMAP.md) for new, provisional windows.

## Current technical state

**Foundation / baseline instrumentation.** The project has a public research charter, evaluation and hardware standards, experiment protocols, a minimal `qlab doctor` CLI, and repository scaffolding.

A draft PR, [#7](https://github.com/Tre-Up/quantization-lab/pull/7), adds a small baseline record validator and synthetic contract tests. It is **not merged** as of this status entry; those tests do not constitute quantization or hardware results.

## Not yet demonstrated

- No measured first local baseline on Apple Silicon / 16 GB has been published.
- No original adaptive quantization or expert-residency method is implemented.
- No expert routing/sensitivity profiler or finished benchmark suite exists.
- No verified 3×/4× compression, 99%/99.9% measured retention, cross-family validation, or independent reproduction result exists.

## Next acceptance gate: M0

- Select a feasible supported model/runtime path and pin exact revisions/licenses.
- Freeze workload, decoding, device and software metadata.
- Run real reference measurements on the actual target hardware: weight storage, resident and peak memory, TTFT and throughput.
- Attempt at least one established quantized comparison under comparable conditions.
- Commit or immutably reference raw results and reproducible instructions.

We make no efficiency or quality claims until the evidence supports them.
