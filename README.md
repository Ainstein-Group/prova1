```markdown
# Amazon Price Monitor
==================

This project monitors product prices on Amazon using a Python multi-agent system.

## Overview
The Amazon Price Monitor allows you to track the prices of specific products on Amazon and receive notifications when prices change. 

## Project Structure

- **`agents/`**: Contains the classes responsible for different aspects of the monitoring process. 
    -  `download_agent.py`: Downloads the HTML content of product pages.
    -  `extract_agent.py`: Extracts product information (name, price, availability) from the downloaded HTML.
    -  `compare_agent.py`: Compares extracted prices with previously recorded data, identifying price changes.
    -  `notify_agent.py`: Sends notifications (e.g., email) when price changes are detected.
- **`tests/`**: Contains the unit tests for each agent.
- **`data/`**: 
    - `price_history.json`: Stores the previously recorded price history for each product.
- **`main.py`**: Orchestrates the monitoring process by managing agents and interacting with the data.
- **`README.md`**: This documentation file.
- **`requirements.txt`**: Lists the project's dependencies.

## Dependencies

To use this project, you need to have the following Python packages installed:

```bash
pip install requests beautifulsoup4 pytest
```

## Usage

1. **Configure price history:**
   - Update the `data/price_history.json` file with the initial prices for the products you want to monitor.
2. **Run the monitor:**
   - execute `python main.py` to start the price monitoring process.

3. **(Optional) Customize notifications:**
   -  Modify the `notify_agent.py` to configure email settings and notification methods.

## Features

- **Multi-agent architecture:** Different agents handle specific tasks like downloading, extracting data, comparing prices, and sending notifications.
- **Price history tracking:**  Records price changes over time, allowing for price trend analysis.
- **Flexible notification system:** Can be configured to send emails or any other type of notification when price thresholds are met.

## Contributing

Contributions are welcome! Here's how you can help:

- **Report issues:** If you encounter any bugs or problems, please submit an issue report on GitHub.
- **Suggest improvements:**  Share your ideas for new features or enhancements.
- **Contribute code:**  Contribute code patches or new features.


Remember to follow the project's coding style and guidelines.