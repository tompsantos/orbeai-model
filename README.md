# OrbeAI Model

Development of the OrbeAI model: open-weight foundation models, PT-BR datasets, post-training, evaluations, and portable deployment.

## Status

**Phase m0 — Foundation**

This repository is the engineering workspace for building the OrbeAI Model. The project starts from open-weight foundation models and focuses on reproducible post-training, Portuguese (Brazil) quality, evaluation, and infrastructure portability.

## Initial goals

- define the requirements for OrbeAI Model v0.1
- select the initial foundation model using explicit technical criteria
- design and version the OrbeAI training dataset
- build a repeatable evaluation suite before training
- run SFT / LoRA / QLoRA experiments when compute is available
- keep model artifacts portable across Hugging Face, cloud GPUs, and self-hosted runtimes

## Repository map

```text
orbeai-model/
├── docs/          project vision, architecture and technical decisions
├── configs/       model and training configurations
├── training/      SFT / LoRA / QLoRA training code
├── datasets/      schemas and small public samples
├── evals/         benchmarks and evaluation results
├── experiments/   experiment logs and reproducibility notes
├── scripts/       utility scripts
└── .github/       repository collaboration files
```

## Artifact policy

Large model weights, checkpoints, full datasets, caches, and generated binaries do **not** belong in Git. They will live in dedicated model/data storage such as the Hugging Face Hub or equivalent infrastructure. GitHub tracks code, configs, documentation, small samples, and evaluation reports.

## Project tracking

Development is tracked in Linear under **OrbeAI Model**.

Current milestones:

- m0 · foundation
- m1 · dataset v0.1
- m2 · evals v0.1
- m3 · first fine-tune

## Current candidate models

The initial shortlist includes Qwen, Ministral, Gemma, and other open-weight models that meet our licensing, PT-BR, efficiency, fine-tuning, and deployment requirements. The final choice will be recorded as an architecture decision rather than hard-coded into the project identity.

## License

Repository licensing and model-derivative licensing will be defined after the foundation-model decision so that upstream terms are handled correctly.
