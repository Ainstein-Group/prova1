```markdown
## Sistema Multi-Agente per il Monitoraggio dei Prezzi

Questo è un semplice sistema multi-agente scritto in Python per monitorare i prezzi di prodotti su siti web e inviare notifiche via email quando i prezzi scendono.

### Come funziona

Il sistema funziona in modo ciclico:

1. **Scarica le pagine web:** Per ogni URL specificato, il sistema scarica la pagina web utilizzando la libreria `requests`.
2. **Estrae i dati:** Dal contenuto HTML scaricato, il sistema estrae informazioni sul prodotto, come il nome, il prezzo e la disponibilità, utilizzando la libreria `BeautifulSoup`.
3. **Confronta i prezzi:** Il sistema confronta il prezzo corrente con un record storico dei prezzi per lo stesso prodotto. 
4. **Invia notifiche:** Se il prezzo corrente è inferiore al prezzo storico, il sistema invia un'email di avviso al destinatario specificato.

### Requisiti

* Python 3.6+ 
* Librerie Python: requests, beautifulsoup4, smtplib, email.mime.text

### Installazione

1.  Scatena l'installazione delle dipendenza:
    ``` bash
    pip install requests beautifulsoup4
    ```

### Usi del codice

1.  Modificare il file `system_multi_agente.py` con i propri URL dei prodotti e l'indirizzo email del destinatario.
2.  Modificare il file `system_multi_agente.py` con il path al file di storage delle informazioni storiche dei prezzi.

3.  Eseguire il script:

    ```bash
    python system_multi_agente.py
    ```

### Esempio

Nel file `system_multi_agente.py`,  questo è un esempio di come usare il codice:

```python
urls = ["https://www.amazon.it/dp/B08N5WRWNW", "https://www.amazon.it/dp/B07XJPGFWL"]  
history_file_path = 'history/price_history.json'
sistema = SistemaMultiAgente(urls, history_file_path)
sistema.main() 
### 

### Note

 * Le email vengono inviate utilizzando la configurazione di Gmail. È necessario abilitare l'accesso "Semplice" per il tuo account Gmail nelle impostazioni di sicurezza. 


 * Questo è un esempio di base. Puoi estenderlo con funzionalità aggiuntive, come il supporto per più siti web o la memorizzazione dei prezzi in un database.

*   È necessario impostare le variabili d'ambiente `EMAIL_SENDER` e `EMAIL_PASSWORD` per inviare le email. 



Contattaci per qualsiasi domanda o feedback.