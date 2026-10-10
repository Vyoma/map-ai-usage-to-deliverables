"""Bind the public correction record to the workshop artifact it qualifies."""

from __future__ import annotations

from hashlib import sha256
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PDF = ROOT / "Map_AI_Usage_to_Deliverables_VyomaGajjar.pdf"
README = (ROOT / "README.md").read_text(encoding="utf-8")
BOUNDARY = (ROOT / "CLAIM_BOUNDARY.md").read_text(encoding="utf-8")
NORMALIZED_README = " ".join(README.split())
NORMALIZED_BOUNDARY = " ".join(BOUNDARY.split())
EXPECTED_PDF_SHA256 = "41bdc9ee2e44d208274f4eab709078fe0e9f4c939c329996f8da179980415d71"

failures: list[str] = []

if not PDF.is_file():
    failures.append("workshop PDF is missing")
else:
    observed = sha256(PDF.read_bytes()).hexdigest()
    if observed != EXPECTED_PDF_SHA256:
        failures.append(
            "workshop PDF changed without a reviewed claim boundary: "
            f"expected {EXPECTED_PDF_SHA256}, observed {observed}"
        )

for phrase in (
    "historical workshop artifact",
    "synthetic fixtures",
    "not independently reproducible here",
    "CLAIM_BOUNDARY.md",
):
    if phrase not in NORMALIZED_README:
        failures.append(f"README is missing required boundary: {phrase}")

for phrase in (
    EXPECTED_PDF_SHA256,
    "Unsupported generalization",
    "Retracted as a universal claim",
    "Incorrect for the public repository",
    "Synthetic trajectory",
    "Unsupported prevalence claims",
    "unvalidated system proposal",
):
    if phrase not in NORMALIZED_BOUNDARY:
        failures.append(f"correction record is missing required boundary: {phrase}")

for stale_phrase in (
    "DM me",
    "numbers that survive scrutiny",
    "what actually shipped",
):
    if stale_phrase.casefold() in README.casefold():
        failures.append(f"README retains an unsupported promotional claim: {stale_phrase}")

if failures:
    raise SystemExit("\n".join(f"FAIL {failure}" for failure in failures))

print(f"Claim boundary validated for PDF sha256={EXPECTED_PDF_SHA256}")
