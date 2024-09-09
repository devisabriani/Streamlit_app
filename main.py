import os
from crewai import Agent
from langchain.llms import OpenAI

# Configura la chiave API OpenAI
os.environ["OPENAI_API_KEY"] = "la-tua-api-key"

# Definisci il modello LLM
llm = OpenAI(temperature=0.7)

# Crea un agente CrewAI
STEM_expert = Agent(
    role="Esperto STEM",
    goal="Rispondere a domande complesse in ambito scientifico",
    llm=llm,
    verbose=True
)

print("Agente configurato correttamente")
