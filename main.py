from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st

st.title("EduCrew")
st.markdown("*by Devis Abriani*")

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

openai_api_key = st.secrets["OPENAI_API_KEY"]

#openai_api_key = "abc"



STEM_expert = Agent(
    role="Pianificatore di lezioni di matematica",
    goal="Pianificare lezioni di matematica interessanti per una {class} di un liceo scientifico italiano riguardo {topic}",
    backstory="Sei un esperto in didattica STEM per le scuole italiane."
                "Conosci molto bene le connessioni fra la fisica e la matematica insegnate al liceo.",
    allow_delegation=False,
  	verbose=True
)


