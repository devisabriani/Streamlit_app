from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from crewai_tools import (
    DirectoryReadTool,
    FileReadTool,
    SerperDevTool,
    WebsiteSearchTool
)

st.title("EduCrew")
st.markdown("*by Devis Abriani*")

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

openai_api_key = st.secrets["OPENAI_API_KEY"]

#openai_api_key = "abc"

st.write("Sito web in fase di ampliamento. Non operativo.")

wow = Agent(
  role="Batman",
  goal="Sconfiggere il crimine",
  backstory="Sono Batman!",
  verbose=True,
  tools=[]
)


