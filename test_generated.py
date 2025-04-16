```python
# Test per il codice principale
import pytest
from unittest.mock import patch, MagicMock
from your_main_module import main  # Sostituire con il nome del modulo principale

class TestMain:
    @patch('your_main_module.download_pages')  # Sostituire con il percorso corretto
    @patch('your_main_module.extract_product_info')
    @patch('your_main_module.compare_prices')
    @patch('your_main_module.send_notification')
    def test_main_funziona_correttamente(self, mock_send_notification, mock_compare_prices, mock_extract_product_info, mock_download_pages):
        # Configurazione dei mock
        mock_download_pages.return_value = ["html1", "html2"]
        mock_extract_product_info.return_value = [{"prodotto": "prodotto1", "prezzo": 100}, {"prodotto": "prodotto2", "prezzo": 200}]
        mock_compare_prices.return_value = [{"prodotto": "prodotto1", "prezzo": 90}]
        mock_send_notification.return_value = None

        # Esecuzione della funzione principale
        result = main()

        # Verifica che la funzione non abbia restituito nulla (None)
        assert result is None

        # Verifica che le funzioni siano state chiamate
        mock_download_pages.assert_called_once()
        mock_extract_product_info.assert_called_once()
        mock_compare_prices.assert_called_once()
        mock_send_notification.assert_called_once()

    @patch('your_main_module.download_pages')
    def test_download_pages_ritorna_html(self, mock_download_pages):
        # Configurazione del mock
        mock_download_pages.return_value = ["<html>pagina1</html>", "<html>pagina2</html>"]

        # Esecuzione della funzione principale
        html_pages = download_pages(["url1", "url2"])

        # Verifica che vengano restituite le pagine HTML
        assert len(html_pages) == 2
        assert html_pages[0] == "<html>pagina1</html>"
        assert html_pages[1] == "<html>pagina2</html>"

    @patch('your_main_module.extract_product_info')
    def test_extract_product_info_ritorna_info_prodotti(self, mock_extract_product_info):
        # Configurazione del mock
        mock_extract_product_info.return_value = [
            {"prodotto": "prodotto1", "prezzo": 100},
            {"prodotto": "prodotto2", "prezzo": 200}
        ]

        # Esecuzione della funzione di estrazione
        product_info = extract_product_info(["<html>pagina1</html>", "<html>pagina2</html>"])

        # Verifica che le informazioni siano state estratte correttamente
        assert len(product_info) == 2
        assert product_info[0]["prodotto"] == "prodotto1"
        assert product_info[0]["prezzo"] == 100
        assert product_info[1]["prodotto"] == "prodotto2"
        assert product_info[1]["prezzo"] == 200

    @patch('your_main_module.compare_prices')
    def test_compare_prices_confronta_prezzi(self, mock_compare_prices):
        # Configurazione del mock
        mock_compare_prices.return_value = [
            {"prodotto": "prodotto1", "prezzo": 90},
            {"prodotto": "prodotto2", "prezzo": 180}
        ]

        # Esecuzione della funzione di confronto
        decreased_prices = compare_prices(
            [{"prodotto": "prodotto1", "prezzo": 100}, {"prodotto": "prodotto2", "prezzo": 200}],
            "data/price_history.json"
        )

        # Verifica che vengano restituiti i prezzi diminuiti
        assert len(decreased_prices) == 2
        assert decreased_prices[0]["prodotto"] == "prodotto1"
        assert decreased_prices[0]["prezzo"] == 90
        assert decreased_prices[1]["prodotto"] == "prodotto2"
        assert decreased_prices[1]["prezzo"] == 180

    @patch('your_main_module.send_notification')
    def test_send_notification_invia_notifica(self, mock_send_notification):
        # Configurazione del mock
        mock_send_notification.return_value = None

        # Esecuzione della funzione di notifica
        send_notification([{"prodotto": "prodotto1", "prezzo": 90}])

        # Verifica che la notifica sia stata inviata
        mock_send_notification.assert_called_once()

    @patch('your_main_module.send_notification')
    def test_send_notification_gestisce_eccezioni(self, mock_send_notification):
        # Configurazione del mock per sollevare un'eccezione
        mock_send_notification.side_effect = smtplib.SMTPException("Errore di invio")

        # Esecuzione della funzione di notifica
        send_notification([{"prodotto": "prodotto1", "prezzo": 90}])

        # Verifica che venga gestita l'eccezione
        assert mock_send_notification.call_count == 1

if __name__ == "__main__":
    pytest.main()
```