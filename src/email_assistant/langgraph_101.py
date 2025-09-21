from typing import Literal, cast
from langchain.chat_models import init_chat_model
from langchain.tools import tool
from langchain_core.messages import AIMessage, ToolMessage
from langgraph.graph import MessagesState, StateGraph, END, START
from dotenv import load_dotenv
load_dotenv(".env")

@tool
def write_email(to: str, subject: str, content: str) -> str:
    """Escrever e enviar um email."""
    # Placeholder response - in real app would send email
    return f"Email enviado para {to} com assunto '{subject}' e conteúdo: {content}"

llm = init_chat_model("gemini-2.5-flash", model_provider="google-genai", temperature=0)
model_with_tools = llm.bind_tools([write_email], tool_choice="any")

def call_llm(state: MessagesState) -> MessagesState:
    """Run LLM"""
    output = model_with_tools.invoke(state["messages"])
    return {"messages": [output]}

def run_tool(state: MessagesState) -> MessagesState:
    """Performs the tool call"""
    result = []
    last_message = state["messages"][-1]

    # Type guard: ensure we have an AIMessage with tool_calls
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        ai_message = cast(AIMessage, last_message)
        for tool_call in ai_message.tool_calls:
            observation = write_email.invoke(tool_call["args"])
            tool_message = ToolMessage(
                content=observation,
                tool_call_id=tool_call["id"]
            )
            result.append(tool_message)
    return {"messages": result}

def should_continue(state: MessagesState) -> Literal["run_tool", "__end__"]:
    """Route to tool handler, or end if Done tool called"""

    # Get the last message
    messages = state["messages"]
    last_message = messages[-1]

    # Type guard: check if it's an AIMessage with tool_calls
    if hasattr(last_message, "tool_calls") and last_message.tool_calls:
        return "run_tool"
    # Otherwise, we stop (reply to the user)
    return "__end__"

workflow = StateGraph(MessagesState)
workflow.add_node("call_llm", call_llm)
workflow.add_node("run_tool", run_tool)
workflow.add_edge(START, "call_llm")
workflow.add_conditional_edges("call_llm", should_continue, {"run_tool": "run_tool", END: END})
workflow.add_edge("run_tool", END)

app = workflow.compile()