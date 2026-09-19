# Success Criteria

The project distinguishes **v0.1 success**, **stretch success**, and **unsupported claims**.

## v0.1 success

v0.1 is successful only if all of the following are true:

- established quantization and MoE baselines are reproduced under fixed conditions;
- at least three open-weight model families or architecture variants are attempted;
- the headline candidate demonstrates **≥3× expert-weight storage compression** relative to FP16/BF16 where technically appropriate;
- aggregate measured quality retention is **≥99%** on the locked held-out protocol;
- no major evaluation domain is silently omitted because it performs badly;
- resident and peak runtime memory are measured under a fixed workload;
- TTFT and generation throughput are reported;
- expert transfer/cache behavior is reported when offloading materially affects the result;
- the adaptive policy is compared with simpler baselines;
- the final candidate is frozen before held-out evaluation;
- every headline result maps to committed code, config, model revision, hardware metadata, and raw/immutable result artifacts;
- at least one documented result can be reproduced without private setup instructions.

## Stretch success

A result becomes notably stronger if it demonstrates some combination of:

- approximately **4× or better expert-weight compression**;
- **≥99.9% measured quality retention** on the locked protocol;
- materially lower peak/resident memory than a fair uniform-quantized MoE baseline;
- measurable energy or sustained-thermal improvement;
- expert prefetch/cache gains without unacceptable latency or memory growth;
- consistent behavior across multiple model families;
- independent external reproduction.

Stretch outcomes are not required for v0.1 and are not promised.

## Automatic failure conditions for a headline claim

Do not publish a headline compression, quality, memory, or efficiency claim if any of the following is true:

- final held-out data influenced bit width, group size, residency, cache, prefetch, or candidate selection;
- baseline and candidate runs use non-equivalent prompts, context, decoding, or scoring rules without explicit justification;
- compression is calculated only from a ZIP/download size;
- parameter count is presented as reduced when only representation size changed;
- runtime-memory evidence is missing for a deployment claim;
- offload/transfer overhead is hidden;
- a strong aggregate score hides a major domain collapse;
- failed runs or seeds were discarded without explanation;
- the result depends on an uncommitted patch or unidentified model revision;
- the test set is too small or narrow for the wording of the claim;
- novelty is claimed without prior-art review.

## Language standard

Preferred:

> “The candidate retained 99.4% of the baseline score on the locked held-out protocol while reducing expert-weight storage by 3.2× on the tested model.”

Avoid:

> “The model keeps 99.4% of its intelligence.”

The first statement is scoped evidence. The second is marketing language pretending to be measurement.
