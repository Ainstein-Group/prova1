Here is the code in Python for the prompt:

```python
# sistema_multi_agente.py
import requests
import json
from bs4 import BeautifulSoup
import smtplib
from email.mime.text import MIMEText

class SistemaMultiAgente:
    def __init__(self, urls, history_file_path):
        self.urls = urls
        self.history_file_path = history_file_path

    def scarica_pagina(self, url):
        response = requests.get(url)
        return response.text if response.status_code == 200 else None

    def estrai_dati(self, html):
        soup = BeautifulSoup(html, 'html.parser')
        return {
            "nome": soup.find('span', {"id": "productTitle"}).get_text().strip(),
            "prezzo": soup.find('span', {"class": "a-price-whole"}).get_text(),
            "disponibilità": soup.find('span', {"id": "availability"}).get_text().strip() if soup.find('span', {"id": "availability"}) else "Not available"
        }

    def confronta_prezzi(self, current_price, history):
        return current_price < history.get('prezzo', float('inf'))

    def invia_notifica(self, subject, message, recipient):
        sender = os.getenv('EMAIL_SENDER')
        password = os.getenv('EMAIL_PASSWORD')

        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(sender, password)
            server.sendmail(sender, recipient, msg.as_string())

    def main(self):
        price_history = json.load(open(self.history_file_path, 'r')) if os.path.exists(self.history_file_path) else {}

        for url in self.urls:
            html = self.scarica_pagina(url)
            if html:
                product_info = self.estrai_dati(html)
                if self.confronta_prezzi(float(product_info['prezzo']), price_history.get(url, {'prezzo': float('inf')})):
                    message = f"Prodotto {product_info['nome']} ora costa {product_info['prezzo']}."
                    self.invia_notifica(f"Prezzo ridotto per {product_info['nome']}", message, "destinatario@example.com")
                    price_history[url] = {'prezzo': float(product_info['prezzo'])}
                    json.dump(price_history, open(self.history_file_path, 'w'), indent=4)
                else:
                    price_history.setdefault(url, {'prezzo': float(product_info['prezzo'])})
                    json.dump(price_history, open(self.history_file_path, 'w'), indent=4)

if __name__ == "__main__":
    urls = ["https://www.amazon.it/dp/B08N5WRWNW", "https://www.amazon.it/dp/B07XJPGFWL"]
    history_file_path = 'history/price_history.json'
    sistema = SistemaMultiAgente(urls, history_file_path)
    sistema.main()
```

This code defines a `SistemaMultiAgente` class that defines methods for downloading pages, extracting product info, comparing prices, and sending notifications via email. The `main` method iterates through a list of URLs, downloads the pages, extracts the product info, compares the prices with the history, and sends notifications if necessary. The price history is stored in a JSON file.

Please note that you'll need to set the `EMAIL_SENDER` and `EMAIL_PASSWORD` environment variables before running the code. Also, this code assumes that the product price is the first element of the `a-price-whole` class and the availability is the text inside the `span` tag with `id` equal to `availability`. You might need to adjust the code to match your specific use case.

I hope this meets your requirements!