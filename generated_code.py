```
import crewai
import groq
import logging
from typing import Dict, Any

logging.basicConfig(level=logging.INFO)

class SolarCalculator:
    def __init__(self):
        self.data = {
            "superficie": 0,
            "località": "",
            "consumo": 0,
            "budget": 0
        }

    def set_data(self, superficie: int, località: str, consumo: int, budget: int) -> None:
        self.data["superficie"] = superficie
        self.data["località"] = località
        self.data["consumo"] = consumo
        self.data["budget"] = budget

    def calculate_cost(self) -> float:
        # Calcolo del costo stimato dell'impianto solare
        cost = (self.data["consumo"] * 0.1) + (self.data["superficie"] * 0.05)
        return cost

    def calculate_roi(self) -> float:
        # Calcolo del Ritorno sull'Investimento (ROI)
        roi = (self.data["budget"] - self.data["consumo"]) / self.data["budget"]
        return roi

    def calculate_saving(self) -> float:
        # Calcolo del risparmio economico
        saving = self.data["budget"] - self.data["consumo"]
        return saving

    def calculate_incentives(self) -> float:
        # Calcolo degli incentivi disponibili
        incentives = self.data["budget"] * 0.1
        return incentives

    def calculate_co2_saving(self) -> float:
        # Calcolo della quantità di CO₂ risparmiata
        co2_saving = self.data["consumo"] * 0.05
        return co2_saving

    def run(self) -> Dict[str, Any]:
        self.set_data(**dati_fittizi)
        cost = self.calculate_cost()
        roi = self.calculate_roi()
        saving = self.calculate_saving()
        incentives = self.calculate_incentives()
        co2_saving = self.calculate_co2_saving()
        return {
            "cost": cost,
            "roi": roi,
            "saving": saving,
            "incentives": incentives,
            "co2_saving": co2_saving
        }

dati_fittizi = {
    "superficie": 50,
    "località": "Roma",
    "consumo": 8000,
    "budget": 20000
}

calculator = SolarCalculator()
result = calculator.run()
print(result)
```