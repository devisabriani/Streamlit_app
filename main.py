import streamlit as st
from crewai import Agent, Task, Crew

# Verifica se l'ambiente è configurato correttamente
try:
    agent = Agent()  # Crea un agente CrewAI per testare l'importazione
    print("CrewAI importato correttamente!")
except ImportError as e:
    st.error(f"Errore nell'importazione di CrewAI: {e}")

# Resto del tuo codice
