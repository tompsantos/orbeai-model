# OrbeAI SFT Dataset v0.1

## Goal

Create a small, high-quality supervised fine-tuning dataset that teaches the OrbeAI Model how to behave, communicate and solve practical tasks in Brazilian Portuguese without trying to replace the foundation model's general knowledge.

The v0.1 dataset is optimized for **quality, coverage and traceability**, not raw volume.

## Canonical format

The training source of truth is JSONL using a chat-style `messages` field plus metadata.

Each line represents one training example.

```json
{
  "id": "orbe-sft-000001",
  "version": "0.1",
  "category": "instruction_following",
  "language": "pt-BR",
  "difficulty": "medium",
  "source": "human_curated",
  "tags": ["constraints", "formatting"],
  "messages": [
    {"role": "system", "content": "Você é a OrbeAI."},
    {"role": "user", "content": "Explique RAG em três tópicos curtos."},
    {"role": "assistant", "content": "1. ..."}
  ]
}
```

## Dataset categories and initial target mix

| Category | Target | Purpose |
|---|---:|---|
| `ptbr_communication` | 20% | Natural Brazilian Portuguese, tone control, clarity and concise dialogue |
| `instruction_following` | 15% | Respect explicit constraints, requested formats and task boundaries |
| `practical_reasoning` | 15% | Break down real technical/business problems into useful decisions and next steps |
| `technical_ai_coding` | 15% | AI engineering, software, APIs, debugging and coding-oriented answers |
| `document_analysis` | 10% | Summaries, extraction, comparison and structured analysis of supplied content |
| `structured_output` | 10% | Valid JSON, schemas, tables and machine-consumable outputs when requested |
| `tool_use` | 5% | Decide when a tool is needed, prepare arguments and handle tool results coherently |
| `uncertainty_truthfulness` | 5% | State uncertainty, avoid fabrication and distinguish evidence from inference |
| `orbe_behavior` | 5% | Stable Orbe identity, execution style and interaction principles |

The mix is a starting hypothesis and can change after evals.

## Required fields

- `id`: globally unique stable identifier
- `version`: dataset version
- `category`: one primary taxonomy category
- `language`: normally `pt-BR` for v0.1
- `difficulty`: `easy`, `medium` or `hard`
- `source`: provenance label
- `messages`: ordered chat messages ending in an assistant response

## Optional fields

- `tags`: secondary labels
- `notes`: curator notes not intended for model training
- `quality_score`: curator score from 1 to 5
- `reviewed_by`: reviewer identifier
- `license`: source/license note when applicable
- `synthetic_generator`: model/tool used when an example is synthetic

## Source values

Recommended values:

- `human_curated`
- `human_written`
- `synthetic_reviewed`
- `public_licensed`
- `transformed_internal`

Synthetic content is allowed only after human review for the v0.1 gold set.

## Quality rules

An example is accepted only when it:

1. has one clear training objective;
2. is factually defensible or self-contained;
3. contains natural PT-BR rather than literal translated English;
4. demonstrates the exact behavior we want to reinforce;
5. avoids unnecessary verbosity and generic filler;
6. follows requested output constraints exactly;
7. does not include private, secret or personal data without explicit rights;
8. has traceable provenance;
9. is not a near-duplicate of another example;
10. would be considered a good answer even if no training were involved.

## Negative patterns to reject

Reject examples that contain:

- invented facts presented as certain;
- broken JSON when valid JSON was requested;
- excessive canned disclaimers;
- fake citations;
- unexplained English jargon when PT-BR wording is available;
- hidden chain-of-thought or requests to reproduce private reasoning;
- outputs copied from sources without compatible rights;
- personality quirks that reduce usefulness outside a narrow conversation;
- duplicated prompts with superficial wording changes.

## System-message strategy

The dataset should not rely on a huge system prompt to manufacture the behavior. The system message should be minimal and stable, while desired behaviors are demonstrated in the assistant responses.

Initial default:

```text
Você é a OrbeAI, uma assistente de inteligência artificial focada em clareza, execução, raciocínio prático e português brasileiro natural.
```

This wording is provisional and will be tested against the baseline.

## Versioning

- `0.1-dev`: actively changing working set
- `0.1-rc1`: frozen candidate used for validation
- `0.1`: first training-ready release

Every training run must reference an immutable dataset commit or Hub revision.

## Initial volume target

For the first real experiment, target **300 to 500 gold examples** rather than thousands of weak examples.

Suggested checkpoints:

- 50 examples: schema and style validation
- 100 examples: category coverage review
- 300 examples: first serious SFT candidate
- 500 examples: v0.1 target if quality remains consistent

## Train/eval separation

Evaluation prompts must not be copied into the training dataset. The eval suite is maintained separately so we can measure whether the model generalized rather than memorized.

## Definition of done for dataset v0.1

The dataset is training-ready only when:

- all records validate against the JSON schema;
- every category reaches its agreed minimum coverage;
- every record has provenance;
- duplicates and obvious contamination are removed;
- a manual review sample passes quality inspection;
- train and eval sets are demonstrably separated;
- the dataset is pinned to a version/commit.
