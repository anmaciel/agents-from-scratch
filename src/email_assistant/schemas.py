from pydantic import BaseModel, Field
from typing_extensions import TypedDict, Literal
from langgraph.graph import MessagesState

class RouterSchema(BaseModel):
    """Analisar o email não lido e roteá-lo de acordo com seu conteúdo."""

    reasoning: str = Field(
        description="Raciocínio passo a passo por trás da classificação."
    )
    classification: Literal["ignore", "respond", "notify"] = Field(
        description="A classificação de um email: 'ignore' para emails irrelevantes, "
        "'notify' para informações importantes que não precisam de resposta, "
        "'respond' para emails que precisam de uma resposta",
    )

class StateInput(TypedDict):
    # Esta é a entrada para o estado
    email_input: dict

class State(MessagesState):
    # Esta classe de estado tem a chave messages construída
    email_input: dict
    classification_decision: Literal["ignore", "respond", "notify"]

class EmailData(TypedDict):
    id: str
    thread_id: str
    from_email: str
    subject: str
    page_content: str
    send_time: str
    to_email: str

class UserPreferences(BaseModel):
    """Preferências do usuário atualizadas baseadas no feedback do usuário."""
    chain_of_thought: str = Field(description="Raciocínio sobre quais preferências do usuário precisam ser adicionadas/atualizadas se necessário")
    user_preferences: str = Field(description="Preferências do usuário atualizadas")