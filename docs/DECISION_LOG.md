# Decision Log

Major project decisions are recorded here so later changes have context.

## 2026-09-12 — D001: Optimize for measured preservation, not a marketing number

**Decision:** Report measured quality retention against the original model rather than claims such as “99.9% intelligence.”

**Reason:** Intelligence is not a single directly measurable scalar. Frozen evaluation, per-domain scores, and uncertainty are defensible.

## 2026-09-12 — D002: Runtime memory is a first-class metric

**Decision:** Disk/model size and runtime memory are reported separately.

**Reason:** A compact file that requires excessive working memory fails the deployment goal.

## 2026-09-12 — D003: Initial dense-quantization target

**Decision:** The original foundation set ~4× weight-storage compression as the primary target and 5× + 99.9% measured retention as stretch.

**Status:** **Superseded by D007.**

**Reason for preservation:** This records the repository's original research direction rather than rewriting history.

## 2026-09-12 — D004: Apple Silicon is the first deployment target

**Decision:** Use an M4 / 16 GB unified-memory machine as the primary constrained-device target.

**Reason:** Hard local constraints force deployment measurements to include real memory and runtime behavior.

## 2026-09-12 — D005: Reproduce before inventing

**Decision:** Established quantization/runtime approaches must be reproduced before custom algorithm claims.

**Reason:** Without trustworthy baselines, novelty and improvement claims are meaningless.

## 2026-09-12 — D006: Licensing remains intentionally unresolved during foundation work

**Decision:** Do not select a final software license yet.

**Reason:** Public validation, individual/research access, commercial options, and possible IP protection need a deliberate decision before the first serious release.

## 2026-09-19 — D007: Expand the research question to joint MoE precision + residency optimization

**Decision:** v0.1 will investigate device-aware MoE inference rather than dense quantization alone. The system will test whether quantization precision and expert residency/offload can be selected jointly using sensitivity, routing behavior, and device constraints.

**Reason:** Weight compression alone does not capture the dominant deployment costs on constrained devices. MoE introduces expert-level heterogeneity in active compute, routing frequency, memory residency, and transfer cost that can be measured and optimized together.

**Consequence:** The primary v0.1 target becomes ≥3× expert-weight storage compression with ≥99% locked measured quality retention plus runtime-memory evidence. Approximately 4× + ≥99.9% becomes a stretch target. These are targets, not promised results.

## 2026-09-19 — D008: Public repository is a research artifact, not a personal learning diary

**Decision:** Public structure uses milestones, experiments, configs, results, and provenance. Personal study plans and assessments are not part of the repository's primary surface.

**Reason:** The repository should stand on its technical usefulness to external ML systems engineers, researchers, and contributors.
