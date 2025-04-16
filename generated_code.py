```python
# Serie di moduli per l'agente di download
from agents.download_agent import download_pages

# Serie di moduli per l'agente di estrazione
from agents.extraction_agent import extract_product_info

# Serie di moduli per l'agente di confronto
from agents.comparison_agent import compare_prices

# Serie di moduli per l'agente di notifica
from agents.notification_agent import send_notification

# Configurazione delle dipendenze
import requests
from bs4 import BeautifulSoup
import json
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import pytest

# Creazione di un ambiente virtuale
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt

# Configurazione del file price_history.json
price_history = {
    "prodotto1": {"prezzo": 100, "data": "2023-10-01"},
    "prodotto2": {"prezzo": 200, "data": "2023-10-01"}
}

# Configurazione delle notifiche
sender_email = "your_email@example.com"
receiver_email = "receiver_email@example.com"
smtp_server = "smtp.example.com"
smtp_port = 587

# Funzione principale
def main():
    # Download delle pagine HTML
    urls = ["url_prodotto1", "url_prodotto2"]
    html_pages = download_pages(urls)

    # Estrazione delle informazioni dei prodotti
    product_info = extract_product_info(html_pages)

    # Confronto dei prezzi e invio delle notifiche
    decreased_prices = compare_prices(product_info, "data/price_history.json")
    send_notification(decreased_prices)

# Esecuzione della funzione principale
if __name__ == "__main__":
    main()
```