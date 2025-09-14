# Agentes do Zero

Este repositório é um guia para construir agentes do zero. Evolui até um agente ["ambiente"](https://blog.langchain.dev/introducing-ambient-agents/) que pode gerenciar seus emails com conexão à API do Gmail. Está organizado em 4 seções, cada uma com um notebook e código correspondente no diretório `src/email_assistant`. Essas seções constroem desde os conceitos básicos de agentes, até avaliação de agentes, human-in-the-loop, e finalmente memória. Tudo isso se combina em um agente que você pode implantar, e os princípios podem ser aplicados a outros agentes em uma ampla gama de tarefas.

![overview](notebooks/img/overview.png)

## Configuração do Ambiente

### Versão do Python

* Certifique-se de estar usando Python 3.11 ou superior.
* Esta versão é necessária para compatibilidade otimizada com LangGraph.

```shell
python3 --version
```

### Chaves de API

* Se você não tem uma chave da API do Gemini, [você pode se inscrever](https://makersuite.google.com/).
* [Inscreva-se no LangSmith](https://smith.langchain.com/).
* Gere uma chave de API do LangSmith.

### Definir Variáveis de Ambiente

* Crie um arquivo `.env` no diretório raiz:

```shell
# Copie o arquivo .env.example para .env
cp .env.example .env
```

* Edite o arquivo `.env` com o seguinte:

```shell
LANGSMITH_API_KEY=sua_chave_api_langsmith
LANGSMITH_TRACING=true
LANGSMITH_PROJECT="interrupt-workshop"
GOOGLE_API_KEY=sua_chave_api_google
```

* Você também pode definir as variáveis de ambiente no seu terminal:

```shell
export LANGSMITH_API_KEY=sua_chave_api_langsmith
export LANGSMITH_TRACING=true
export GOOGLE_API_KEY=sua_chave_api_google
```

### Instalação de Pacotes

**Recomendado: Usando uv (mais rápido e confiável)*

```shell
# Instale uv se ainda não tiver
pip install uv

# Instale o pacote com dependências de desenvolvimento
uv sync --extra dev

# Ative o ambiente virtual
source .venv/bin/activate
```

**Alternativa: Usando pip*

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
# Certifique-se de ter uma versão recente do pip (necessário para instalações editáveis com pyproject.toml)
$ python3 -m pip install --upgrade pip
# Instale o pacote no modo editável
$ pip install -e .
```

> **⚠️ IMPORTANTE**: Não pule a etapa de instalação do pacote! Esta instalação editável é **obrigatória** para os notebooks funcionarem corretamente. O pacote é instalado como `interrupt_workshop` com nome de import `email_assistant`, permitindo que você importe de qualquer lugar com `from email_assistant import ...`

## Estrutura

O repositório está organizado em 4 seções, com um notebook para cada uma e código acompanhante no diretório `src/email_assistant`.

### Prefácio: LangGraph 101

Para uma breve introdução ao LangGraph e alguns dos conceitos usados neste repositório, veja o [notebook LangGraph 101](notebooks/langgraph_101.ipynb). Este notebook explica o básico de modelos de chat, chamada de ferramentas, agentes vs fluxos de trabalho, nós / arestas / memória do LangGraph, e LangGraph Studio.

### Construindo um agente

* Notebook: [notebooks/agent.ipynb](/notebooks/agent.ipynb)
* Código: [src/email_assistant/email_assistant.py](/src/email_assistant/email_assistant.py)

![overview-agent](notebooks/img/overview_agent.png)

Este notebook mostra como construir o assistente de email, combinando uma [etapa de triagem de email](https://langchain-ai.github.io/langgraph/tutorials/workflows/) com um agente que gerencia a resposta do email. Você pode ver o código vinculado para a implementação completa em `src/email_assistant/email_assistant.py`.

![Screenshot 2025-04-04 at 4 06 18 PM](notebooks/img/studio.png)

### Evaluation

* Notebook: [notebooks/evaluation.ipynb](/notebooks/evaluation.ipynb)

![overview-eval](notebooks/img/overview_eval.png)

Este notebook introduz a avaliação com um conjunto de dados de email em [eval/email_dataset.py](/eval/email_dataset.py). Mostra como executar avaliações usando Pytest e a API `evaluate` do LangSmith. Executa avaliação para respostas de email usando LLM-como-juiz, bem como avaliações para chamadas de ferramentas e decisões de triagem.

![Screenshot 2025-04-08 at 8 07 48 PM](notebooks/img/eval.png)

### Human-in-the-loop

* Notebook: [notebooks/hitl.ipynb](/notebooks/hitl.ipynb)
* Code: [src/email_assistant/email_assistant_hitl.py](/src/email_assistant/email_assistant_hitl.py)

![overview-hitl](notebooks/img/overview_hitl.png)

Este notebook mostra como adicionar human-in-the-loop (HITL), permitindo ao usuário revisar chamadas específicas de ferramentas (por exemplo, enviar email, agendar reunião). Para isso, usamos o [Agent Inbox](https://github.com/langchain-ai/agent-inbox) como interface para human in the loop. Você pode ver o código vinculado para a implementação completa em [src/email_assistant/email_assistant_hitl.py](/src/email_assistant/email_assistant_hitl.py).

![Agent Inbox showing email threads](notebooks/img/agent-inbox.png)

### Memory

* Notebook: [notebooks/memory.ipynb](/notebooks/memory.ipynb)
* Code: [src/email_assistant/email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py)

![overview-memory](notebooks/img/overview_memory.png)

Este notebook mostra como adicionar memória ao assistente de email, permitindo que aprenda com feedback do usuário e adapte-se às preferências ao longo do tempo. O assistente com memória habilitada ([email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py)) usa o [LangGraph Store](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory) para persistir memórias. Você pode ver o código vinculado para a implementação completa em [src/email_assistant/email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py).

## Connecting to APIs

The above notebooks using mock email and calendar tools.

### Gmail Integration and Deployment

Set up Google API credentials following the instructions in [Gmail Tools README](src/email_assistant/tools/gmail/README.md).

The README also explains how to deploy the graph to LangGraph Platform.

The full implementation of the Gmail integration is in [src/email_assistant/email_assistant_hitl_memory_gmail.py](/src/email_assistant/email_assistant_hitl_memory_gmail.py).

## Running Tests

The repository includes an automated test suite to evaluate the email assistant.

Tests verify correct tool usage and response quality using LangSmith for tracking.

### Running Tests with [run_all_tests.py](/tests/run_all_tests.py)

```shell
python tests/run_all_tests.py
```

### Test Results

Test results are logged to LangSmith under the project name specified in your `.env` file (`LANGSMITH_PROJECT`). This provides:

* Visual inspection of agent traces
* Detailed evaluation metrics
* Comparison of different agent implementations

### Available Test Implementations

The available implementations for testing are:

* `email_assistant` - Basic email assistant

### Testing Notebooks

You can also run tests to verify all notebooks execute without errors:

```shell
# Run all notebook tests
python tests/test_notebooks.py

# Or run via pytest
pytest tests/test_notebooks.py -v
```

## Future Extensions

Add [LangMem](https://langchain-ai.github.io/langmem/) to manage memories:

* Manage a collection of background memories.
* Add memory tools that can look up facts in the background memories.
