```markdown
# CodeWriterAgent: Un agente CrewAI per la generazione di codice Python

Questo documento spiega come utilizzare l'agente CodeWriterAgent per generare codice Python in risposta a prompt.

## Cos'è CodeWriterAgent

CodeWriterAgent è un agente multi-agente che utilizza un modello linguistico di grandi dimensioni (LLM) per generare codice Python basato su prompt.

**Utilizzo**

Per utilizzare l'agente CodeWriterAgent, procedi come segue:

1. **Installa le dipendenze**

   ```
   pip install crewai llm
   ```

2. **Crea un agente**

   ```python
   from crewai import Agent, Task, Crew
   from your_module import CodeWriterAgent, create_agents  # Sostituisci 'your_module' con il nome del modulo

   
   llm1 = llm.load("gpt-3.5-turbo")
   llm2 = llm.load("gpt-3.5-turbo")
   agent = create_agents(llm1, llm2)[0]
   ```

3. **Definisci un compito**

   ```python
   task = Task(description="Scrivere codice Python per un agente basato su prompt ottimizzato", agent=agent)
   ```

4. **Avvia la Crew**

   ```python
   crew = Crew(tasks=[task])
   crew.kickoff()
   ```

**Esempio:**

```python
# Crea un agente
agent = create_agents(llm1, llm2)[0]

# Definisci un compito
task = Task(description="Scrivere funzione Python che somma due numeri", agent=agent)

# Avvia la Crew
crew = Crew(tasks=[task])
crew.kickoff()
```

**Documentazione aggiuntiva**

Per maggiori informazioni sull'architettura degli agenti CrewAI, consulta la documentazione ufficiale [https://crew-ai.io/docs/](https://crew-ai.io/docs/).

## Test

```python
import unittest
from unittest.mock import Mock
from your_module import CodeWriterAgent, create_agents

class TestCodeWriterAgent(unittest.TestCase):
    def test_code_generator_import(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "import random"
        expected_code = "import random\n"
        self.assertEqual(agent.code_generator(prompt), expected_code)
    # ... altri test ...

if __name__ == "__main__":
    unittest.main()
```


```