```markdown
# Price Tracker

## Descrizione

Questo progetto fornisce un agente di download, un agente di estrazione, un agente di confronto e un agente di notifica per monitorare i prezzi dei prodotti in diversi siti web.

## Setup

1. **Ambiente virtuale:**
   - Crea un ambiente virtuale: `python -m venv venv`
   - Attiva l'ambiente: `source venv/bin/activate`
   - Installa le dipendenze: `pip install -r requirements.txt`

2. **Configurazione:**
   - Modifica il file `price_history.json` con le informazioni sui prodotti da monitorare e i loro prezzi iniziali.

   ```json
   {
     "prodotto1": {"prezzo": 100, "data": "2023-10-01"},
     "prodotto2": {"prezzo": 200, "data": "2023-10-01"}
   }
   ```

   - Inserisci le informazioni di configurazione per le notifiche nel file `main.py`: `sender_email`, `receiver_email`, `smtp_server` e `smtp_port`.

3. **Dati sulle pagine:**
   -  Nell'elenco `urls` nella funzione `main()` definisci gli URL dei prodotti da monitorare.


## Funzionamento

Il programma funziona secondo questi passaggi:

1. **Download delle pagine HTML:** Utilizza l'agente di download per scaricare le pagine HTML dei prodotti desiderati.
2. **Estrazione delle informazioni dei prodotti:** Utilizza l'agente di estrazione per estrarre le informazioni pertinenti dai prodotti dalle pagine HTML scaricate (ad esempio, nome prodotto, prezzo).
3. **Confronto dei prezzi:** Confronta i prezzi estratti con quelli archiviati in `price_history.json`.
4. **Invio delle notifiche:** Invia notifiche via email agli utenti registrati se un prodotto raggiunge un prezzo inferiore a quello stabilito o si verificano altri eventi specificati (ad esempio, offerta speciale).

## Utilizzo

1. Esegui il codice utilizzando il comando `python main.py`.
2. Il programma scarica le pagine HTML, estrae le informazioni dei prodotti, confronta i prezzi e invia notifiche se necessario.

## Estensioni future

- Aggiungere la capacità di monitorare più parametri dei prodotti (ad esempio, disponibilità).
- Implementazione di notifiche su diverse piattaforme (ad esempio, SMS, webhook).
- Incorpore la capacità di importare listini prezzi automatici.




```