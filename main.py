from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()
import os
import streamlit as st
from crewai_tools import FileReadTool

#st.set_page_config(page_title="EduCrew - by Devis Abriani")
st.title("EduCrew")
st.markdown("*by Devis Abriani*")

grado = st.selectbox("Scegli il grado scolastico:", [ "Primaria", "Secondaria di primo grado", "Secondaria di secondo grado"], index=2)

if grado == "Secondaria di secondo grado":
        tipo_scuola = st.selectbox("Scegli il tipo di scuola:", [
            "Liceo artistico",
            "Liceo classico",
            "Liceo linguistico",
            "Liceo musicale e coreutico",
            "Liceo scientifico",
            "Liceo scientifico – opzione Scienze applicate",
            "Liceo scientifico – sezione a indirizzo sportivo",
            "Liceo scienze umane",
            "Liceo scienze umane – opzione economico sociale",
            "Liceo del Made in Italy"], index=4)
else:
        tipo_scuola = grado

inclusione = st.selectbox("Inclusione:", [
        "Classe senza DSA e DVA",
        "Presenza di studenti con DSA (non attivo)",
        "Presenza di studenti DVA (non attivo)",
        "Presenza di studenti con DSA e di studenti DVA (non attivo)"], index=0)

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

#openai_api_key = st.secrets["OPENAI_API_KEY"]

openai_api_key = "abc"

#st.write("Sito web in fase di ampliamento. Non operativo.")

pdf_reader = FileReadTool()

STEM_expert = Agent(
    role="Pianificatore di lezioni di matematica e di educazione civica",
    goal="Pianificare lezioni di matematica e di educazione civica interessanti per una {class} di un liceo scientifico italiano riguardo {topic}",
    backstory="Sei un esperto in didattica STEM per le scuole italiane. Conosci molto bene le connessioni fra la fisica e la matematica insegnate al liceo. Conosci bene le nuove linee guida per l'educazione civica, delle quali hai accesso al file.",
    allow_delegation=False,
  	verbose=True,
    tools=[pdf_reader]
)

pdf_path = "resources/Linee-guida-Educazione-civica.pdf"

DigComp_expert = Agent(
    role="Esperto del framework europeo DigComp",
    goal="Revisionare la pianificazione dello STEM_expert in modo da aggiungere elementi dal DigComp.",
    backstory="Sei un esperto di DigComp e DigCompEdu.",
    allow_delegation=False,
    verbose=True
)


read_pdf_task = Task(
    description="Leggi il file PDF e fornisci un riassunto delle informazioni principali.",
    expected_output="Un riassunto delle informazioni contenute nel PDF.",
    tools=[pdf_reader],
    agent=STEM_expert
)



lesson = Task(
    description=(
        "Scrivi la pianificazione di una lezione di 50 minuti nella quale inserisci elementi di educazione civica secondo le nuove linee guida"
        "per una {class} di un liceo scientifico italiano riguardo {topic}"
    ),
    expected_output="Un documento in formato markdown con una pianificazione completa della lezione.",
    tools=[pdf_reader],
    agent=STEM_expert,
)

digcomp = Task(
    description=("Revisiona la pianificazione realizzata dallo STEM_expert"
                 "in modo da aggiungere elementi dal DigComp."),
    expected_output="Una pianificazione ben scritta in formato markdown",
    agent=DigComp_expert,
)

crew = Crew(
    agents=[STEM_expert],
    tasks=[lesson],
    verbose=True
)

if st.button("Pianifica Lezione"):
    if openai_api_key == "abc":
        st.write("Spiacente, attualmente il progetto è in fase di ampliamento e non è operativo.")
    else:
        with st.spinner("Pianificazione in corso..."):
            result = crew.kickoff(inputs={"topic": argomento, "class": classe})
            st.write(result)

