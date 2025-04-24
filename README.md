# CrewAI Multi-Agent Generator

## 🤖  CrewAI Multi-Agent Code Generator

Questo documento descrive la creazione di un'applicazione open-source multi-agent basata su CrewAI per generare codice Python completo, test unitari e documentazione tecnica.

### Descrizione del progetto

Questo progetto dimostra l'utilizzo di CrewAI per automatizzare l'elaborazione di richieste complesse e generare automaticamente un agente completo, composto da:

* **Prompt Writer**: Ottimizza le richieste per ottenere risposte accurati dagli agenti di CrewAI.
* **Code Writer**: Scrive codice Python funzionante basato sul prompt ottimizzato.
* **Code Tester**: Crea test unitari per il codice generato.
* **Doc Writer**: Genera la documentazione in formato markdown per il codice e i test.

## Utilizzo

La creazioni di un nuovo agente multi-agent completa

1. La richiesta viene immessa tramite un'interfaccia utente.

2. L'agente Prompt Writer ottimizza la richiesta per ottenere il miglior output da un modello linguistico di grandi dimensioni (LLM) come Groq.

3. L'agente Code Writer utilizza il prompt ottimizzato per generare codice Python funzionante.

4. L'agente Code Tester crea test unitari per assicurarsi che il codice funzioni correttamente.

5. L'agente Doc Writer genera la documentazione tecnica in markdown per il codice e i test unitari.

6. Il codice, i test e la documentazione vengono raccolti in un pacchetto ZIP che può essere scaricato dall'utente.



## Applicazioni

Questo progetto può essere utile per:

* **Sviluppatori** che desiderano automatizzare la generazione di codice Python basato su richieste testuali.
* **Dataset generation**: Creare codice Python per specifiche attività e generatori di dataset.
* **Esempio**: Automazione di task ricorrenti.



## Contribuire

Questo progetto è open-source e i contributi sono benvenuti. Per contribuire, fork di questo repository e invia una pull request.