```python
import logging
import requests
from typing import Dict, List

from crewai import Agent, Task, Crew

# Constants
API_KEY = "YOUR_API_KEY"
API_URL = "https://api.example.com"

# Logging setup
logging.basicConfig(level=logging.INFO)

class SolarCalculator:
    def __init__(self):
        self.api_key = API_KEY
        self.api_url = API_URL

    def calculate_cost(self, surface: float, location: str, consumption: float, budget: float) -> Dict:
        try:
            # Call API to get data specific to location
            response = requests.get(f"{self.api_url}/location/{location}", headers={"Authorization": f"Bearer {self.api_key}"})
            location_data = response.json()

            # Calculate cost
            cost = surface * location_data["cost_per_square_meter"]

            # Calculate ROI
            roi = (cost - budget) / budget * 100

            # Calculate savings
            savings = consumption * location_data["savings_per_kwh"]

            # Calculate CO2 emissions saved
            co2_emissions = savings * location_data["co2_emissions_per_kwh"]

            return {
                "cost": cost,
                "roi": roi,
                "savings": savings,
                "co2_emissions": co2_emissions
            }
        except Exception as e:
            logging.error(f"Error calculating cost: {e}")
            return {}

    def run(self):
        # Create UI
        surface = float(input("Enter surface area: "))
        location = input("Enter location: ")
        consumption = float(input("Enter consumption: "))
        budget = float(input("Enter budget: "))

        # Calculate cost
        result = self.calculate_cost(surface, location, consumption, budget)

        # Display results
        print("Cost:", result["cost"])
        print("ROI:", result["roi"])
        print("Savings:", result["savings"])
        print("CO2 Emissions Saved:", result["co2_emissions"])

if __name__ == "__main__":
    calculator = SolarCalculator()
    calculator.run()
```
This code defines a `SolarCalculator` class that calculates the cost of a solar panel installation based on the input parameters. It uses the `requests` library to call an API to get data specific to the location, and then calculates the cost, ROI, savings, and CO2 emissions saved. The code also includes error handling and logging.