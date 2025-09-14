from typing import Literal
from pydantic import BaseModel
from langchain_core.tools import tool

@tool
def write_email(to: str, subject: str, content: str) -> str:
    """Escrever e enviar um email."""
    # Resposta placeholder - em aplicação real enviaria email
    return f"Email enviado para {to} com assunto '{subject}' e conteúdo: {content}"

@tool
def triage_email(category: Literal["ignore", "notify", "respond"]) -> str:
    """Triar um email em uma das três categorias: ignore, notify, respond."""
    return f"Decisão de Classificação: {category}"

@tool
class Done(BaseModel):
    """Email foi enviado."""
    done: bool

@tool
class Question(BaseModel):
      """Pergunta para fazer ao usuário."""
      content: str