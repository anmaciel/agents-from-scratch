from typing import Literal

from langchain.chat_models import init_chat_model

from email_assistant.tools import get_tools, get_tools_by_name
from email_assistant.tools.default.prompt_templates import AGENT_TOOLS_PROMPT
from email_assistant.prompts import triage_system_prompt, triage_user_prompt, agent_system_prompt, default_background, default_triage_instructions, default_response_preferences, default_cal_preferences
from email_assistant.schemas import State, RouterSchema, StateInput
from email_assistant.utils import parse_email, format_email_markdown

from langgraph.graph import StateGraph, START, END
from langgraph.types import Command
from dotenv import load_dotenv
load_dotenv(".env")

# Get tools
tools = get_tools()
tools_by_name = get_tools_by_name(tools)

# Initialize the LLM for use with router / structured output
llm = init_chat_model("gemini-2.5-flash", model_provider="google-genai", temperature=0.0)
llm_router = llm.with_structured_output(RouterSchema) 

# Initialize the LLM, enforcing tool use (of any available tools) for agent
llm = init_chat_model("gemini-2.5-flash", model_provider="google-genai", temperature=0.0)
llm_with_tools = llm.bind_tools(tools, tool_choice="any")

# Nós
def llm_call(state: State):
    """LLM decide se deve chamar uma ferramenta ou não"""

    return {
        "messages": [
            llm_with_tools.invoke(
                [
                    {"role": "system", "content": agent_system_prompt.format(
                        tools_prompt=AGENT_TOOLS_PROMPT,
                        background=default_background,
                        response_preferences=default_response_preferences, 
                        cal_preferences=default_cal_preferences)
                    },
                    
                ]
                + state["messages"]
            )
        ]
    }

def tool_node(state: State):
    """Executa a chamada da ferramenta"""

    result = []
    for tool_call in state["messages"][-1].tool_calls:
        tool = tools_by_name[tool_call["name"]]
        observation = tool.invoke(tool_call["args"])
        result.append({"role": "tool", "content" : observation, "tool_call_id": tool_call["id"]})
    return {"messages": result}

# Função de aresta condicional
def should_continue(state: State) -> Literal["Action", "__end__"]:
    """Redireciona para Action ou termina se a ferramenta Done foi chamada"""
    messages = state["messages"]
    last_message = messages[-1]
    if last_message.tool_calls:
        for tool_call in last_message.tool_calls: 
            if tool_call["name"] == "Done":
                return END
            else:
                return "Action"

# Construir fluxo de trabalho
agent_builder = StateGraph(State)

# Adicionar nós
agent_builder.add_node("llm_call", llm_call)
agent_builder.add_node("environment", tool_node)

# Adicionar arestas para conectar nós
agent_builder.add_edge(START, "llm_call")
agent_builder.add_conditional_edges(
    "llm_call",
    should_continue,
    {
        # Nome retornado por should_continue : Nome do próximo nó a visitar
        "Action": "environment",
        END: END,
    },
)
agent_builder.add_edge("environment", "llm_call")

# Compilar o agente
agent = agent_builder.compile()

def triage_router(state: State) -> Command[Literal["response_agent", "__end__"]]:
    """Analisa o conteúdo do email para decidir se devemos responder, notificar ou ignorar.

    A etapa de triagem evita que o assistente perca tempo com:
    - Emails de marketing e spam
    - Anúncios da empresa
    - Mensagens destinadas a outras equipes
    """
    author, to, subject, email_thread = parse_email(state["email_input"])
    system_prompt = triage_system_prompt.format(
        background=default_background,
        triage_instructions=default_triage_instructions
    )

    user_prompt = triage_user_prompt.format(
        author=author, to=to, subject=subject, email_thread=email_thread
    )

    # Cria markdown do email para Agent Inbox em caso de notificação  
    email_markdown = format_email_markdown(subject, author, to, email_thread)

    # Executa o LLM roteador
    result = llm_router.invoke(
        [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt},
        ]
    )

    # Decisão
    classification = result.classification

    if classification == "respond":
        print("📧 Classificação: RESPONDER - Este email requer uma resposta")
        goto = "response_agent"
        # Adiciona o email às mensagens
        update = {
            "classification_decision": result.classification,
            "messages": [{"role": "user",
                            "content": f"Responder ao email: {email_markdown}"
                        }],
        }
    elif result.classification == "ignore":
        print("🚫 Classificação: IGNORAR - Este email pode ser ignorado com segurança")
        update =  {
            "classification_decision": result.classification,
        }
        goto = END
    elif result.classification == "notify":
        # Na vida real, isso faria algo diferente
        print("🔔 Classificação: NOTIFICAR - Este email contém informações importantes")
        update = {
            "classification_decision": result.classification,
        }
        goto = END
    else:
        raise ValueError(f"Classificação inválida: {result.classification}")
    return Command(goto=goto, update=update)

# Construir fluxo de trabalho
overall_workflow = (
    StateGraph(State, input=StateInput)
    .add_node(triage_router)
    .add_node("response_agent", agent)
    .add_edge(START, "triage_router")
)

email_assistant = overall_workflow.compile()