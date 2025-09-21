"""Dataset de avaliação de emails com classificações de referência."""

# Email comum de resposta
STANDARD_EMAIL = {
    "author": "Alice Silva <alice.silva@empresa.com.br>",
    "to": "João Santos <joao.santos@empresa.com.br>",
    "subject": "Dúvida rápida sobre documentação da API",
    "email_thread": """Oi João,

Estava revisando a documentação da API para o novo serviço de autenticação e notei que alguns endpoints parecem estar faltando nas especificações. Pode me ajudar a esclarecer se isso foi intencional ou se devemos atualizar a documentação?

Especificamente, estou procurando:
- /auth/refresh
- /auth/validate

Obrigada!
Alice""",
}

# Email comum de notificação
NOTIFICATION_EMAIL = {
    "author": "Admin do Sistema <sysadmin@empresa.com.br>",
    "to": "Equipe de Desenvolvimento <dev@empresa.com.br>",
    "subject": "Manutenção programada - indisponibilidade do banco de dados",
    "email_thread": """Olá equipe,

Este é um lembrete de que realizaremos manutenção programada no banco de dados de produção hoje à noite das 2h às 4h. Durante este período, todos os serviços de banco de dados estarão indisponíveis.

Por favor, planejem seu trabalho adequadamente e garantam que não haja deployments críticos programados durante esta janela.

Obrigado,
Equipe Admin do Sistema"""
}

# Exemplos do dataset
email_input_1 = {
    "author": "Alice Silva <alice.silva@empresa.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Dúvida rápida sobre documentação da API",
    "email_thread": """Oi Bruno,

Estava revisando a documentação da API para o novo serviço de autenticação e notei que alguns endpoints parecem estar faltando nas especificações. Pode me ajudar a esclarecer se isso foi intencional ou se devemos atualizar a documentação?

Especificamente, estou procurando:
- /auth/refresh
- /auth/validate

Obrigada!
Alice""",
}

email_input_2 = {
    "author": "Carlos Mendes <carlos.mendes@parceiro.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Reunião para revisão do Q1 - vamos marcar?",
    "email_thread": """Oi Bruno!

Espero que esteja tudo bem. Preciso agendar nossa reunião trimestral de revisão do Q1.

Temos bastante coisa para discutir:
- Performance das vendas (muito boa por sinal!)
- Planejamento do Q2
- Novos produtos que estamos lançando
- Orçamento para marketing digital

Tenho disponibilidade na próxima semana:
- Terça-feira de manhã (mas prefiro evitar muito cedo)
- Quarta-feira depois das 14h
- Sexta-feira o dia todo

A reunião deve durar umas 2 horas. Que tal fazermos presencial no escritório de SP?

Abraços,
Carlos""",
}

email_input_3 = {
    "author": "Marina Costa <marina.costa@cliente.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Status do projeto - preciso de uma atualização",
    "email_thread": """Olá Bruno,

Estou acompanhando o desenvolvimento do projeto de integração e gostaria de uma atualização sobre o andamento.

Pontos específicos que preciso saber:
1. As funcionalidades de autenticação estão funcionando?
2. Quando podemos esperar a versão beta?
3. Há algum bloqueio que precise da nossa ajuda?

Temos uma apresentação para a diretoria na próxima sexta e preciso de dados atualizados.

Muito obrigada,
Marina""",
}

email_input_4 = {
    "author": "RH <rh@empresa.com.br>",
    "to": "Todos <todos@empresa.com.br>",
    "subject": "Lembrete: Prazo para entrega de documentos",
    "email_thread": """Caros colaboradores,

Este é um lembrete de que o prazo para entrega dos documentos do benefício médico é 15 de outubro.

Documentos necessários:
- Comprovante de renda atualizado
- Documentos dos dependentes
- Formulário preenchido

Favor enviar para rh@empresa.com.br até a data limite.

Atenciosamente,
Departamento de RH"""
}

email_input_5 = {
    "author": "GitHub <noreply@github.com>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "[langchain] Nova pull request #1234",
    "email_thread": """
Pull Request #1234: Implementar autenticação OAuth2

Detalhes:
- Autor: desenvolvedor@empresa.com.br
- Estado: Aberto
- Arquivos alterados: 15
- Linhas adicionadas: +245, -12

Ver no GitHub: https://github.com/langchain/repo/pull/1234

Esta é uma notificação automática do GitHub.
"""
}

email_input_6 = {
    "author": "Ana Souza <ana@empresa.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Bug crítico no sistema de pagamentos",
    "email_thread": """Oi Bruno,

Identificamos um bug crítico no sistema de pagamentos que está afetando as transações dos clientes.

Detalhes do problema:
- Transações estão falhando com erro 500
- Começou por volta das 14h30
- Afetando aprox. 30% das tentativas
- Log de erro em anexo

Preciso que você analise urgentemente. Os clientes estão reclamando e perdemos algumas vendas.

Obrigada,
Ana"""
}

email_input_7 = {
    "author": "Marketing <marketing@empresa.com.br>",
    "to": "Equipe Desenvolvimento <dev@empresa.com.br>",
    "subject": "Newsletter Semanal - Novidades da Empresa",
    "email_thread": """Olá pessoal!

Confira as principais novidades desta semana:

🚀 Lançamos a nova funcionalidade de relatórios
📈 Crescimento de 15% nas vendas este mês
👥 Bem-vindos aos novos membros da equipe
🎉 Festa da empresa será no dia 25!

Acompanhem mais detalhes no portal interno.

Equipe de Marketing"""
}

