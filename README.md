# SISTEMA MULTI-AGENT PER IL MONITORAGGIO DEI PREZZI SU AMAZON

Questo sistema è composto da quattro agenti separati che lavorano insieme per monitorare i prezzi di vari prodotti su Amazon. Ogni agente è modulare e può essere testato separatamente. Il sistema è documentato in modo che sia facile da utilizzare e integrare.

## Struttura del Progetto

```
amazon_price_monitor/
│
├── agents/
│   ├── downloader.py
│   ├── extractor.py
│   ├── price_comparator.py
│   └── notification_agent.py
│
├── tests/
│   ├── test_downloader.py
│   ├── test_extractor.py
│   ├── test_price_comparator.py
│   └── test_notification_agent.py
│
├── data/
│   └── price_history.json
│
├── README.md
├── requirements.txt
└── main.py
```

## Requisiti

- Python 3.7+
- BeautifulSoup
- Requests
- PyTest
- Smtplib (per inviare email)

## Installazione

1. Clona il repository:
    ```bash
    git clone https://github.com/yourusername/amazon_price_monitor.git
    cd amazon_price_monitor
    ```
2. Installa le dipendenze:
    ```bash
    pip install -r requirements.txt
    ```

## Documentazione

### Downloader

```python
import requests
def download_page(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text
```

Questo modulo scarica il contenuto HTML di una pagina web fornita dall'URL. 

### Extractor

```python
from bs4 import BeautifulSoup
def extract_info(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    name = soup.find('span', id='productTitle').get_text(strip=True)
    price = soup.find('span', class_='a-price-whole').get_text(strip=True)
    availability = soup.find('span', class_='a-available').get_text(strip=True)
    return {'name': name, 'price': price, 'availability': availability}
```

Questo modulo estrae le informazioni essenziali di un prodotto da un contenuto HTML, come nome, prezzo e disponibilità. 

### Price Comparator

```python
import json
def compare_prices(current_price, history_file):
    with open(history_file, 'r') as f:
        history = json.load(f)
    current_price_float = float(current_price.replace(',', ''))
    if 'prices' not in history:
        return False
    last_price = history['prices'][-1]
    return current_price_float < last_price
```

Questo modulo confronta il prezzo corrente di un prodotto con il prezzo storico, analizzando un file JSON con le informazioni precedenti.

### Notification Agent

```python
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(subject, body, to_email):
    from_email = "tuoindirizzoemail@example.com"
    from_password = "tuapass"
    msg = MIMEMultipart()
    msg['From'] = from_email
    msg['To'] = to_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, from_password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
```

Questo modulo invia un'e-mail di notifica quando il prezzo di un prodotto scende al di sotto di una soglia definita.

### Main

```python
from downloader import download_page
from extractor import extract_info
from price_comparator import compare_prices
from notification_agent import send_email
def monitor_products(urls, history_file, to_email):
    for url in urls:
        html_content = download_page(url)
        product_info = extract_info(html_content)
        current_price = product_info['price']
        if compare_prices(current_price, history_file):
            subject = f"Prezzo diminuito per {product_info['name']}"
            body = f"Il prezzo del prodotto {product_info['name']} è sceso a {current_price}."
            send_email(subject, body, to_email)
if __name__ == "__main__":
    product_urls = ['URL1', 'URL2', 'URL3']
    history_file = 'data/price_history.json'
    to_email = 'destinatario@example.com'
    monitor_products(product_urls, history_file, to_email)
```

La funzione principale del sistema, il modulo `main.py`, esegue il monitoraggio dei prezzi per un elenco di prodotti specificati, confrontando i prezzi attuali con quelli storici e inviando una notifica via e-mail quando viene rilevata una riduzione.

## Testing

Ogni agente è testabile separatamente usando `pytest`. Esegui i test con il seguente comando:

```bash
pytest
```

## Note

- Assicurati di configurare le credenziali SMTP corrette per inviare email.
- Questo è un esempio di base e potrebbe richiedere ulteriori configurazioni per gestire i requisiti aggiuntivi di scraping e gestione degli errori.