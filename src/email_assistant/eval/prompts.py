# Usado em /eval/evaluate_triage.py
TRIAGE_CLASSIFICATION_PROMPT = """

<Tarefa>
Você está avaliando a classificação de emails.

Eles devem ser classificados em uma das seguintes categorias:
- ignore
- notify
- respond

Você receberá:
- o email_input
- o raciocínio e decisão do agente como uma lista de mensagens
- a classificação correta

Seu trabalho é avaliar o raciocínio e decisão do agente relativo à classificação correta.
</Tarefa>

<email_input>
{inputs}
</email_input>

<agent_response>
{outputs}
</agent_response>

<correct_classification>
{reference_outputs}
</correct_classification>
"""

# Usado em /tests/test_email_assistant.py
RESPONSE_CRITERIA_SYSTEM_PROMPT = """Você está avaliando um assistente de email que trabalha em nome de um usuário.

Você verá uma sequência de mensagens, começando com um email enviado ao usuário.

Você então verá a resposta do assistente a este email em nome do usuário, que inclui quaisquer chamadas de ferramenta feitas (por exemplo, write_email, schedule_meeting, check_calendar_availability, done).

Você também verá uma lista de critérios que a resposta do assistente deve atender.

Seu trabalho é avaliar se a resposta do assistente atende TODOS os pontos de critério fornecidos.

INSTRUÇÕES IMPORTANTES DE AVALIAÇÃO:
1. A resposta do assistente é formatada como uma lista de mensagens.
2. Os critérios de resposta são formatados como pontos (•)
3. Você deve avaliar a resposta contra CADA ponto individualmente
4. TODOS os pontos devem ser atendidos para que a resposta receba uma nota 'True'
5. Para cada ponto, cite texto específico da resposta que satisfaz ou falha em satisfazê-lo
6. Seja objetivo e rigoroso em sua avaliação
7. Em sua justificativa, indique claramente quais critérios foram atendidos e quais não foram
7. Se QUALQUER critério não for atendido, a nota geral deve ser 'False'

Sua saída será usada para testes automatizados, então mantenha uma abordagem de avaliação consistente."""

# Usado em /tests/test_hitl.py
HITL_FEEDBACK_SYSTEM_PROMPT = """Você está avaliando a resposta de um assistente de email para determinar se atende critérios específicos.

Este é um assistente de email usado para responder a emails. Revise nossa resposta inicial de email e o feedback do usuário dado para atualizar a resposta do email. Aqui está o feedback: {feedback}. Avalie se a resposta final do email aborda o feedback que fornecemos."""

# Usado em /tests/test_memory.py
MEMORY_UPDATE_SYSTEM_PROMPT = """Este é um assistente de email que usa memória para atualizar suas preferências de resposta.

Revise as preferências de resposta iniciais e as preferências de resposta atualizadas. Avalie se as preferências de resposta atualizadas são mais precisas que as preferências de resposta iniciais."""