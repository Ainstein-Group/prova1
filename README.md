# Pipeline per l'Analisi di Documenti

Questo repository contiene un semplice pipeline per l'analisi di documenti PDF. Utilizza diversi agenti in sequenza per estrarre informazioni chiave da un documento, tra cui il testo, i token, le entità nominate e le parole chiave.

## Come funziona il pipeline

Il pipeline è costituito da diverse classi-agenti, ognuna responsabile di un compito specifico:

* **DocumentAgent**: Esegue l'estrazione del testo da un documento PDF .pdf2text e rimuove numeri decimali dal testo. 

* **PreprocessingAgent**: Impiega il modello linguistico spaCy per tokenizzare il testo e determinare la parte del discorso di ogni token.

* **NamedEntityRecognitionAgent**: Utilizza spaCy per identificare entità nominate nel testo, come persone, luoghi e organizzazioni.

* **KeywordExtractionAgent**:  Estrae le parole chiave dal testo utilizzando la frequenza di occorrenza dei token. Le parole chiave sono ordinate in modo decrescente in base alla loro frequenza.

* **CoordinatorAgent**: Gestisce la sequenza degli agenti, trasmettendo il risultato di un agente all'agente successivo.

* **ResultVisualizerAgent**: Visualizza i risultati ottenuti dai diversi agenti, stampando il testo, i token, le entità nominate e le parole chiave per ogni documento.

## Utilizzo

1. **Installazione**: Assicurarsi di avere installato le librerie necessarie: `pdf2text`, `spacy`, `networkx`, `matplotlib`.
2. **Carica il documento**: Crea una lista di percorsi dei documenti PDF da analizzare.
3. **Crea gli agenti**: Utilizza la funzione `create_agents()` per creare gli agenti necessari per il pipeline.
4. **Avvia il pipeline**: Chiama la funzione `kick_off_agents()` per eseguire il pipeline.

## Esempio

```
documents = ['document1.pdf', 'document2.pdf']
agents = create_agents(documents)
kick_off_agents(agents)
```



## Prossimi passi

* **Integrazione con grafici**: visualizzare le relazioni tra le entità nominate utilizzando grafici.
* **Impostazioni personalizzabili**: consentire all'utente di personalizzare il pipeline, ad esempio aggiungendo o rimuovendo agenti.