email_input_8 = {
    "author": "Suporte Técnico <suporte@fornecedor.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Resposta ao ticket #AB123 - Problema resolvido",
    "email_thread": """Olá Bruno,

Referente ao seu ticket #AB123 sobre a instabilidade no servidor.

Resolução aplicada:
✅ Identificamos alta utilização de memória
✅ Otimizamos as consultas do banco
✅ Reiniciamos os serviços afetados
✅ Sistema está funcionando normalmente

O monitoramento continuará por 24h para garantir estabilidade.

Caso tenha outras questões, entre em contato.

Atenciosamente,
Equipe de Suporte"""
}

email_input_9 = {
    "author": "Esposa <maria@email.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Não esqueça: consulta médica hoje às 16h",
    "email_thread": """Oi amor,

Só lembrando que você tem consulta com o Dr. Silva hoje às 16h.

A clínica fica na Av. Paulista, 1000 - sala 502.

Leva os exames que fizemos semana passada.

Beijo,
Maria"""
}

email_input_10 = {
    "author": "TechConf Brasil <info@techconf.com.br>",
    "to": "Bruno Martins <bruno@empresa.com.br>",
    "subject": "Últimos dias! Desconto early bird - TechConf 2024",
    "email_thread": """Olá Bruno!

⏰ Restam apenas 3 dias para aproveitar o desconto early bird da TechConf 2024!

🎟️ Desconto de 40% válido até 20/10
🗣️ Mais de 50 palestras sobre IA, Cloud e DevOps
🌟 Speakers internacionais confirmados
📍 São Paulo Convention Center

Garante sua vaga: www.techconf.com.br

Não perca essa oportunidade!

Equipe TechConf Brasil"""
}

# Lista de exemplos de email
EMAIL_DATASET = [
    email_input_1,
    email_input_2,
    email_input_3,
    email_input_4,
    email_input_5,
    email_input_6,
    email_input_7,
    email_input_8,
    email_input_9,
    email_input_10,
]

# Classificações esperadas para o dataset
EXPECTED_CLASSIFICATIONS = {
    "email_input_1": "respond",  # Pergunta técnica direta
    "email_input_2": "respond",  # Solicitação de reunião
    "email_input_3": "respond",  # Consulta de cliente sobre projeto
    "email_input_4": "notify",   # Lembrete de RH - importante mas não requer resposta
    "email_input_5": "notify",   # Notificação do GitHub
    "email_input_6": "respond",  # Bug crítico - requer ação
    "email_input_7": "ignore",   # Newsletter de marketing
    "email_input_8": "notify",   # Confirmação de resolução de ticket
    "email_input_9": "respond",  # Lembrete pessoal da família
    "email_input_10": "ignore", # Email promocional/marketing
}

# Aliases para compatibilidade com testes
email_inputs = EMAIL_DATASET
expected_tool_calls = [
    ["write_email"],  # email_input_1 - resposta direta
    ["schedule_meeting"],  # email_input_2 - agendar reunião
    ["write_email"],  # email_input_3 - resposta de status
    [],  # email_input_4 - apenas notificar
    [],  # email_input_5 - apenas notificar
    ["write_email"],  # email_input_6 - resposta urgente
    [],  # email_input_7 - ignorar
    [],  # email_input_8 - apenas notificar
    ["write_email"],  # email_input_9 - resposta pessoal
    [],  # email_input_10 - ignorar
]

# Lista de classificações de triagem esperadas (compatibilidade com evaluation.ipynb)
triage_outputs_list = [
    "respond",  # email_input_1 - resposta direta
    "respond",  # email_input_2 - agendar reunião
    "respond",  # email_input_3 - resposta de status
    "notify",   # email_input_4 - apenas notificar
    "notify",   # email_input_5 - apenas notificar
    "respond",  # email_input_6 - resposta urgente
    "ignore",   # email_input_7 - ignorar
    "notify",   # email_input_8 - apenas notificar
    "respond",  # email_input_9 - resposta pessoal
    "ignore",   # email_input_10 - ignorar
]

# Critérios de resposta para emails que requerem resposta
response_criteria_list = [
    "A resposta deve ser educada, profissional e endereçar especificamente as perguntas sobre os endpoints da API /auth/refresh e /auth/validate.",  # email_input_1
    "A resposta deve confirmar disponibilidade, sugerir horários específicos e ser amigável para networking profissional.",  # email_input_2
    "A resposta deve fornecer uma atualização clara sobre o status do projeto, endereçar os pontos específicos mencionados e incluir próximos passos.",  # email_input_3
    "",  # email_input_4 - apenas notificar, sem critério de resposta
    "",  # email_input_5 - apenas notificar, sem critério de resposta
    "A resposta deve demonstrar urgência, reconhecer a criticidade do problema e fornecer uma linha temporal clara para resolução.",  # email_input_6
    "",  # email_input_7 - ignorar, sem critério de resposta
    "",  # email_input_8 - apenas notificar, sem critério de resposta
    "A resposta deve ser carinhosa mas eficiente, confirmando o compromisso e agradecendo pelo lembrete.",  # email_input_9
    "",  # email_input_10 - ignorar, sem critério de resposta
]

# Exemplos para dataset do LangSmith (evaluation.ipynb)
examples_triage = []
for i, email in enumerate(EMAIL_DATASET):
    examples_triage.append({
        "inputs": {"email_input": email},
        "outputs": {"classification": triage_outputs_list[i]}
    })