from datetime import datetime
from langchain_core.tools import tool

@tool
def schedule_meeting(
    attendees: list[str], subject: str, duration_minutes: int, preferred_day: datetime, start_time: int
) -> str:
    """Agendar uma reunião no calendário."""
    # Resposta placeholder - em aplicação real verificaria calendário e agendaria
    date_str = preferred_day.strftime("%A, %d de %B de %Y")
    return f"Reunião '{subject}' agendada para {date_str} às {start_time}h por {duration_minutes} minutos com {len(attendees)} participantes"

@tool
def check_calendar_availability(day: str) -> str:
    """Verificar disponibilidade do calendário para um determinado dia."""
    # Resposta placeholder - em aplicação real verificaria calendário real
    return f"Horários disponíveis em {day}: 9:00, 14:00, 16:00"
