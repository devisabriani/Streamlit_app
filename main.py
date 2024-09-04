import streamlit as st
from textwrap import dedent

def create_agents(topic, grade):
    teacher = {
        'role': 'Insegnante',
        'goal': 'Pianificare una lezione efficace e coinvolgente',
        'backstory': dedent(f"""
            Sei un insegnante esperto con anni di esperienza nell'insegnamento a studenti di {grade}.
            Il tuo obiettivo è creare lezioni coinvolgenti e informative su {topic}.
        """)
    }
    
    curriculum_expert = {
        'role': 'Esperto di Curriculum',
        'goal': 'Assicurare che la lezione sia allineata con gli standard educativi',
        'backstory': dedent(f"""
            Sei un esperto di curriculum con una profonda conoscenza degli standard educativi per studenti di {grade}.
            Il tuo compito è garantire che la lezione su {topic} soddisfi tutti i requisiti curriculari necessari.
        """)
    }
    
    creative_consultant = {
        'role': 'Consulente Creativo',
        'goal': 'Suggerire attività e approcci innovativi per la lezione',
        'backstory': dedent(f"""
            Sei un consulente creativo specializzato in metodi di insegnamento innovativi.
            Il tuo obiettivo è proporre idee uniche e coinvolgenti per insegnare {topic} a studenti di {grade}.
        """)
    }
    
    return [teacher, curriculum_expert, creative_consultant]

def create_tasks(topic, grade):
    task1 = {
        'description': f"Sviluppa una struttura di base per una lezione su {topic} per studenti di {grade}",
        'agent': 0
    }
    
    task2 = {
        'description': f"Verifica che la struttura della lezione su {topic} sia conforme agli standard curricolari per {grade}",
        'agent': 1
    }
    
    task3 = {
        'description': f"Proponi attività creative e coinvolgenti per insegnare {topic} a studenti di {grade}",
        'agent': 2
    }
    
    task4 = {
        'description': "Integra il feedback e finalizza il piano di lezione",
        'agent': 0
    }
    
    return [task1, task2, task3, task4]

def main():
    st.title("Pianificatore di Lezioni con CrewAI")

    topic = st.text_input("Inserisci l'argomento della lezione:")
    grade = st.selectbox("Seleziona la classe:", ["Elementari", "Medie", "Superiori"])

    if st.button("Pianifica Lezione"):
        if topic and grade:
            with st.spinner("Pianificazione in corso..."):
                agents = create_agents(topic, grade)
                tasks = create_tasks(topic, grade)
                
                result = dedent(f"""
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
                st.write(result)
        else:
            st.warning("Per favore, inserisci sia l'argomento che la classe.")

if __name__ == "__main__":
    main()
