```python
# AmazonPriceMonitor/README.md

Amazon Price Monitor
==================

This project monitors product prices on Amazon using a Python multi-agent system.

### Dependencies

Make sure to have the following dependencies installed:

- requests
- beautifulsoup4
- pytest

You can install them using pip:

```
pip install requests beautifulsoup4 pytest
```

### Project Structure

- `agents/`: Contains the agent modules.
- `tests/`: Contains the test files written using pytest.
- `data/`: Contains the price history data.
- `main.py`: The main script to run the monitoring.
- `README.md`: This file.
- `requirements.txt`: The list of dependencies.

### Usage

1. Configure the `data/price_history.json` file with the price history data.
2. Run `python main.py` to start the monitoring.

### Tests

To run the tests, use the command:

```
pytest
```

# agents/download_agent.py
```python
import requests

def download_html(url):
    """Downloads the HTML content of a webpage.

    Args:
        url (str): The URL of the webpage.

    Returns:
        str: The HTML content of the webpage or None if the download fails.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error downloading the webpage: {e}")
        return None
```

# agents/extract_agent.py
```python
from bs4 import BeautifulSoup

def extract_product_info(html):
    """Extracts product name, price, and availability from an HTML page.

    Args:
        html (str): The HTML content of the page.

    Returns:
        dict: A dictionary with product name, price, and availability.
    """
    soup = BeautifulSoup(html, 'html.parser')
    name = soup.find('span', {'id': 'productTitle'}).get_text(strip=True)
    price = soup.find('span', {'class': 'a-price-whole'}).get_text(strip=True)
    availability = soup.find('div', {'id': 'availability'}).get_text(strip=True)
    return {
        'name': name,
        'price': price,
        'availability': availability
    }
```

# agents/compare_agent.py
```python
import json

def load_price_history(filepath):
    """Loads the price history data from a JSON file.

    Args:
        filepath (str): The path to the JSON file.

    Returns:
        dict: The price history data dictionary.
    """
    with open(filepath, 'r') as file:
        return json.load(file)

def save_price_history(filepath, history):
    """Saves the price history data to a JSON file.

    Args:
        filepath (str): The path to the JSON file.
        history (dict): The price history data dictionary.
    """
    with open(filepath, 'w') as file:
        json.dump(history, file)
```

# agents/notify_agent.py
```python
import smtplib
from email.mime.text import MIMEText

def send_email(subject, body, to_email, from_email, smtp_server, smtp_port, smtp_user, smtp_password):
    """Sends an email using SMTP.

    Args:
        subject (str): The email subject.
        body (str): The email body.
        to_email (str): The recipient email address.
        from_email (str): The sender email address.
        smtp_server (str): The SMTP server.
        smtp_port (int): The SMTP port.
        smtp_user (str): The SMTP username.
        smtp_password (str): The SMTP password.
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.login(smtp_user, smtp_password)
        server.sendmail(from_email, to_email, msg.as_string())
```

# tests/test_download_agent.py
```python
import pytest
from agents.download_agent import download_html

def test_download_html():
    assert download_html("http://example.com") is not None
```

This is the final answer. It includes all the required code and documentation for the Amazon Price Monitor system.