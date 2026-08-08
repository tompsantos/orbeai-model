# Architecture

## Development flow

```text
foundation model
      ↓
baseline evaluation
      ↓
OrbeAI dataset
      ↓
post-training (SFT / LoRA / QLoRA)
      ↓
evaluation + comparison
      ↓
model artifact
      ↓
portable deployment
```

## Separation of concerns

### GitHub
Stores source code, configs, documentation, small dataset samples, experiment metadata and evaluation reports.

### Linear
Tracks project decisions, milestones, issues, blockers and execution status.

### Model / dataset hub
Stores model weights, adapters, checkpoints, full datasets and model cards when those artifacts are ready to be published or persisted.

### Compute
Training may run on Hugging Face Jobs, Modal, another GPU cloud, or self-hosted infrastructure. Compute is intentionally decoupled from artifact storage.

## Portability target

Whenever technically compatible with the selected base model, the project should preserve paths for deployment through common runtimes such as Transformers, vLLM, llama.cpp / GGUF, Ollama, or equivalent tooling.
