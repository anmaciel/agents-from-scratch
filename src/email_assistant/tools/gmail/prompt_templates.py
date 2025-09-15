"""Templates de prompts de ferramentas para integração Gmail."""

# Prompt de ferramentas Gmail para inserção em prompts de sistema do agente
GMAIL_TOOLS_PROMPT = """
1. fetch_emails_tool(email_address, minutes_since) - Buscar emails recentes do Gmail
2. send_email_tool(email_id, response_text, email_address, additional_recipients) - Enviar uma resposta a uma thread de email
3. check_calendar_tool(dates) - Verificar disponibilidade do Google Calendar para datas específicas
4. schedule_meeting_tool(attendees, title, start_time, end_time, organizer_email, timezone) - Agendar uma reunião e enviar convites
5. triage_email(ignore, notify, respond) - Triar emails em uma das três categorias
6. Done - Email foi enviado
"""

# Prompt de ferramentas combinadas (padrão + Gmail) para integração completa
COMBINED_TOOLS_PROMPT = """
1. fetch_emails_tool(email_address, minutes_since) - Buscar emails recentes do Gmail
2. send_email_tool(email_id, response_text, email_address, additional_recipients) - Enviar uma resposta a uma thread de email
3. check_calendar_tool(dates) - Verificar disponibilidade do Google Calendar para datas específicas
4. schedule_meeting_tool(attendees, title, start_time, end_time, organizer_email, timezone) - Agendar uma reunião e enviar convites
5. write_email(to, subject, content) - Redigir emails para destinatários específicos
6. triage_email(ignore, notify, respond) - Triar emails em uma das três categorias
7. check_calendar_availability(day) - Verificar slots de horário disponíveis para um determinado dia
8. Done - Email foi enviado
"""