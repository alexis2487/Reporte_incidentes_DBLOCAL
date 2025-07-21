import os
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnableSequence


def create_agent():
    # Obtener el modelo desde las variables de entorno o usar llama3 por defecto
    model = os.getenv("LLM_MODEL", "llama3")
    llm = ChatOllama(model=model)

    # Prompt base del agente de ciberseguridad
    prompt = ChatPromptTemplate.from_messages([
        ("system", "Eres un agente de ciberseguridad llamado BlackTechSec. Sé útil, directo y profesional."),
        ("user", "{input}")
    ])

    # Crear la secuencia: prompt -> modelo
    chain = RunnableSequence(prompt | llm)

    return chain