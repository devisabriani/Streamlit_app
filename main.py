import streamlit as st
from crewai import Agent, Task, Crew
from langchain.llms import OpenAI
from dotenv import load_dotenv
load_dotenv()

st.title("EduCrew")
st.markdown("*by Devis Abriani*")

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

openai_api_key = st.secrets["OPENAI_API_KEY"]

#openai_api_key = "abc"


