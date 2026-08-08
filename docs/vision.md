# OrbeAI Model Vision

## Purpose

OrbeAI Model is the model-engineering track of the OrbeAI ecosystem. Its purpose is to create a portable, reproducible, PT-BR-first model lineage built from open-weight foundations rather than depending exclusively on third-party closed APIs.

## v0.1 direction

The first release should prioritize:

1. strong natural Brazilian Portuguese
2. clear, structured and useful responses
3. reliable instruction following
4. good reasoning for practical business and technical tasks
5. compatibility with tools / agentic workflows when supported by the base model
6. reproducible post-training and evaluation
7. deployability outside a single vendor

## Non-goals for v0.1

- training a foundation model from scratch
- maximizing benchmark scores at any cost
- storing model weights in GitHub
- replacing every closed model used by OrbeAI
- prematurely specializing for every Orbe vertical

## Guiding principle

The project should earn complexity gradually: baseline first, dataset second, evaluation before training, then progressively larger or more specialized models only when the evidence justifies it.
