# Decision Log

Major project decisions belong here so future changes have context.

## 2026-09-12 — D001: Optimize for measured preservation, not a marketing number

**Decision:** The project will report measured quality retention against the original model, not claim “99.9% intelligence.”

**Reason:** Intelligence is not a single directly measurable scalar. A frozen evaluation battery, domain scores, and uncertainty are defensible.

## 2026-09-12 — D002: Runtime memory is a first-class metric

**Decision:** Disk/model size and peak runtime memory will always be reported separately.

**Reason:** A compact file that still requires excessive working memory fails the local-deployment goal.

## 2026-09-12 — D003: 4× is the v0.1 primary target; 5× + 99.9% is stretch

**Decision:** The project will not define success as an unproven breakthrough.

**Reason:** Starting from beginner level, v0.1 needs a demanding but credible engineering/research target while still attacking a much harder stretch result.

## 2026-09-12 — D004: Apple Silicon is the first deployment target

**Decision:** Use an M4 / 16 GB unified-memory machine as the primary constrained-device target.

**Reason:** Local inference is the project's immediate use case, and hard memory constraints force honest deployment measurements.

## 2026-09-12 — D005: Reproduce before inventing

**Decision:** Existing quantization methods must be reproduced and measured before custom algorithm claims begin.

**Reason:** Without a trustworthy baseline, novelty and improvement claims are meaningless.

## 2026-09-12 — D006: Licensing remains intentionally unresolved during foundation work

**Decision:** Do not add a final software license yet.

**Reason:** The project wants public validation and broad individual access while preserving commercial/IP options. The open-source vs source-available tradeoff must be decided deliberately before the first serious release.
