# Research Records

This directory contains the evidence trail behind technical decisions.

The repository uses **experiment IDs and research questions**, not week-by-week progress diaries.

For the milestone-level public history, see [PROVENANCE.md](PROVENANCE.md). It records only meaningful technical transitions and links them to immutable repository evidence.

## Experiment record

Every serious experiment should answer one narrow question and preserve enough information to repeat it.

Recommended ID:

```text
YYYYMMDD-model-method-purpose-NNN
```

Example:

```text
20261031-moe-routing-frequency-profile-001
```

Use [experiment-template.md](experiment-template.md).

## What belongs here

- hypotheses;
- experiment records;
- negative results;
- ablations;
- architecture-specific observations;
- unresolved questions that affect interpretation;
- milestone-level provenance backed by commits or immutable artifacts.

Large raw artifacts should live in an appropriate artifact store. Commit immutable references/checksums plus compact machine-readable summaries.

## What does not belong here

- personal learning diaries;
- application material;
- motivational logs;
- private assessment or ownership evidence;
- retrospective claims not backed by experiments.

The Git history and experiment sequence should make the technical evolution of the project visible without turning the repository into a personal progress journal.
