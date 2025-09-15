# Ferramentas de Integração Gmail

Conecte seu assistente de email às APIs do Gmail e Google Calendar.

## Grafo

O grafo `src/email_assistant/email_assistant_hitl_memory_gmail.py` está configurado para usar ferramentas Gmail.

Você simplesmente precisa executar a configuração abaixo para obter as credenciais necessárias para executar o grafo com seu próprio email.

## Configurar Credenciais

### 1. Configurar Projeto Google Cloud e Habilitar APIs Necessárias

#### Habilitar APIs Gmail e Calendar

1. Vá para a [Biblioteca de APIs Google e habilite a API Gmail](https://developers.google.com/workspace/gmail/api/quickstart/python#enable_the_api)
2. Vá para a [Biblioteca de APIs Google e habilite a API Google Calendar](https://developers.google.com/workspace/calendar/api/quickstart/python#enable_the_api)

#### Criar Credenciais OAuth

1. [Autorizar credenciais para uma aplicação desktop](https://developers.google.com/workspace/gmail/api/quickstart/python#authorize_credentials_for_a_desktop_application)
2. Vá para Credentials → Create Credentials → OAuth Client ID
3. Defina Application Type como "Desktop app"
4. Clique em "Create"

> Nota: Se estiver usando um email pessoal (não Google Workspace) selecione "External" em "Audience"

![Screenshot 2025-04-26 at 7:43:57 AM](https://github.com/user-attachments/assets/718da39e-9b10-4a2a-905c-eda87c1c1126)

> Em seguida, adicione-se como usuário de teste

1. Salve o arquivo JSON baixado (você precisará dele no próximo passo)

### 2. Configurar Arquivos de Autenticação

1. Mova seu arquivo JSON de client secret baixado para o diretório `.secrets`

```bash
# Criar um diretório secrets
mkdir -p src/email_assistant/tools/gmail/.secrets

# Mover seu client secret baixado para o diretório secrets
mv /path/to/downloaded/client_secret.json src/email_assistant/tools/gmail/.secrets/secrets.json
```

1. Execute o script de configuração do Gmail

```bash
# Executar o script de configuração do Gmail
python src/email_assistant/tools/gmail/setup_gmail.py
```

- Isso abrirá uma janela do navegador para você autenticar com sua conta Google
- Isso criará um arquivo `token.json` no diretório `.secrets`
- Este token será usado para acesso à API Gmail

## Usar com Implantação Local

### 1. Executar o Script de Ingestão Gmail com Servidor LangGraph Local

1. Uma vez que você tenha a autenticação configurada, execute o servidor LangGraph localmente:

```txt
langgraph dev
```

1. Execute o script de ingestão em outro terminal com os parâmetros desejados:

```bash
python src/email_assistant/tools/gmail/run_ingest.py --email lance@langgraph.dev --minutes-since 1000
```

- Por padrão, isso usará a URL de implantação local (<http://127.0.0.1:2024>) e buscará emails dos últimos 1000 minutos.
- Usará o LangGraph SDK para passar cada email para o assistente de email executando localmente.
- Usará o grafo `email_assistant_hitl_memory_gmail`, que está configurado para usar ferramentas Gmail.

#### Parâmetros

- `--graph-name`: Nome do LangGraph a usar (padrão: "email_assistant_hitl_memory_gmail")
- `--email`: O endereço de email para buscar mensagens (alternativa para definir EMAIL_ADDRESS)
- `--minutes-since`: Processar apenas emails mais novos que esta quantidade de minutos (padrão: 60)
- `--url`: URL da implantação LangGraph (padrão: <http://127.0.0.1:2024>)
- `--rerun`: Processar emails que já foram processados (padrão: false)
- `--early`: Parar após processar um email (padrão: false)
- `--include-read`: Incluir emails que já foram lidos (por padrão apenas emails não lidos são processados)
- `--skip-filters`: Processar todos os emails sem filtrar (por padrão apenas as mensagens mais recentes em threads onde você não é o remetente são processadas)

#### Solução de Problemas

- **Emails ausentes?** A API Gmail aplica filtros para mostrar apenas emails importantes/primários por padrão. Você pode:
  - Aumentar o parâmetro `--minutes-since` para um valor maior (ex: 1000) para buscar emails de um período mais longo
  - Usar a flag `--include-read` para processar emails marcados como "lidos" (por padrão apenas emails não lidos são processados)
  - Usar a flag `--skip-filters` para incluir todas as mensagens (não apenas a mais recente em uma thread, incluindo as que você enviou)
  - Tentar executar com todas as opções para processar tudo: `--include-read --skip-filters --minutes-since 1000`
  - Usar a flag `--mock` para testar o sistema com emails simulados

### 2. Conectar ao Agent Inbox

Após a ingestão, você pode acessar todas as suas threads interrompidas no Agent Inbox (<https://dev.agentinbox.ai/>):

- URL de Implantação: <http://127.0.0.1:2024>
- ID do Assistente/Grafo: `email_assistant_hitl_memory_gmail`
- Nome: `Graph Name`

## Executar uma Implantação Hospedada

### 1. Implantar na Plataforma LangGraph

1. Navegue para a página de implantações no LangSmith
2. Clique em New Deployment
3. Conecte-o ao seu fork do [este repositório](https://github.com/langchain-ai/agents-from-scratch) e branch desejado
4. Dê um nome como `Yourname-Email-Assistant`
5. Adicione as seguintes variáveis de ambiente:
   - `GOOGLE_API_KEY`
   - `GMAIL_SECRET` - Este é o dicionário completo em `.secrets/secrets.json`
   - `GMAIL_TOKEN` - Este é o dicionário completo em `.secrets/token.json`
6. Clique em Submit
7. Obtenha a `API URL` (<https://your-email-assistant-xxx.us.langgraph.app>) da página de implantação

### 2. Executar Ingestão com Implantação Hospedada

Uma vez que sua implantação LangGraph esteja funcionando, você pode testar a ingestão de email com:

```bash
python src/email_assistant/tools/gmail/run_ingest.py --email lance@langchain.dev --minutes-since 2440 --include-read --url https://your-email-assistant-xxx.us.langgraph.app
```

### 3. Conectar ao Agent Inbox

Após a ingestão, você pode acessar todas as suas threads interrompidas no Agent Inbox (<https://dev.agentinbox.ai/>):

- URL de Implantação: <https://your-email-assistant-xxx.us.langgraph.app>
- ID do Assistente/Grafo: `email_assistant_hitl_memory_gmail`
- Nome: `Graph Name`
- Chave API LangSmith: `LANGSMITH_API_KEY`

### 4. Configurar Cron Job

Com uma implantação hospedada, você pode configurar um cron job para executar o script de ingestão em um intervalo especificado.

Para automatizar a ingestão de email, configure um cron job agendado usando o script de configuração incluído:

```bash
python src/email_assistant/tools/gmail/setup_cron.py --email lance@langchain.dev --url https://lance-email-assistant-4681ae9646335abe9f39acebbde8680b.us.langgraph.app
```

#### Parâmetros

- `--email`: Endereço de email para buscar mensagens (obrigatório)
- `--url`: URL de implantação LangGraph (obrigatório)
- `--minutes-since`: Buscar apenas emails mais novos que esta quantidade de minutos (padrão: 60)
- `--schedule`: Expressão de agendamento cron (padrão: "*/10* ** *" = a cada 10 minutos)
- `--graph-name`: Nome do grafo a usar (padrão: "email_assistant_hitl_memory_gmail")
- `--include-read`: Incluir emails marcados como lidos (por padrão apenas emails não lidos são processados) (padrão: false)

#### Como o Cron Funciona

O cron consiste em dois componentes principais:

1. **`src/email_assistant/cron.py`**: Define um grafo LangGraph simples que:
   - Chama a mesma função `fetch_and_process_emails` usada por `run_ingest.py`
   - Envolve isso em um grafo simples para que possa ser executado como um cron hospedado usando a Plataforma LangGraph

2. **`src/email_assistant/tools/gmail/setup_cron.py`**: Cria o cron job agendado:
   - Usa o LangGraph SDK `client.crons.create` para criar um cron job para o grafo `cron.py` hospedado

#### Gerenciando Cron Jobs

Para visualizar, atualizar ou deletar cron jobs existentes, você pode usar o LangGraph SDK:

```python
from langgraph_sdk import get_client

# Conectar à implantação
client = get_client(url="https://your-deployment-url.us.langgraph.app")

# Listar todos os cron jobs
cron_jobs = await client.crons.list()
print(cron_jobs)

# Deletar um cron job
await client.crons.delete(cron_job_id)
```

## Como a Ingestão Gmail Funciona

O processo de ingestão Gmail funciona em três estágios principais:

### 1. Parâmetros CLI → Consulta de Busca Gmail

Parâmetros CLI são traduzidos em uma consulta de busca Gmail:

- `--minutes-since 1440` → `after:TIMESTAMP` (emails das últimas 24 horas)
- `--email you@example.com` → `to:you@example.com OR from:you@example.com` (emails onde você é remetente ou destinatário)
- `--include-read` → remove filtro `is:unread` (inclui mensagens lidas)

Por exemplo, executando:

```txt
python run_ingest.py --email you@example.com --minutes-since 1440 --include-read
```

Cria uma consulta de busca da API Gmail como:

```txt
(to:you@example.com OR from:you@example.com) after:1745432245
```

### 2. Resultados da Busca → Processamento de Thread

Para cada mensagem retornada pela busca:

1. O script obtém o ID da thread
2. Usando este ID da thread, busca a **thread completa** com todas as mensagens
3. Mensagens na thread são ordenadas por data para identificar a mensagem mais recente
4. Dependendo das opções de filtragem, processa:
   - A mensagem específica encontrada na busca (comportamento padrão)
   - A mensagem mais recente na thread (ao usar `--skip-filters`)

### 3. Filtros Padrão e Comportamento `--skip-filters`

#### Filtros Padrão Aplicados

Sem `--skip-filters`, o sistema aplica estes três filtros em sequência:

1. **Filtro Não Lido** (controlado por `--include-read`):
   - Comportamento padrão: Processa apenas mensagens não lidas
   - Com `--include-read`: Processa mensagens lidas e não lidas
   - Implementação: Adiciona `is:unread` à consulta de busca Gmail
   - Este filtro acontece no nível de busca antes de qualquer mensagem ser recuperada

2. **Filtro de Remetente**:
   - Comportamento padrão: Pula mensagens enviadas pelo seu próprio endereço de email
   - Implementação: Verifica se seu email aparece no cabeçalho "From"
   - Lógica: `is_from_user = email_address in from_header`
   - Isso impede que o assistente responda aos seus próprios emails

3. **Filtro de Posição da Thread**:
   - Comportamento padrão: Processa apenas a mensagem mais recente em cada thread
   - Implementação: Compara ID da mensagem com a última mensagem na thread
   - Lógica: `is_latest_in_thread = message["id"] == last_message["id"]`
   - Impede processamento de mensagens antigas quando uma resposta mais nova existe

A combinação destes filtros significa que apenas a mensagem mais recente em cada thread que não foi enviada por você e não foi lida (a menos que `--include-read` seja especificado) será processada.

#### Efeito da Flag `--skip-filters`

Quando `--skip-filters` está habilitado:

1. **Ignora Filtros de Remetente e Posição da Thread**:
   - Mensagens enviadas por você serão processadas
   - Mensagens que não são as mais recentes na thread serão processadas
   - Lógica: `should_process = skip_filters or (not is_from_user and is_latest_in_thread)`

2. **Muda Qual Mensagem É Processada**:
   - Sem `--skip-filters`: Usa a mensagem específica encontrada pela busca
   - Com `--skip-filters`: Sempre usa a mensagem mais recente na thread
   - Mesmo se a mensagem mais recente não foi encontrada nos resultados da busca

3. **Filtro Não Lido Ainda Se Aplica (a menos que sobrescrito)**:
   - `--skip-filters` NÃO ignora o filtro de não lidos
   - Para processar mensagens lidas, você ainda deve usar `--include-read`
   - Isso é porque o filtro de não lidos acontece no nível de busca

Em resumo:

- Padrão: Processar apenas mensagens não lidas onde você não é o remetente e que são as mais recentes em sua thread
- `--skip-filters`: Processar todas as mensagens encontradas pela busca, usando a mensagem mais recente em cada thread
- `--include-read`: Incluir mensagens lidas na busca
- `--include-read --skip-filters`: Mais abrangente, processa a mensagem mais recente em todas as threads encontradas pela busca

## Limitações Importantes da API Gmail

A API Gmail tem várias limitações que afetam a ingestão de email:

1. **API Baseada em Busca**: Gmail não fornece um endpoint direto "obter todos os emails do período"
   - Toda recuperação de email depende da funcionalidade de busca do Gmail
   - Resultados de busca podem ter atraso para mensagens muito recentes (atraso de indexação)
   - Resultados de busca podem não incluir todas as mensagens que tecnicamente atendem aos critérios

2. **Processo de Recuperação em Duas Etapas**:
   - Busca inicial para encontrar IDs de mensagem relevantes
   - Recuperação secundária de thread para obter conversas completas
   - Este processo de duas etapas é necessário porque a busca não garante informações completas da thread
