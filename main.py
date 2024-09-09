import streamlit as st
from crewai import Agent, Task, Crew
from crewai_tools import *

st.title("EduCrew")
st.markdown("*by Devis Abriani*")

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

openai_api_key = st.secrets["OPENAI_API_KEY"]
#os.environ["OPENAI_API_KEY"] = openai_api_key

#llm = OpenAI(temperature=0.7)

#openai_api_key = "abc"

st.write(crewai.__version__)
