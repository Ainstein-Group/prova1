```
from crewai import Agent, Task, Crew
import llm
import json
import random

class CodeWriterAgent(Agent):
    def __init__(self, role, goal, backstory, llm):
        super().__init__(role, goal, backstory, llm)

    def code_generator(self, prompt):
        code = ""
        prompt_parts = prompt.split(" ")
        for part in prompt_parts:
            if part.startswith("import"):
                code += f"import {part.split('(')[1].split(')')[0]}\n"
            elif part.startswith("class"):
                code += f"class {part.split(' ')[1]}:\n"
            elif part.startswith("def"):
                code += f"def {part.split(' ')[1]}:\n"
            else:
                code += part + "\n"
        return code

    def task_handler(self, task):
        prompt = task.description
        code = self.code_generator(prompt)
        return code

def create_agents(llms1, llms2):
    agent = CodeWriterAgent(role="Code Writer", goal="Scrivere codice Python per agenti CrewAI", backstory="Esperto di multi-agente.", llm=llms1)
    return agent

task = Task(description="Scrivere codice Python per un agente basato su prompt ottimizzato", agent=create_agents(llms1,llms2)[0])
crew = Crew(agents=[create_agents(llms1,llms2)[0]], tasks=[task])
crew.kickoff()
```