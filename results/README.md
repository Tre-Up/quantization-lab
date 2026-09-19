# Results

This directory contains compact machine-readable summaries suitable for version control.

Headline tables in the README or technical report must be traceable to records here or to immutable external artifacts.

Prefer formats such as JSON, JSONL, CSV, or small Parquet files when practical.

Do not commit:

- model weights;
- large benchmark dumps;
- huge profiler traces;
- opaque binary artifacts without provenance.

For large artifacts, record immutable locations, hashes, tool versions, and the config/commit that produced them.
