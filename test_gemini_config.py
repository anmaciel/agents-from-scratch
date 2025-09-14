#!/usr/bin/env python3

"""
Teste simples para verificar a configuração do Gemini 2.5 Flash.
"""

import os
from dotenv import load_dotenv

def test_environment_variables():
    """Testar se as variáveis de ambiente necessárias estão definidas."""
    load_dotenv()

    google_api_key = os.getenv('GOOGLE_API_KEY')
    langsmith_api_key = os.getenv('LANGSMITH_API_KEY')

    print("=== Teste de Variáveis de Ambiente ===")
    if google_api_key:
        print(f"✅ GOOGLE_API_KEY: Configurada (começa com: {google_api_key[:10]}...)")
    else:
        print("❌ GOOGLE_API_KEY: Não encontrada")
        return False

    if langsmith_api_key:
        print(f"✅ LANGSMITH_API_KEY: Configurada (começa com: {langsmith_api_key[:10]}...)")
    else:
        print("⚠️ LANGSMITH_API_KEY: Não encontrada (opcional para teste)")

    return True

def test_gemini_import():
    """Testar se as dependências do Gemini podem ser importadas."""
    print("\n=== Teste de Imports ===")
    try:
        from langchain.chat_models import init_chat_model
        print("✅ LangChain chat_models importado com sucesso")

        # Tenta inicializar o modelo (sem fazer chamadas)
        try:
            model = init_chat_model("gemini-2.5-flash", model_provider="google-genai", temperature=0)
            print("✅ Modelo Gemini 2.5 Flash inicializado com sucesso")
            return True
        except Exception as e:
            print(f"❌ Erro ao inicializar Gemini 2.5 Flash: {e}")
            return False

    except Exception as e:
        print(f"❌ Erro de import: {e}")
        return False

def test_basic_functionality():
    """Testar funcionalidade básica sem fazer chamadas de API."""
    print("\n=== Teste de Funcionalidade Básica ===")
    try:
        from email_assistant.prompts import triage_system_prompt
        from email_assistant.schemas import RouterSchema

        # Teste básico de schema
        print("✅ Prompts e schemas carregados com sucesso")
        print(f"✅ Prompt de triagem tem {len(triage_system_prompt)} caracteres")

        return True

    except Exception as e:
        print(f"❌ Erro no teste básico: {e}")
        return False

if __name__ == "__main__":
    print("🧪 Iniciando validação da configuração Gemini 2.5 Flash...\n")

    success = True
    success &= test_environment_variables()
    success &= test_gemini_import()
    success &= test_basic_functionality()

    print("\n" + "="*50)
    if success:
        print("🎉 SUCESSO: Todas as validações passaram!")
        print("✨ O projeto está configurado corretamente para usar Gemini 2.5 Flash")
    else:
        print("❌ FALHA: Algumas validações falharam")
        print("🔧 Verifique a configuração e as dependências")
    print("="*50)