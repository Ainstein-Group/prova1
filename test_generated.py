Ecco i test unitari per ciascun modulo del progetto. Ogni test è scritto utilizzando pytest e include diverse case di test per assicurare la copertura totale della funzionalità.

### Test per il Downloader

```python
# tests/test_downloader.py
import pytest
from unittest.mock import patch
from downloader import download_page
import requests

@pytest.fixture
def mock_response():
    return "<html>Mock HTML Response</html>"

def test_download_page_valid_url(mock_response):
    with patch('requests.get', return_value=mock_response) as mock_get:
        result = download_page("http://example.com")
        assert mock_get.called_once
        assert result == mock_response

def test_download_page_invalid_url():
    with pytest.raises(requests.exceptions.RequestException):
        download_page("http://invalid.url")

def test_download_page_connection_error():
    with patch('requests.get', side_effect=requests.exceptions.ConnectionError()):
        with pytest.raises(requests.exceptions.RequestException):
            download_page("http://example.com")
```

### Test per l'Extractor

```python
# tests/test_extractor.py
from extractor import extract_info
from bs4 import BeautifulSoup
import pytest

@pytest.fixture
def mock_html():
    return """
    <html>
        <span id="productTitle">Test Product</span>
        <span class="a-price-whole">39,99</span>
        <span class="a-available">Disponibile</span>
    </html>
    """

def test_extract_info_valid_html(mock_html):
    result = extract_info(mock_html)
    assert result['name'] == 'Test Product'
    assert result['price'] == '39,99'
    assert result['availability'] == 'Disponibile'

def test_extract_info_missing_name(mock_html):
    soup = BeautifulSoup(mock_html, 'html.parser')
    soup.find('span', id='productTitle').extract()
    result = extract_info(str(soup))
    assert result['name'] == ''

def test_extract_info_missing_price(mock_html):
    soup = BeautifulSoup(mock_html, 'html.parser')
    soup.find('span', class_='a-price-whole').extract()
    result = extract_info(str(soup))
    assert result['price'] == ''
```

### Test per il Price Comparator

```python
# tests/test_price_comparator.py
import json
import tempfile
from price_comparator import compare_prices
import pytest

@pytest.fixture
def temp_history_file():
    with tempfile.NamedTemporaryFile(mode='w', delete=False) as f:
        json.dump({'prices': [40.0, 39.0]}, f)
        f.close()
        yield f.name
    import os
    os.unlink(f.name)

def test_compare_prices_lower_price(temp_history_file):
    assert compare_prices('39,99', temp_history_file) == True

def test_compare_prices_higher_price(temp_history_file):
    assert compare_prices('40,99', temp_history_file) == False

def test_compare_prices_empty_history():
    with tempfile.NamedTemporaryFile(mode='w') as f:
        json.dump({}, f)
        f.close()
        result = compare_prices('39,99', f.name)
        assert result == False
```

### Test per il Notification Agent

```python
# tests/test_notification_agent.py
from notification_agent import send_email
import pytest
from unittest.mock import patch, MagicMock

@pytest.fixture
def mock_smtp():
    with patch('smtplib.SMTP') as mock_smtp_class:
        yield mock_smtp_class

def test_send_email_valid_input(mock_smtp):
    mock_server = MagicMock()
    mock_smtp.return_value = mock_server
    send_email('Test Subject', 'Test Body', 'test@example.com')
    mock_server.sendmail.assert_called_once()

def test_send_email_empty_subject():
    with patch('smtplib.SMTP') as mock_smtp_class:
        send_email('', 'Test Body', 'test@example.com')
        mock_smtp_class.return_value.sendmail.assert_called_once()

def test_send_email_invalid_email():
    with patch('smtplib.SMTP') as mock_smtp_class:
        mock_server = MagicMock()
        mock_smtp.return_value = mock_server
        mock_server.sendmail.side_effect = Exception('Invalid email')
        with pytest.raises(Exception):
            send_email('Test Subject', 'Test Body', 'invalid-email')
```

### Test per il Main

```python
# tests/test_main.py
from main import monitor_products
from unittest.mock import patch, MagicMock
import pytest

@pytest.fixture
def mock_downloader():
    with patch('main.download_page', return_value='<html></html>') as mock_downloader:
        yield mock_downloader

@pytest.fixture
def mock_extractor():
    with patch('main.extract_info', return_value={'name': 'Test Product', 'price': '39,99'}) as mock_extractor:
        yield mock_extractor

@pytest.fixture
def mock_price_comparator():
    with patch('main.compare_prices', return_value=True) as mock_price_comparator:
        yield mock_price_comparator

@pytest.fixture
def mock_notification_agent():
    with patch('main.send_email') as mock_notification_agent:
        yield mock_notification_agent

def test_monitor_products(mock_downloader, mock_extractor, mock_price_comparator, mock_notification_agent):
    urls = ['http://example.com']
    history_file = 'test.json'
    to_email = 'test@example.com'
    monitor_products(urls, history_file, to_email)
    mock_downloader.assert_called_once()
    mock_extractor.assert_called_once()
    mock_price_comparator.assert_called_once()
    mock_notification_agent.assert_called_once()

def test_monitor_products_empty_urls():
    urls = []
    history_file = 'test.json'
    to_email = 'test@example.com'
    monitor_products(urls, history_file, to_email)
    # Verifica che non vengono chiamate le funzioni
```

Per eseguire tutti i test, posizionati nella cartella principale del progetto e esegui:

```bash
pytest tests/
```

Questi test coprono tutte le funzionalità principali del sistema, inclusi i casi di successo e fallimento. È possibile estendere i test aggiungendo altre case di test in base alle specifiche esigenze.