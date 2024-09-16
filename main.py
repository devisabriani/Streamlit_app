from crewai import Agent, Task, Crew
from dotenv import load_dotenv
load_dotenv()
import os
import io
import sys
import streamlit as st
import time
import base64
from crewai_tools import FileReadTool

st.set_page_config(layout="wide", page_title="EduCrew - by Devis Abriani")

st.title("EduCrew")
st.markdown("*by Devis Abriani*")

#col1, col2 = st.columns([1, 2])
#with col1:
#with col2:
    
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
    
metodologia = st.selectbox("Metodologia didattica:", ["Lezione frontale", "Cooperative learning", "Peer tutoring", "Learning by doing", "Inquiry Based Learning"], index=0)

inclusione = st.selectbox("Inclusione:", [
    "Classe senza DSA e DVA",
    "Presenza di studenti con DSA (non attivo)",
    "Presenza di studenti DVA (non attivo)",
    "Presenza di studenti con DSA e di studenti DVA (non attivo)"], index=0)

civica = st.checkbox("Lezione di educazione civica")

orientamento = st.checkbox("Lezione di orientamento")

framework = st.multiselect("Framework europei (opzionale):", ["DigComp", "EntreComp", "LifeComp"], default=[])

classe = st.text_input("Inserisci la classe:")
argomento = st.text_input("Inserisci l'argomento della lezione:")

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

#openai_api_key = "abc"
openai_api_key = st.secrets["OPENAI_API_KEY"]

# Funzione per convertire l'immagine in base64 per renderla utilizzabile da HTML
def get_base64_image(image_path):
    with open(image_path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# Caricamento delle immagini in base64 per essere usate nel componente HTML
image1 = get_base64_image("AI1.jpeg")
image2 = get_base64_image("AI2.jpeg")
image3 = get_base64_image("AI3.jpeg")
image4 = get_base64_image("AI4.jpeg")

# Codice HTML e JS con immagini convertite in base64
image_slider_html = f"""
<div style="text-align: center;">
    <img id="slider" src="data:image/jpeg;base64,{image1}" alt="Loading" width="300">
</div>
<script type="text/javascript">
    var currentIndex = 0;
    var images = [
        "data:image/jpeg;base64,{image1}",
        "data:image/jpeg;base64,{image2}",
        "data:image/jpeg;base64,{image3}",
        "data:image/jpeg;base64,{image4}"
    ];
    var interval = setInterval(function() {{
        document.getElementById("slider").src = images[currentIndex];
        currentIndex = (currentIndex + 1) % images.length;
    }}, 1000);

    // Funzione per fermare l'animazione
    function stopSlider() {{
        clearInterval(interval);
    }}
</script>
"""

if st.button("Pianifica Lezione"):
    if openai_api_key == "abc":
        st.write("Spiacente, attualmente il progetto è in fase di ampliamento e non è operativo.")
    else:

        col1, col2 = st.columns([1, 2])

        with col1:
            # Crea un placeholder per il contenuto dinamico
            placeholder = st.empty()
    
            # Mostra lo slider delle immagini all'interno del placeholder
            with placeholder:
                st.components.v1.html(image_slider_html, height=350)
    
            final_result = crew.kickoff(inputs={"topic": argomento, "class": classe})
    
            # Una volta ottenuta la risposta, aggiorna il contenuto e ferma l'animazione
            placeholder.empty()  # Svuota il placeholder per rimuovere lo slider
            # Aggiungi uno script per fermare lo slider dopo aver ricevuto la risposta
            st.components.v1.html("""
            <script type="text/javascript">
                stopSlider();  // Chiama la funzione per fermare lo slider
            </script>
            """)
        with col2:
            st.write(final_result.run())
            
        
        st.write(final_result)  # Mostra il risultato della richiesta API

        
