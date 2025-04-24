```markdown
# SolarCalculator: A Python Tool for Estimating Solar Panel Costs

## Description

SolarCalculator is a Python tool designed to help you estimate the costs associated with installing solar panels. It utilizes an API to retrieve location-specific data, allowing for accurate calculations of cost, return on investment (ROI), energy savings, and CO2 emissions reduction. 

## Requirements

* **Python 3.6 or higher:**  Ensure you have a compatible Python version installed.
* **requests:** This library is used to make API calls. Install it using pip:
   ```bash
   pip install requests
   ```
* **logging:** This library is used for logging errors and other important information.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/solar-calculator.git
   ```
2. **Navigate to the project directory:**
   ```bash
   cd solar-calculator
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Replace `YOUR_API_KEY`:**  
   In the `solar_calculator.py` file, replace `YOUR_API_KEY` with your actual API key from the solar panel data provider.

2. **Run the script:**
   ```bash
   python solar_calculator.py
   ```

3. **Enter the following information when prompted:**
   * **Surface area (m²):** The area of your roof or ground where you plan to install the solar panels.
   * **Location:** The city or region where the solar installation will be located.
   * **Consumption (kWh):** Your average monthly electricity consumption.
   * **Budget:** Your estimated budget for the solar panel installation.

4. **View the results:** The script will display the calculated cost, ROI, energy savings, and CO2 emissions saved.

**Example:**

```
Enter surface area: 10.0
Enter location: London
Enter consumption: 1000.0
Enter budget: 10000.0

Cost: 1000.0
ROI: -90.0%
Savings: 500.0
CO2 Emissions Saved: 100.0
```

## Architecture

SolarCalculator consists of a single Python file (`solar_calculator.py`) containing the following:

* **`SolarCalculator` class:**
    *  `__init__`: Initializes the class with the API key and URL.
    *  `calculate_cost`:  Calculates the cost, ROI, savings, and CO2 emissions based on user input and API data.
    *  `run`:  Handles user input, calls `calculate_cost`, and displays the results.

## API Reference

* **`SolarCalculator` class:**

    *  **`__init__(self)`:** Initializes the object with the API key and URL.

        * **Parameters:**
            * `api_key`: Your API key for accessing the solar panel data provider.
            * `api_url`: The base URL of the API.

    *  **`calculate_cost(self, surface: float, location: str, consumption: float, budget: float) -> Dict`:** Calculates the cost, ROI, savings, and CO2 emissions.

        * **Parameters:**
            * `surface`: The surface area of the solar panel installation (in square meters).
            * `location`: The location of the installation.
            * `consumption`: Your average monthly electricity consumption (in kilowatt-hours).
            * `budget`: Your estimated budget for the installation.

        * **Returns:** A dictionary containing the calculated values for:
            * `cost`: The total cost of the installation.
            * `roi`: The return on investment as a percentage.
            * `savings`: The estimated annual energy savings.
            * `co2_emissions`: The estimated annual CO2 emissions saved.

    *  **`run(self)`:** Runs the interactive user interface for the SolarCalculator.

## Testing

This project includes unit tests written using the `pytest` framework. To run the tests:

```bash
pytest
```

## Contributing

Contributions are welcome! Please follow these guidelines:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them.
4. Push your branch to your fork.
5. Submit a pull request.

## License

SolarCalculator is licensed under the MIT License.



```