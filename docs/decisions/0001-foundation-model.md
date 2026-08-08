# ADR 0001 — Foundation model inicial

- status: accepted
- date: 2026-08-08

## context

A OrbeAI Model v0.1 precisa de um foundation model open-weight que permita post-training reproduzível, uso comercial compatível, boa portabilidade, suporte moderno de tooling e custo de experimentação baixo o suficiente para iteração frequente.

## decision

Adotar `Qwen/Qwen3.5-4B-Base` como foundation model inicial da OrbeAI Model v0.1.

O modelo possui aproximadamente 4.66B parâmetros, arquitetura Qwen3.5, distribuição em safetensors, integração com Transformers, capacidade multimodal image-text-to-text e licença Apache-2.0.

A variante Base foi escolhida como ponto de partida para que o comportamento de assistente e a especialização Orbe sejam introduzidos pelo nosso pipeline de post-training, em vez de apenas ajustar um modelo já instruído.

## rationale

1. tamanho adequado para experimentação e LoRA/QLoRA com custo controlado;
2. licença Apache-2.0, simplificando uso comercial e criação de derivados;
3. ecossistema amplo e compatibilidade com ferramentas modernas de fine-tuning e inferência;
4. arquitetura multimodal, preservando espaço de evolução futura;
5. existência de uma linha natural de escala para `Qwen/Qwen3.5-9B` caso os testes mostrem necessidade de mais capacidade;
6. forte adoção do Qwen3.5 no Hugging Face, reduzindo risco de tooling imaturo.

## alternatives considered

### Qwen/Qwen3.5-9B

Excelente candidato para uma segunda etapa, mas aproximadamente dobra o número de parâmetros e aumenta custo de treino e inferência antes de validarmos dataset, evals e pipeline.

### mistralai/Ministral-3-3B-Base-2512

Também é Apache-2.0, compacto e explicitamente multilíngue. Permanece como principal plano B caso Qwen3.5 apresente problemas relevantes em PT-BR, tooling ou post-training.

### google/gemma-4-E2B-it

Modelo multimodal moderno e Apache-2.0, mas a variante analisada é instruction-tuned. Para o objetivo inicial, preferimos uma variante Base e uma linhagem de post-training mais diretamente controlada pela OrbeAI.

### openai/gpt-oss-20b

Interessante para uma fase posterior, porém grande demais para ser o primeiro laboratório econômico da OrbeAI Model.

## consequences

- baseline principal: `Qwen/Qwen3.5-4B-Base`;
- referência instruct para comparação: `Qwen/Qwen3.5-4B`;
- plano B: `mistralai/Ministral-3-3B-Base-2512`;
- caminho de escala: `Qwen/Qwen3.5-9B`;
- o próximo trabalho passa a ser definir schema, curadoria e critérios de qualidade do dataset SFT v0.1;
- a escolha poderá ser revisada após baseline/evals, mas qualquer troca deverá gerar um novo ADR.
