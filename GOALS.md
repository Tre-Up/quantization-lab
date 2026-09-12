# Goals

## v0.1 primary goals

By 2026-12-12, the project should aim to demonstrate all of the following:

1. **Multiple model families**
   - Validate on at least 3 open-weight transformer families.

2. **Meaningful compression**
   - Target approximately **4× weight-storage compression** relative to FP16/BF16.
   - Report real peak runtime memory separately.

3. **High measured quality retention**
   - Target **≥99% aggregate measured quality retention** on the locked held-out evaluation protocol.
   - No single core domain may be hidden by a strong aggregate score.

4. **Real local deployment evidence**
   - Measure at least one representative model on the primary Apple Silicon development device.
   - Report memory, latency, and throughput under fixed settings.

5. **Reproducibility**
   - Every headline result must map to committed code, config, model identifier, hardware metadata, and raw result artifacts.

6. **Usability**
   - A technically competent external user should be able to reproduce at least one result without private instructions.

## Stretch goals

These are intentionally difficult and are not promised:

- **≥5× compression** with **≥99.9% measured quality retention** on the locked protocol;
- a 27B-class open model that becomes practically usable within a constrained local-memory envelope;
- an automatic model-sensitive bit-allocation policy that outperforms a fixed-bit baseline;
- independent external reproduction of a headline result;
- meaningful open-source adoption: real users, issues, forks, and contributions rather than vanity metrics.

## Non-goals

The project does not optimize for:

- raw GitHub star count at the expense of technical quality;
- benchmark gaming;
- a single hand-picked model that cannot generalize;
- vague “same intelligence” claims without a frozen evaluation definition;
- compression ratios calculated only from a ZIP file or download size;
- using closed APIs as if their internal weights had been quantized.

## Long-term ambition

The long-term ambition is to reduce the compute and memory cost of running capable models, first for local users and eventually for larger inference systems, while preserving measurable capability as tightly as possible.

That ambition is not evidence. The repository will earn it one experiment at a time.
