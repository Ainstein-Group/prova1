```python
from crewai import Agent, Task, Crew
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)

class CrewAI-Agent:
    def __init__(self, role, goal, backstory, llm):
        self.role = role
        self.goal = goal
        self.backstory = backstory
        self.llm = llm

    def respond(self, input_text: str) -> str:
        try:
            response = self.llm.generate(input_text, max_length=200)
            return response[0]['generated_text']
        except Exception as e:
            logging.error(f"Error generating response: {e}")
            return "Mi dispiace, non sono in grado di rispondere alla tua domanda."

class CrewAI-Task:
    def __init__(self, description, agent):
        self.description = description
        self.agent = agent

class CrewAI-Crew:
    def __init__(self, agents, tasks):
        self.agents = agents
        self.tasks = tasks

    def kickoff(self):
        for task in self.tasks:
            agent = task.agent
            input_text = input("Utente: ")
            response = agent.respond(input_text)
            print(f"Agente: {response}")

def create_agents(llms1, llms2):
    agent1 = CrewAI-Agent(role="Code Writer", goal="Scrivere codice Python per agenti CrewAI", backstory="Esperto di multi-agente.", llm=llms1)
    agent2 = CrewAI-Agent(role="Code Writer", goal="Scrivere codice Python per agenti CrewAI", backstory="Esperto di multi-agente.", llm=llms2)
    return [agent1, agent2]

llms1 = pipeline("text-generation", model="t5-small")
llms2 = pipeline("text-generation", model="t5-small")

agents = create_agents(llms1, llms2)
task = CrewAI-Task(description="Scrivere codice Python per un agente basato su prompt ottimizzato", agent=agents[0])
crew = CrewAI-Crew(agents=agents, tasks=[task])
crew.kickoff()
```