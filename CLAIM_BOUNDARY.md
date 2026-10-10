# Claim boundary and correction record

This record applies to `Map_AI_Usage_to_Deliverables_VyomaGajjar.pdf` with
SHA-256:

`41bdc9ee2e44d208274f4eab709078fe0e9f4c939c329996f8da179980415d71`

It separates what the deck demonstrates from what its evidence does not support.
The PDF is preserved unchanged so the correction stays auditable.

## Supported scope

The deck demonstrates an illustrative data model, deterministic calculations,
and a possible reporting workflow over a synthetic 28-person team. It can be
used as teaching material or as a design prompt.

The repository does not contain the engine, input data, tests, dashboard, or
intervention record described in the deck. It therefore does not independently
verify the implementation or any numerical result.

## Corrections and limitations

| Slides | Statement or implication | Evidence status |
|---|---|---|
| 2, 16, 17, 19 | The 89%, 29%, $3,600, $283,200, and 16.9x figures describe a team and its economics. | Synthetic fixture. The $200 value per traced artifact and $50 monthly seat price are assumptions, not measurements. These values cannot support an ROI or savings claim about a real deployment. |
| 3 | Every AI vendor reports the same adoption signals, and those signals do not predict anything. | Unsupported generalization. No vendor sample, dashboard versions, correlation analysis, or outcome data is published here. |
| 4, 10, 22 | Lineage is the only adoption metric that cannot be gamed without doing real work. | Retracted as a universal claim. A marker can be added without meaningful AI contribution or omitted when AI was used. The proposed regexes measure declared markers, not causal contribution, artifact quality, or business value. |
| 7 | Every architecture box is a real file in this repository, including roughly 1,800 lines of Python and dashboards. | Incorrect for the public repository. Only the deck and its documentation are published. |
| 8, 17 | A roughly 760-line engine and ten passing assertions verify the scenario. | Not independently reproducible here because the referenced code, data, and tests are absent. The slide output is a presentation artifact, not executable evidence. |
| 14 | AI attribution percentages can be attached to OKR value. | Illustrative only. Association between a tagged artifact and an OKR does not establish the fraction of OKR value caused by AI. |
| 20 | A week-6 intervention increased organization-wide and OKR attribution, value, and ROI over twelve weeks. | Synthetic trajectory. It is not an observed intervention, and no causal effect can be inferred. |
| 22 | 21% of typical seats have no traceable output, theater performers prompt four times more, a 60-point gap is typical, and every enterprise has paid for a bot. | Unsupported prevalence claims derived from the synthetic fixture. They must not be quoted as measured facts. |

## What would be required to upgrade the claims

1. Publish the exact code, synthetic generator, input schema, fixtures, and tests.
2. Pin vendor exports and delivery records to documented versions and collection
   windows, with privacy-preserving stable joins.
3. Validate marker precision and recall against independently reviewed examples.
4. Define an outcome before inspecting the data and distinguish attribution from
   causal contribution.
5. Pre-register thresholds and the intervention analysis, including comparison
   groups, missingness, uncertainty, and stopping rules.
6. Report failure cases, sensitivity to the $200 value assumption, and the cost
   of maintaining provenance instrumentation.

Until those conditions are met, this is a useful teaching artifact and an
unvalidated system proposal, not evidence that the method works in production.
