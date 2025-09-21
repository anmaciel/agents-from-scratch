# Agentes do Zero

Este repositório é um guia para construir agentes do zero.
Evolui até um agente ["ambiente"](https://blog.langchain.dev/introducing-ambient-agents/) que pode gerenciar seus emails com conexão à API do Gmail.
Está organizado em 4 seções, cada uma com um notebook e código correspondente no diretório `src/email_assistant`.
Essas seções constroem desde os conceitos básicos de agentes, até avaliação de agentes, human-in-the-loop, e finalmente memória.
Tudo isso se combina em um agente que você pode implantar, e os princípios podem ser aplicados a outros agentes em uma ampla gama de tarefas.

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

> **⚠️ IMPORTANTE**: Não pule a etapa de instalação do pacote!
Esta instalação editável é **obrigatória** para os notebooks funcionarem corretamente.
O pacote é instalado como `interrupt_workshop` com nome de import `email_assistant`, permitindo que você importe de qualquer lugar com `from email_assistant import ...`

## Estrutura

O repositório está organizado em 4 seções, com um notebook para cada uma e código acompanhante no diretório `src/email_assistant`.

### Prefácio: LangGraph 101

Para uma breve introdução ao LangGraph e alguns dos conceitos usados neste repositório, veja o [notebook LangGraph 101](notebooks/langgraph_101.ipynb).
Este notebook explica o básico de modelos de chat, chamada de ferramentas, agentes vs fluxos de trabalho, nós / arestas / memória do LangGraph, e LangGraph Studio.

### Construindo um agente

* Notebook: [notebooks/agent.ipynb](/notebooks/agent.ipynb)
* Código: [src/email_assistant/email_assistant.py](/src/email_assistant/email_assistant.py)

![overview-agent](notebooks/img/overview_agent.png)

Este notebook mostra como construir o assistente de email, combinando uma [etapa de triagem de email](https://langchain-ai.github.io/langgraph/tutorials/workflows/) com um agente que gerencia a
resposta do email.
Você pode ver o código vinculado para a implementação completa em `src/email_assistant/email_assistant.py`.

![Screenshot 2025-04-04 at 4 06 18 PM](notebooks/img/studio.png)

### Evaluation

* Notebook: [notebooks/evaluation.ipynb](/notebooks/evaluation.ipynb)

![overview-eval](notebooks/img/overview_eval.png)

Este notebook introduz a avaliação com um conjunto de dados de email em [eval/email_dataset.py](/eval/email_dataset.py). Mostra como executar avaliações usando Pytest e a API `evaluate` do LangSmith.
Executa avaliação para respostas de email usando LLM-como-juiz, bem como avaliações para chamadas de ferramentas e decisões de triagem.

![Screenshot 2025-04-08 at 8 07 48 PM](notebooks/img/eval.png)

### Human-in-the-loop

* Notebook: [notebooks/hitl.ipynb](/notebooks/hitl.ipynb)
* Code: [src/email_assistant/email_assistant_hitl.py](/src/email_assistant/email_assistant_hitl.py)

![overview-hitl](notebooks/img/overview_hitl.png)

Este notebook mostra como adicionar human-in-the-loop (HITL), permitindo ao usuário revisar chamadas específicas de ferramentas (por exemplo, enviar email, agendar reunião).
Para isso, usamos o [Agent Inbox](https://github.com/langchain-ai/agent-inbox) como interface para human in the loop. Você pode ver o código vinculado para a implementação completa em [src/email_assistant/email_assistant_hitl.py](/src/email_assistant/email_assistant_hitl.py).

![Agent Inbox showing email threads](notebooks/img/agent-inbox.png)

### Memory

* Notebook: [notebooks/memory.ipynb](/notebooks/memory.ipynb)
* Code: [src/email_assistant/email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py)

![overview-memory](notebooks/img/overview_memory.png)

Este notebook mostra como adicionar memória ao assistente de email, permitindo que aprenda com feedback do usuário e adapte-se às preferências ao longo do tempo.
O assistente com memória habilitada ([email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py))
usa o [LangGraph Store](https://langchain-ai.github.io/langgraph/concepts/memory/#long-term-memory) para persistir memórias.
Você pode ver o código vinculado para a implementação completa em [src/email_assistant/email_assistant_hitl_memory.py](/src/email_assistant/email_assistant_hitl_memory.py).

## Executando como Scripts Python

Além dos notebooks educacionais, você pode executar os agentes diretamente como scripts Python:

### Scripts Disponíveis

```shell
# 1. LangGraph 101 - Conceitos básicos
python src/email_assistant/langgraph_101.py

# 2. Assistente de Email básico
python src/email_assistant/email_assistant.py

# 3. Assistente com Human-in-the-Loop
python src/email_assistant/email_assistant_hitl.py

# 4. Assistente com Human-in-the-Loop e Memória
python src/email_assistant/email_assistant_hitl_memory.py

# 5. Assistente com integração Gmail (requer configuração adicional)
python src/email_assistant/email_assistant_hitl_memory_gmail.py
```

### Exemplo de Uso

Para testar um script específico, você pode executar:

```python
# Exemplo: executar o assistente básico
from email_assistant.email_assistant import email_assistant
from email_assistant.schemas import StateInput

# Email de exemplo
email_input = """
De: cliente@exemplo.com
Para: suporte@empresa.com
Assunto: Dúvida sobre produto

Olá,

Gostaria de saber mais informações sobre o produto X.
Podem me ajudar?

Obrigado!
"""

# Executar o assistente
result = email_assistant.invoke(StateInput(email_input=email_input))
print(result)
```

## Automação com Jobs Cron

Para automação completa, o projeto inclui um job cron que busca e processa emails automaticamente:

### Job Automatizado (cron.py)

O `src/email_assistant/cron.py` implementa um workflow LangGraph que:

1. 🔍 **Busca emails** recentes do Gmail
2. 🤖 **Processa automaticamente** cada email usando o assistente de IA
3. ⚡ **Executa ações** (responder, agendar reuniões, etc.)
4. 🌐 **Integra** com LangGraph Platform para execução distribuída

### Como usar o Job Cron

**1. Execução programática:**

```python
from email_assistant.cron import graph, JobKickoff

# Configurar job para buscar emails dos últimos 30 minutos
config = JobKickoff(
    email="seu@gmail.com",
    minutes_since=30,
    graph_name="email_assistant_hitl_memory_gmail",
    url="http://127.0.0.1:2024"  # LangGraph Platform
)

# Executar job
result = await graph.ainvoke(config)
print(f"Status: {result['status']}")
```

**2. Cron real (Linux/macOS):**

```bash
# Executar a cada hora
0 * * * * cd /path/to/project && python -c "
import asyncio
from email_assistant.cron import graph, JobKickoff

config = JobKickoff(email='seu@gmail.com')
result = asyncio.run(graph.ainvoke(config))
print(f'Cron job completed: {result}')
"

# Executar a cada 15 minutos
*/15 * * * * cd /path/to/project && python -c "..."
```

**3. Teste/desenvolvimento:**

```bash
# Executar uma vez para teste
python -c "
import asyncio
from email_assistant.cron import graph, JobKickoff
result = asyncio.run(graph.ainvoke(JobKickoff(email='test@gmail.com')))
print(result)
"
```

### Configurações do JobKickoff

| Parâmetro | Tipo | Padrão | Descrição |
|-----------|------|--------|-----------|
| `email` | str | **obrigatório** | Seu endereço Gmail |
| `minutes_since` | int | 60 | Buscar emails dos últimos X minutos |
| `graph_name` | str | "email_assistant_hitl_memory_gmail" | Nome do grafo LangGraph |
| `url` | str | "<http://127.0.0.1:2024>" | URL do LangGraph Platform |
| `include_read` | bool | False | Incluir emails já lidos |
| `skip_filters` | bool | False | Pular filtros de thread |

## Conectando a APIs

Os notebooks acima usam ferramentas mock de email e calendário.

### Integração Gmail e Deploy

Configure as credenciais da API do Google seguindo as instruções em [Gmail Tools README](src/email_assistant/tools/gmail/README.md).

O README também explica como fazer deploy do grafo na LangGraph Platform.

A implementação completa da integração Gmail está em [src/email_assistant/email_assistant_hitl_memory_gmail.py](/src/email_assistant/email_assistant_hitl_memory_gmail.py).

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
