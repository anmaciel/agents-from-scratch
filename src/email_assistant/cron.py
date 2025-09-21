"""
Job automatizado (cron) para buscar e processar emails do Gmail.

Este módulo implementa um workflow LangGraph que:
1. Busca emails recentes do Gmail
2. Processa cada email usando o assistente de IA
3. Executa ações automáticas (responder, agendar, etc.)
4. Integra com LangGraph Platform para execução distribuída

Exemplo de uso:
    from email_assistant.cron import graph, JobKickoff

    # Configurar job para buscar emails dos últimos 30 minutos
    job_config = JobKickoff(
        email="seu.email@gmail.com",
        minutes_since=30,
        graph_name="email_assistant_hitl_memory_gmail",
        url="http://127.0.0.1:2024"
    )

    # Executar job
    result = await graph.ainvoke(job_config)
    print(f"Status: {result['status']}")

Para usar em um cron real:
    # Executar a cada hora
    0 * * * * cd /path/to/project && python -c "
    import asyncio
    from email_assistant.cron import graph, JobKickoff

    config = JobKickoff(email='seu@email.com')
    result = asyncio.run(graph.ainvoke(config))
    print(f'Cron job completed: {result}')
    "
"""

import os
import sys
import asyncio
from typing import Dict, Any, TypedDict
from dataclasses import dataclass, field
from langgraph.graph import StateGraph, START, END
from email_assistant.tools.gmail.run_ingest import fetch_and_process_emails

@dataclass(kw_only=True)
class JobKickoff:
    """State for the email ingestion cron job"""
    email: str
    minutes_since: int = 60
    graph_name: str = "email_assistant_hitl_memory_gmail"
    url: str = "http://127.0.0.1:2024"
    include_read: bool = False
    rerun: bool = False
    early: bool = False
    skip_filters: bool = False

async def main(state: JobKickoff):
    """Executar o processo de ingestão de email"""
    print(f"Iniciando job para buscar emails dos últimos {state.minutes_since} minutos")
    print(f"Email: {state.email}")
    print(f"URL: {state.url}")
    print(f"Graph name: {state.graph_name}")
    
    try:
        # Convert state to args object for fetch_and_process_emails
        class Args:
            def __init__(self, **kwargs: Any):
                self.email: str = ""
                self.minutes_since: int = 60
                self.graph_name: str = ""
                self.url: str = ""
                self.include_read: bool = False
                self.rerun: bool = False
                self.early: bool = False
                self.skip_filters: bool = False

                for key, value in kwargs.items():
                    setattr(self, key, value)
                print(f"Args criado com atributos: {dir(self)}")

        args = Args(
            email=state.email,
            minutes_since=state.minutes_since,
            graph_name=state.graph_name,
            url=state.url,
            include_read=state.include_read,
            rerun=state.rerun,
            early=state.early,
            skip_filters=state.skip_filters
        )
        
        # Imprimir email e URL para verificar se estão sendo passados corretamente
        print(f"Email dos Args: {args.email}")
        print(f"URL dos Args: {args.url}")
        
        # Run the ingestion process
        print("Starting fetch_and_process_emails...")
        result = await fetch_and_process_emails(args)
        print(f"fetch_and_process_emails returned: {result}")
        
        # Return the result status
        return {"status": "success" if result == 0 else "error", "exit_code": result}
    except Exception as e:
        import traceback
        print(f"Error in cron job: {str(e)}")
        print(traceback.format_exc())
        return {"status": "error", "error": str(e)}

# Build the graph
workflow = StateGraph(JobKickoff)
workflow.add_node("ingest_emails", main)
workflow.set_entry_point("ingest_emails")
graph = workflow.compile()