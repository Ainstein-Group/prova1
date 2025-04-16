```markdown
# amazon_price_monitor

This project is an open-source tool to monitor the price of products on Amazon and send you notifications when the price drops.


##  Getting Started

1. **Installation:**

   ```bash
   pip install -r requirements.txt
   ```

2. **Configuration:**

   - You need to configure the project with the URLs of the Amazon product pages you want to monitor.
   - You can also customize the email settings for notifications.

3. **Usage:**

   - Run the `main.py` script.
   - The script will fetch the product data from the specified URLs, parse the prices, compare them to historical prices, and send notifications if a price drop is detected.

## Features

- **Price Monitoring:** Tracks the prices of products on Amazon.
- **Historical Price Comparison:** Compares current prices to previously recorded prices.
- **Price Drop Notifications:** Sends email notifications when a product's price drops below a certain threshold.
- **Extensible Architecture:** Allows for easy integration of new features and functionality.

## Components

- **Fetcher Agent:** Responsible for fetching the HTML content of the product pages.
- **Parser Agent:** Extracts relevant product information (title, price, availability) from the HTML content.
- **Price Comparer Agent:** Compares the current product prices to historical prices and identifies price drops.
- **Notification Agent:** Sends email notifications to the configured recipients.


## Requirements

- Python 3.6+
- `requests`: For making HTTP requests to retrieve product data.
- `beautifulsoup4`: For parsing HTML content.
- `json`: For handling JSON data (historical price storage).
- `smtplib`: For sending email notifications.



## Project Structure

```
amazon_price_monitor/
└── agents/
    └── fetcher_agent.py
└── tests/
    └── test_fetcher_agent.py
└── utils/
    └── helpers.py
└── README.md


```



Feel free to contribute to the project or open issues for any requests or bug reports.