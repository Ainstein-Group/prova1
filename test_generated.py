Ecco una suite di test unitari completa per il codice fornito, utilizzando il framework `unittest` e il mocking per isolare le dipendenze:

```python
import unittest
from unittest.mock import patch, MagicMock
from sistema_multi_agente import SistemaMultiAgente
import requests
from bs4 import BeautifulSoup
import json
import os
import smtplib
from email.mime.text import MIMEText

class TestSistemaMultiAgente(unittest.TestCase):

    def setUp(self):
        self.urls = ["http://test.com/page1", "http://test.com/page2"]
        self.history_file_path = "test_history.json"
        self.system = SistemaMultiAgente(self.urls, self.history_file_path)
        
    def test_scarica_pagina(self):
        # Test case when the request is successful
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 200
            mock_response.text = "<html>Test HTML</html>"
            mock_get.return_value = mock_response
            
            result = self.system.scarica_pagina("http://test.com")
            self.assertEqual(result, "<html>Test HTML</html>")
            
        # Test case when the request fails
        with patch('requests.get') as mock_get:
            mock_response = MagicMock()
            mock_response.status_code = 404
            mock_get.return_value = mock_response
            
            result = self.system.scarica_pagina("http://test.com")
            self.assertIsNone(result)
    
    def test_estrai_dati(self):
        html = """
        <html>
            <span id="productTitle">Test Product</span>
            <span class="a-price-whole">39.90</span>
            <span id="availability">Disponibile</span>
        </html>
        """
        
        expected_data = {
            "nome": "Test Product",
            "prezzo": "39.90",
            "disponibilità": "Disponibile"
        }
        
        result = self.system.estrai_dati(html)
        self.assertDictEqual(result, expected_data)
        
        # Test case when availability is not found
        html_without_availability = """
        <html>
            <span id="productTitle">Test Product</span>
            <span class="a-price-whole">39.90</span>
        </html>
        """
        
        result = self.system.estrai_dati(html_without_availability)
        self.assertEqual(result["disponibilità"], "Not available")
    
    def test_confronta_prezzi(self):
        # Test case when current price is lower
        current_price = 39.90
        history = {"prezzo": 40.00}
        self.assertTrue(self.system.confronta_prezzi(current_price, history))
        
        # Test case when current price is higher
        current_price = 40.50
        history = {"prezzo": 40.00}
        self.assertFalse(self.system.confronta_prezzi(current_price, history))
        
        # Test case when history is empty
        current_price = 39.90
        history = {}
        self.assertTrue(self.system.confronta_prezzi(current_price, history))
    
    @patch('smtplib.SMTP_SSL')
    @patch('os.getenv')
    def test_invia_notifica(self, mock_getenv, mock_smtp):
        # Setup mock environment variables
        mock_sender = "test@example.com"
        mock_password = "test_password"
        mock_getenv.side_effect = [mock_sender, mock_password]
        
        # Setup email message
        subject = "Test Subject"
        message = "Test Message"
        recipient = "recipient@example.com"
        
        # Call the method
        self.system.invia_notifica(subject, message, recipient)
        
        # Verify that the message was constructed correctly
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = mock_sender
        msg['To'] = recipient
        
        # Verify that the SMTP server was used correctly
        mock_smtp.return_value.__enter__.return_value.login.assert_called_once_with(mock_sender, mock_password)
        mock_smtp.return_value.__enter__.return_value.sendmail.assert_called_once_with(mock_sender, recipient, msg.as_string())
    
    @patch('json.load')
    @patch('json.dump')
    @patch('os.path.exists')
    @patch('sistema_multi_agente.SistemaMultiAgente.scarica_pagina')
    @patch('sistema_multi_agente.SistemaMultiAgente.estrai_dati')
    def test_main(self, mock_estrai_dati, mock_scarica_pagina, mock_os_path_exists, mock_json_dump, mock_json_load):
        # Setup mock file operations
        mock_os_path_exists.return_value = False
        
        # Setup mock JSON load to return empty history
        mock_json_load.return_value = {}
        
        # Setup mock scarica_pagina to return HTML
        mock_scarica_pagina.return_value = "<html><span id='productTitle'>Test Product</span><span class='a-price-whole'>39.90</span></html>"
        
        # Setup mock estrai_dati to return test data
        mock_estrai_dati.return_value = {
            "nome": "Test Product",
            "prezzo": "39.90",
            "disponibilità": "Not available"
        }
        
        # Call main method
        self.system.main()
        
        # Verify that the history file was updated
        mock_json_dump.call_args_list[0][0][0][0].sort()
        expected_history = {self.urls[0]: {'prezzo': 39.90}}
        self.assertEqual(mock_json_dump.call_args_list[0][0][0][0], expected_history)
        
if __name__ == "__main__":
    unittest.main()
```

Questi test coprono tutte le principali funzionalità del codice, inclusa:
- Verifica del download della pagina
- Estrazione dei dati dalla pagina HTML
- Confronto dei prezzi
- Invio di notifiche via email
- Logica principale del sistema

I test utilizzano mocking per isolare le dipendenze esterne come richieste HTTP, operazioni file system e invio email, assicurando che i test siano eseguiti rapidamente e in modo affidabile.

Per eseguire i test, salva il codice in un file chiamato `test_sistema_multi_agente.py` e esegui il comando:

```bash
python -m unittest test_sistema_multi_agente.py -v
```