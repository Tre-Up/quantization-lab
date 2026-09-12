# Success Criteria

The project has two separate success levels: **v0.1 success** and **research breakthrough**. They must not be confused.

## v0.1 success

v0.1 is successful if all of these are true:

- at least 3 open-weight model families are evaluated;
- an established baseline is reproduced correctly;
- approximately 4× weight-storage compression is demonstrated on representative models where technically appropriate;
- aggregate measured quality retention is at least 99% on the locked held-out battery for the headline configuration;
- peak runtime memory is measured under a fixed workload;
- latency and throughput are reported;
- no core evaluation domain is silently omitted because it performs badly;
- the final result can be reproduced from committed code and configs;
- at least one external person can run the project without private setup instructions.

## Stretch / breakthrough success

A result becomes genuinely unusual if it demonstrates something close to:

- ≥5× compression;
- ≥99.9% measured quality retention;
- consistent results across multiple model families;
- materially lower real peak runtime memory;
- usable speed on constrained local hardware;
- independent reproduction.

A single lucky model does not establish the general claim.

## Automatic failure conditions for a headline claim

Do **not** publish a headline compression/quality claim if any of the following is true:

- the final test set was used to tune the quantizer;
- baseline and quantized runs use different prompts, decoding, context, or scoring rules;
- the reported compression number is only a compressed download size;
- runtime memory is missing for a deployment-oriented claim;
- only aggregate quality is reported while a major domain collapses;
- failed seeds/runs were discarded without explanation;
- the result depends on an uncommitted local patch;
- the exact model revision cannot be identified;
- the test suite is too small or too narrow to support the wording of the claim.

## Language standard

Preferred wording:

> “The quantized model retained 99.2% of the baseline score on the locked held-out evaluation battery.”

Avoid:

> “The model keeps 99.2% of its intelligence.”

The first sentence is measured. The second is marketing pretending to be measurement.
