"""Templates de prompts de ferramentas para o assistente de email."""

# Descrições padrão de ferramentas para inserção em prompts
STANDARD_TOOLS_PROMPT = """
1. triage_email(ignore, notify, respond) - Triar emails em uma das três categorias
2. write_email(to, subject, content) - Enviar emails para destinatários específicos
3. schedule_meeting(attendees, subject, duration_minutes, preferred_day, start_time) - Agendar reuniões no calendário onde preferred_day é um objeto datetime
4. check_calendar_availability(day) - Verificar slots de horário disponíveis para um determinado dia
5. Done - Email foi enviado
"""

# Descrições de ferramentas para workflow HITL
HITL_TOOLS_PROMPT = """
1. write_email(to, subject, content) - Enviar emails para destinatários específicos
2. schedule_meeting(attendees, subject, duration_minutes, preferred_day, start_time) - Agendar reuniões no calendário onde preferred_day é um objeto datetime
3. check_calendar_availability(day) - Verificar slots de horário disponíveis para um determinado dia
4. Question(content) - Fazer qualquer pergunta de acompanhamento ao usuário
5. Done - Email foi enviado
"""

# Descrições de ferramentas para workflow HITL com memória
# Nota: Ferramentas específicas de memória adicionais poderiam ser adicionadas aqui
HITL_MEMORY_TOOLS_PROMPT = """
1. write_email(to, subject, content) - Enviar emails para destinatários específicos
2. schedule_meeting(attendees, subject, duration_minutes, preferred_day, start_time) - Agendar reuniões no calendário onde preferred_day é um objeto datetime
3. check_calendar_availability(day) - Verificar slots de horário disponíveis para um determinado dia
4. Question(content) - Fazer qualquer pergunta de acompanhamento ao usuário
5. Done - Email foi enviado
"""

# Descrições de ferramentas para workflow do agente sem triagem
AGENT_TOOLS_PROMPT = """
1. write_email(to, subject, content) - Enviar emails para destinatários específicos
2. schedule_meeting(attendees, subject, duration_minutes, preferred_day, start_time) - Agendar reuniões no calendário onde preferred_day é um objeto datetime
3. check_calendar_availability(day) - Verificar slots de horário disponíveis para um determinado dia
4. Done - Email foi enviado
"""