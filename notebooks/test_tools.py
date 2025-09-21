
# mypy: ignore-errors
"""
Arquivo de testes para ferramentas do assistente de email.
Configurado para ignorar erros do Mypy relacionados a imports locais.
"""

import sys
from pathlib import Path

# Add project root to Python path
project_root = Path(__file__).parent.parent
src_path = project_root / "src"
sys.path.insert(0, str(project_root))
sys.path.insert(0, str(src_path))

import pytest
from dotenv import load_dotenv

# Import dos módulos do projeto com type ignore para Mypy
from email_assistant.eval.email_dataset import email_inputs, expected_tool_calls  # type: ignore
from email_assistant.utils import format_messages_string, extract_tool_calls  # type: ignore
from email_assistant.email_assistant import email_assistant  # type: ignore
from langsmith import testing as t  # type: ignore

load_dotenv(".env")

@pytest.mark.langsmith
@pytest.mark.parametrize(
    "email_input, expected_calls",
    [   # Pick some examples with e-mail reply expected
        (email_inputs[0],expected_tool_calls[0]),
        (email_inputs[3],expected_tool_calls[3]),
    ],
)
def test_email_dataset_tool_calls(email_input, expected_calls):
    """Testa se o processamento de email contém as chamadas de ferramenta esperadas."""    
    # Executa o assistente de email
    result = email_assistant.invoke({"email_input": email_input})

    # Extrai chamadas de ferramenta da lista de mensagens
    extracted_tool_calls = extract_tool_calls(result['messages'])
            
    # Verifica se todas as chamadas de ferramenta esperadas estão nas extraídas
    missing_calls = [call for call in expected_calls if call.lower() not in extracted_tool_calls]

    t.log_outputs({
                "missing_calls": missing_calls,
                "extracted_tool_calls": extracted_tool_calls,
                "response": format_messages_string(result['messages'])
            })

    # Teste passa se não há chamadas esperadas faltando
    assert len(missing_calls) == 0
