import streamlit as st
import os
from crewai import Agent
from langchain.llms import OpenAI

# Ottieni la chiave API dai secrets di Streamlit
openai_api_key = st.secrets["OPENAI_API_KEY"]

os.environ["OPENAI_API_KEY"] = openai_api_key

# Definisci il modello LLM con la chiave API corretta
llm = OpenAI(temperature=0.7)

# Crea l'agente
STEM_expert = Agent(
    role="Esperto STEM",
    goal="Rispondere a domande complesse in ambito scientifico",
    llm=llm,
    verbose=True
)

st.write("Agente configurato correttamente!")
