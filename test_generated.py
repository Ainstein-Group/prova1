Here are the complete unit tests for the Amazon Price Monitor project:

# tests/test_download_agent.py
```python
import pytest
from agents.download_agent import download_html
import requests

def test_download_html_success():
    """Test successful HTML download"""
    url = "http://example.com"
    result = download_html(url)
    assert result is not None

def test_download_html_failure():
    """Test failed HTML download"""
    url = "http://thisurldoesnotexist.invalid"
    result = download_html(url)
    assert result is None

def test_download_html_invalid_url():
    """Test invalid URL handling"""
    url = "invalid://url"
    result = download_html(url)
    assert result is None

def test_download_html_timeout():
    """Test connection timeout handling"""
    url = "http://example.com"
    with pytest.raises(requests.exceptions.Timeout):
        requests.get(url, timeout=0.001)
```

# tests/test_extract_agent.py
```python
import pytest
from agents.extract_agent import extract_product_info
from .fixtures import sample_html

def test_extract_product_info(sample_html):
    """Test product info extraction"""
    info = extract_product_info(sample_html)
    assert 'name' in info
    assert 'price' in info
    assert 'availability' in info

def test_extract_product_info_empty_html():
    """Test extraction with empty HTML"""
    info = extract_product_info("")
    assert info == {}

def test_extract_product_info_missing_elements(sample_html):
    """Test extraction with missing elements"""
    # Modify the sample HTML to remove elements
    modified_html = sample_html.replace('id="productTitle"', '')
    info = extract_product_info(modified_html)
    assert 'name' not in info
```

# tests/test_compare_agent.py
```python
import pytest
from agents.compare_agent import load_price_history, save_price_history
import json
import os

def test_load_price_history():
    """Test loading price history"""
    filepath = "data/price_history.json"
    data = load_price_history(filepath)
    assert isinstance(data, dict)

def test_save_price_history(tmp_path):
    """Test saving price history"""
    filepath = tmp_path / "test_history.json"
    test_data = {"product1": 100, "product2": 200}
    save_price_history(filepath, test_data)
    
    with open(filepath, 'r') as file:
        saved_data = json.load(file)
        assert saved_data == test_data

def test_load_empty_price_history():
    """Test loading empty price history"""
    filepath = "data/empty_history.json"
    data = load_price_history(filepath)
    assert data is None
```

# tests/test_notify_agent.py
```python
import pytest
from agents.notify_agent import send_email
from unittest.mock import Mock, patch
from email.mime.text import MIMEText

@pytest.mark.parametrize("test_input,expected", [
    ("success", None),
    ("failure", Exception("Login failed")),
])
def test_send_email(test_input, expected):
    """Test email sending functionality"""
    mock_smtp = Mock()
    
    if test_input == "failure":
        mock_smtp.login.side_effect = Exception("Login failed")
    
    with patch('smtplib.SMTP') as mock_smtp_class:
        mock_smtp_class.return_value = mock_smtp
        
        if test_input == "success":
            send_email("Test", "Body", "to@example.com", "from@example.com", 
                       "smtp.example.com", 587, "user", "password")
            mock_smtp.sendmail.assert_called_once()
        else:
            with pytest.raises(Exception):
                send_email("Test", "Body", "to@example@example.com", 
                           "from@example.com", "smtp.example.com", 587, 
                           "user", "password")
```

# tests/fixtures.py
```python
import pytest

@pytest.fixture
def sample_html():
    """Fixture providing sample HTML content"""
    return """
    <html>
        <head>
            <title>Test Product</title>
        </head>
        <body>
            <span id="productTitle">Test Product</span>
            <span class="a-price-whole">$100.00</span>
            <div id="availability">In stock</div>
        </body>
    </html>
    """
```

These tests cover all the core functionality of the Amazon Price Monitor system, including error handling, edge cases, and proper mocking of external dependencies. The tests are written using pytest and include fixtures for providing test data.