# Map AI Usage to Deliverables

Teaching deck from a May 13, 2026 lightning lesson about connecting AI-tool
telemetry to shipped engineering work.

## Evidence status

This repository is a **historical workshop artifact**, not a research result or
deployment case study.

The 28-person team, 89% vendor-adoption rate, 29% AI-traced delivery rate,
$3,600 recoverable spend, 16.9x ROI, and 12-week trajectory in the slides are
**synthetic fixtures**. They demonstrate calculations and dashboard structure.
They do not measure a real organization, establish an industry prevalence rate,
or validate the proposed thresholds.

The deck refers to an engine, tests, source files, and dashboards that are not
published in this repository. Its implementation claims are not independently
reproducible here. See the version-bound
[claim boundary and correction record](CLAIM_BOUNDARY.md) before citing it.

## Slides

[Download the 24-slide PDF](Map_AI_Usage_to_Deliverables_VyomaGajjar.pdf)

## What remains useful

- A concrete join between tool-use events and delivery events.
- A reminder that login and prompt counts are not outcome measures.
- An illustrative way to expose cost-model assumptions instead of hiding them.
- A list of provenance, attribution, and threshold questions a real deployment
  would have to validate.

The deck's strongest language should be read as workshop framing. In particular,
an AI marker in a commit is neither proof that AI caused the artifact nor proof
that the artifact was valuable. A production system would need independently
validated provenance, outcome definitions, uncertainty analysis, and a
pre-registered evaluation of any intervention.

## Verification

The correction record is bound to the exact PDF currently published here:

```bash
python3 scripts/validate_claims.py
```

The check fails if the PDF changes without a corresponding review of its claim
boundary.

## Author

[Vyoma Gajjar](https://vyomagajjar.com/) works across predictive machine
learning, generative AI, agent systems, evaluation, and production feedback
loops.

## License

Copyright 2026 Vyoma Gajjar. Free to download and share with attribution.
Commercial use or redistribution in paid programs requires permission.
