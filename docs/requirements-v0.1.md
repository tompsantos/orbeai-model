# OrbeAI Model v0.1 — Requirements

## Goal

Build the first useful, measurable and portable OrbeAI model derivative. v0.1 is not intended to replace frontier closed models. It is intended to prove that OrbeOne can post-train, evaluate and deploy its own open-weight model lineage with clear gains for the OrbeAI use case.

## Product profile

OrbeAI Model v0.1 should behave as a PT-BR-first general-purpose assistant with strong practical reasoning, technical fluency and reliable structured output. It should be useful as a base for future Orbe verticals without baking each vertical deeply into the first release.

## Priority capabilities

### P0 — Brazilian Portuguese

The model must:
- understand informal and formal Brazilian Portuguese naturally;
- avoid literal translation artifacts and unnatural European Portuguese phrasing;
- preserve tone, intent and technical vocabulary;
- write concise, structured answers when the task benefits from structure;
- handle mixed PT-BR + English technical terminology cleanly.

Success signal: human evaluation and OrbeAI eval set show no material degradation against the chosen base model and measurable improvement in Orbe-style PT-BR interactions.

### P0 — Instruction following

The model must:
- obey explicit format, scope and ordering constraints;
- distinguish requests to explain, plan, compare, draft and execute;
- avoid adding unnecessary steps when the user asked for a direct answer;
- preserve requested output schemas.

Success signal: high pass rate on deterministic format and constraint-following evals.

### P0 — Practical reasoning

The model should perform well on:
- breaking ambiguous real-world problems into actionable steps;
- comparing options using explicit criteria;
- identifying assumptions, risks and missing information;
- producing plans with dependencies and next actions;
- explaining technical concepts without unnecessary jargon.

Success signal: preferred over the base model on a majority of blinded Orbe practical-reasoning evals without increasing hallucination rate.

### P0 — Structured output

The model must reliably produce:
- JSON when explicitly requested;
- tables and checklists when appropriate;
- concise summaries;
- step-by-step implementation plans;
- machine-consumable fields for downstream automation.

Success signal: schema-valid output on the dedicated structured-output eval set.

### P1 — Technical and coding fluency

The model should be competent at:
- Python and API-oriented examples;
- architecture and integration reasoning;
- reading small code snippets and identifying obvious bugs;
- producing implementation-oriented pseudocode;
- explaining infrastructure and AI engineering concepts in PT-BR.

v0.1 does not need to compete with dedicated frontier coding models.

### P1 — Tool and agent readiness

When the selected foundation supports tool calling, the derivative should preserve or improve:
- tool-selection discipline;
- argument formatting;
- separation between reasoning, tool call and final answer;
- ability to use tool results rather than inventing them.

This capability must not be introduced if the base model lacks a stable tool-calling path.

### P1 — Uncertainty and factual discipline

The model should:
- distinguish known facts from assumptions;
- say when information is uncertain or unavailable;
- avoid fabricating citations, tool results or external state;
- avoid pretending an action was executed when it was not.

Success signal: no regression against the base model on hallucination and unsupported-claim evals.

## Behavioral profile

The model should be:
- direct rather than ceremonious;
- warm without becoming verbose by default;
- adaptive to user expertise;
- comfortable with informal PT-BR while remaining capable of professional output;
- explicit about tradeoffs and uncertainty;
- oriented toward useful next actions.

The behavior must be learned primarily through training examples and evaluation, not hidden behind an oversized system prompt.

## Portability requirements

The selected base and resulting derivative should support a path to:
- Hugging Face Transformers;
- PEFT / LoRA or QLoRA training;
- export or merge into a standalone model when technically supported;
- self-hosted inference through at least one production-oriented runtime such as vLLM;
- local or low-cost inference through GGUF / llama.cpp / Ollama when architecture support exists.

No single hosting provider may be a hard dependency of the model lineage.

## Cost and size constraints

For the first training cycle:
- prefer a model small enough to fine-tune with LoRA/QLoRA on a single affordable cloud GPU;
- target the 3B–9B class unless evidence strongly favors another size;
- larger models may be evaluated as future candidates but should not be the default v0.1 training target;
- all training runs must have an estimated cost before execution.

## Evaluation requirements

No fine-tune is considered successful based only on training loss.

Every candidate must be compared against its untouched base model using the same eval set.

The v0.1 evaluation suite must cover at minimum:
1. PT-BR naturalness;
2. instruction following;
3. practical reasoning;
4. structured output;
5. technical/coding tasks;
6. uncertainty and hallucination discipline;
7. tool calling if supported;
8. regression checks for general capability.

## Data requirements

Training data must be:
- versioned;
- traceable to source or generation method;
- reviewed before use;
- separated into train and evaluation data;
- free of secrets and private credentials;
- compatible with the selected base model license and intended use.

Synthetic data is allowed, but synthetic examples must be filtered and reviewed rather than accepted blindly.

## Out of scope for v0.1

- pretraining a foundation model from scratch;
- embedding all OrbeGov, OrbeCorp, OrbeZen, OrbeScience and OrbeX knowledge directly into weights;
- replacing RAG with memorized knowledge;
- training on confidential customer data;
- optimizing exclusively for public benchmarks;
- claiming the derivative is a new foundation model;
- production deployment before baseline and regression testing.

## Minimum release gate

OrbeAI Model v0.1 may be tagged as a successful first release only if:
- the training pipeline is reproducible;
- model, dataset version and config are recorded;
- it beats or matches the base model on the majority of Orbe-specific priority evals;
- it does not show a material regression in factual discipline or instruction following;
- it can be loaded outside the training environment;
- its license and attribution requirements are documented;
- the result, including failed or neutral findings, is documented honestly.

## Decision consequence

The foundation-model selection should optimize for these requirements, not for headline benchmark position alone. The next decision is to score candidate base models against this specification and select a primary model plus one fallback.