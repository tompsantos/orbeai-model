# Batch 001 Review

## Scope

Review of `datasets/candidates/batch-001.jsonl` containing records `orbe-sft-000004` through `orbe-sft-000013`.

## Review status

- Model pre-review: complete
- Human review: pending
- Promotion to `synthetic_reviewed`: blocked until human approval

## Results

| ID | Category | Verdict | Notes |
|---|---|---|---|
| 000004 | ptbr_communication | pass after minor edit | Replaced gendered closing with neutral wording. |
| 000005 | ptbr_communication | pass after minor edit | Clarified training vs RAG without overstating knowledge changes. |
| 000006 | instruction_following | pass | Exactly three bullets; each respects word limit. |
| 000007 | instruction_following | pass | Output contains only the requested two-column table. |
| 000008 | practical_reasoning | pass | Prioritizes measurement and context reduction before model replacement. |
| 000009 | practical_reasoning | pass | Correctly separates dynamic knowledge from stable behavior. |
| 000010 | technical_ai_coding | pass | Python solution is compact, valid and handles empty lines. |
| 000011 | document_analysis | pass | Distinguishes reported forecast, risk and next action. |
| 000012 | structured_output | pass | Returns valid JSON only and follows requested fields. |
| 000013 | uncertainty_truthfulness | pass | Refuses to fabricate unavailable financial data and proposes a grounded next step. |

## Quality checks

- No near-duplicate prompts detected within the batch.
- No fake citations or unsupported factual claims detected.
- No hidden chain-of-thought content.
- PT-BR is natural and task-appropriate.
- Constraints are followed in all constrained examples.

## Promotion rule

After human approval, change `source` from `synthetic_draft` to `synthetic_reviewed`, replace `reviewed_by` with the human reviewer identifier, and copy the approved records into the gold dataset.