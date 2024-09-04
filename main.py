import streamlit as st
from textwrap import dedent

def create_agents(topic, grade, school_type, inclusion, frameworks, teaching_method):
    teacher = {
        'role': 'Insegnante',
        'goal': 'Pianificare una lezione efficace e coinvolgente',
        'backstory': dedent(f"""
            Sei un insegnante esperto con anni di esperienza nell'insegnamento a studenti di {grade} presso {school_type}.
            Il tuo obiettivo è creare lezioni coinvolgenti e informative su {topic} utilizzando il metodo di {teaching_method}.
        """)
    }
    
    curriculum_expert = {
        'role': 'Esperto di Curriculum',
        'goal': 'Assicurare che la lezione sia allineata con gli standard educativi',
        'backstory': dedent(f"""
            Sei un esperto di curriculum con una profonda conoscenza degli standard educativi per studenti di {grade}.
            Il tuo compito è garantire che la lezione su {topic} soddisfi tutti i requisiti curriculari necessari, tenendo conto delle esigenze di inclusione degli studenti {inclusion}.
        """)
    }
    
    creative_consultant = {
        'role': 'Consulente Creativo',
        'goal': 'Suggerire attività e approcci innovativi per la lezione',
        'backstory': dedent(f"""
            Sei un consulente creativo specializzato in metodi di insegnamento innovativi, con particolare attenzione all'utilizzo dei framework europei {frameworks}.
            Il tuo obiettivo è proporre idee uniche e coinvolgenti per insegnare {topic} a studenti di {grade}.
        """)
    }
    
    return [teacher, curriculum_expert, creative_consultant]

def create_tasks(topic, grade, school_type, inclusion, frameworks, teaching_method):
    task1 = {
        'description': f"Sviluppa una struttura di base per una lezione su {topic} per studenti di {grade} presso {school_type}",
        'agent': 0
    }
    
    task2 = {
        'description': f"Verifica che la struttura della lezione su {topic} sia conforme agli standard curricolari per {grade}, tenendo conto delle esigenze di inclusione degli studenti {inclusion}",
        'agent': 1
    }
    
    task3 = {
        'description': f"Proponi attività creative e coinvolgenti per insegnare {topic} a studenti di {grade}, sfruttando i framework europei {frameworks} e il metodo di {teaching_method}",
        'agent': 2
    }
    
    task4 = {
        'description': "Integra il feedback e finalizza il piano di lezione",
        'agent': 0
    }
    
    return [task1, task2, task3, task4]

def main():
    st.set_page_config(page_title="EduCrew - by Devis Abriani")
    st.title("EduCrew")
    st.markdown("*by Devis Abriani*")

    topic = st.text_input("Inserisci l'argomento della lezione:")
    
    grade = st.selectbox("Scegli il grado scolastico:", ["Secondaria di secondo grado", "Primaria", "Secondaria di primo grado"], index=0)
    
    if grade == "Secondaria di secondo grado":
        school_type = st.selectbox("Scegli il tipo di scuola secondaria:", ["Liceo scientifico", "Liceo classico"], index=0)
    else:
        school_type = grade
    
    inclusion = st.multiselect("Inclusione:", ["Classe senza DSA e DVA", "Presenza di studenti con DSA (non attivo)", "Presenza di studenti DVA (non attivo)", "Presenza di studenti con DSA e di studenti DVA (non attivo)"], default=["Classe senza DSA e DVA"])
    
    frameworks = st.multiselect("Framework europei (opzionale):", ["DigComp", "EntreComp", "LifeComp"], default=[])
    
    teaching_method = st.selectbox("Metodologia didattica:", ["Lezione frontale", "Cooperative learning", "Peer tutoring", "Learning by doing", "Inquiry Based Learning"], index=0)

    if st.button("Pianifica Lezione"):
        if topic and grade and school_type and (inclusion or frameworks or teaching_method):
            with st.spinner("Pianificazione in corso..."):
                agents = create_agents(topic, grade, school_type, inclusion, frameworks, teaching_method)
                tasks = create_tasks(topic, grade, school_type, inclusion, frameworks, teaching_method)
                
                result = dedent(f"""
                    Ecco una pianificazione per il seguente argomento:
                    
                    Agenti:
                    - {agents[0]['role']}: {agents[0]['backstory']}
                    - {agents[1]['role']}: {agents[1]['backstory']}
                    - {agents[2]['role']}: {agents[2]['backstory']}
                    
                    Compiti:
                    1. {tasks[0]['description']} (Assegnato a: {agents[tasks[0]['agent']]['role']})
                    2. {tasks[1]['description']} (Assegnato a: {agents[tasks[1]['agent']]['role']})
                    3. {tasks[2]['description']} (Assegnato a: {agents[tasks[2]['agent']]['role']})
                    4. {tasks[3]['description']} (Assegnato a: {agents[tasks[3]['agent']]['role']})
                """)
                
                st.success("Pianificazione completata!")
                st.write(result, unsafe_allow_html=True)
        else:
            st.warning("Per favore, compila tutti i campi obbligatori.")

if __name__ == "__main__":
    main()
