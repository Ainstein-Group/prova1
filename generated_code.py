amazon_price_monitor/
│
├── agents/
│   ├── fetcher_agent.py
│   ├── parser_agent.py
│   ├── price_comparer_agent.py
│   └── notification_agent.py
│
├── tests/
│   ├── test_fetcher_agent.py
│   ├── test_parser_agent.py
│   ├── test_price_comparer_agent.py
│   └── test_notification_agent.py
│
├── utils/
│   └── helpers.py
│
├── README.md
└── requirements.txt

# Code Start

agents/
├── fetcher_agent.py
from requests.exceptions import HTTPError, Timeout
import requests
import json

class FetcherAgent:
    def __init__(self, urls):
        self.urls = urls

    def fetch_pages(self):
        fetched_pages = []
        for url in self.urls:
            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()
                fetched_pages.append(response.text)
            except (HTTPError, Timeout) as e:
                print(f"Error fetching page {url}: {e}")
        return fetched_pages

# parser_agent.py
from bs4 import BeautifulSoup
import re

class ParserAgent:
    def __init__(self):
        pass

    def parse_pages(self, html_pages):
        product_data = []
        for html_page in html_pages:
            soup = BeautifulSoup(html_page, 'html.parser')
            title = soup.find('h1', id='title').text
            price = soup.find('span', id='priceblock_ourprice').text
            availability = soup.find('span', id='availability').text
            product_data.append({
                'title': title,
                'price': price,
                'availability': availability
            })
        return product_data

# price_comparer_agent.py
import json

class PriceComparerAgent:
    def __init__(self, product_data, price_history_file):
        self.product_data = product_data
        self.price_history_file = price_history_file

    def compare_prices(self):
        with open(self.price_history_file, 'r') as f:
            price_history = json.load(f)
        for product in self.product_data:
            product_id = product['title']
            product_price = float(re.search(r'\d+\.\d+', product['price']).group())
            if product_id in price_history and product_price < price_history[product_id]:
                print(f'Price dropped for {product_id}')
            else:
                print(f'Price for {product_id} is {product_price}')
        with open(self.price_history_file, 'w') as f:
            json.dump(self.product_data, f)

# notification_agent.py
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

class NotificationAgent:
    def __init__(self):
        self.gmail_user = 'your_email@gmail.com'
        self.gmail_pass = 'your_password'
        self.email_to = 'recipient@example.com'

    def send_notifications(self, price_data):
        msg = MIMEMultipart()
        msg['From'] = self.gmail_user
        msg['To'] = self.email_to
        msg['Subject'] = 'Price Alert'
        body = 'Price dropped for ' + price_data
        msg.attach(MIMEText(body, 'plain'))
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(self.gmail_user, self.gmail_pass)
        text = msg.as_string()
        server.sendmail(self.gmail_user, self.email_to, text)
        server.quit()

# helpers.py
import json

def load_price_history(price_history_file):
    with open(price_history_file, 'r') as f:
        price_history = json.load(f)
    return price_history

def save_price_history(price_history, price_history_file):
    with open(price_history_file, 'w') as f:
        json.dump(price_history, f)

# tests/
├── test_fetcher_agent.py
from agents.fetcher_agent import FetcherAgent
from unittest.mock import Mock

class TestFetcherAgent:
    def test_fetch_pages(self):
        urls = ['https://www.amazon.com/dp/1234567890']
        fetcher = FetcherAgent(urls)
        fetched_pages = fetcher.fetch_pages()
        self.assertEqual(len(fetched_pages), 1)

# parser_agent.py
from bs4 import BeautifulSoup
import re
import requests
import unittest

class TestParserAgent(unittest.TestCase):
    def test_parse_pages(self):
        from bs4 import BeautifulSoup as bs
        from requests.exceptions import HTTPError
        from bs4 import BeautifulSoup
        html_pages = ['<!DOCTYPE html><html><head><title>Page 1</title></head><body><h1 id="title">Page 1</h1><span id="priceblock_ourprice">10.00</span><span id="availability">In Stock</span></body></html>']
        parser = ParserAgent()
        product_data = parser.parse_pages(html_pages)
        self.assertEqual(len(product_data), 1)
        self.assertEqual(product_data[0]['title'], 'Page 1')
        self.assertEqual(product_data[0]['price'], '10.00')
        self.assertEqual(product_data[0]['availability'], 'In Stock')

# price_comparer_agent.py
from unittest.mock import Mock
import unittest

class TestPriceComparerAgent:
    def test_compare_prices(self):
        product_data = [{'title': 'Product 1', 'price': '10.00', 'availability': 'In Stock'},
                        {'title': 'Product 2', 'price': '20.00', 'availability': 'In Stock'}]
        price_history_files = ['price_history_file.json']
        price_comparer = PriceComparerAgent(product_data, price_history_files)
        price_comparer.compare_prices()
        self.assertEqual(price_comparer.product_data[0]['price'], '10.00')
        self.assertEqual(price_comparer.product_data[1]['price'], '20.00')

# notification_agent.py
import unittest
from unittest.mock import Mock
import smtplib

class TestNotificationAgent(unittest.TestCase):
    def test_send_notifications(self):
        notification_agent = NotificationAgent()
        price_data = 'Price dropped for Product 1'
        notification_agent.send_notifications(price_data)
        # Assuming that successfull sending of email is handled by smtplib
        # This test only checks if no error is raised
        self.assertTrue(True)

# helpers.py
@RunWith(Pytest)
import pytest
import json

def test_load_price_history():
    with open('price_history_file.json', 'r') as f:
        price_history = json.load(f)
    self.assertEqual(price_history, [])

def test_save_price_history():
    price_history = [{'title': 'Product 1', 'price': '10.00'}]
    price_history_file = 'price_history_file.json'
    save_price_history(price_history, price_history_file)
    with open(price_history_file, 'r') as f:
        loaded_price_history = json.load(f)
    self.assertEqual(loaded_price_history, price_history)