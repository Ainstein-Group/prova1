Your final answer must be the great and the most complete as possible, it must be outcome described.

```python
import pytest
from unittest.mock import patch
from your_module import SolarCalculator  # Sostituire con il nome del modulo reale

@pytest.fixture
def mock_data():
    return {
        "superficie": 50,
        "località": "Roma",
        "consumo": 8000,
        "budget": 20000
    }

def test_init():
    """Test che verifica l'inizializzazione corretta dell'oggetto SolarCalculator."""
    calculator = SolarCalculator()
    assert calculator.data == {
        "superficie": 0,
        "località": "",
        "consumo": 0,
        "budget": 0
    }

def test_set_data(mock_data):
    """Test che verifica l'impostazione corretta dei dati."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    assert calculator.data == mock_data

def test_calculate_cost(mock_data):
    """Test che verifica il calcolo corretto del costo."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    expected_cost = (mock_data["consumo"] * 0.1) + (mock_data["superficie"] * 0.05)
    assert calculator.calculate_cost() == expected_cost

def test_calculate_roi(mock_data):
    """Test che verifica il calcolo corretto del ROI."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    expected_roi = (mock_data["budget"] - mock_data["consumo"]) / mock_data["budget"]
    assert calculator.calculate_roi() == expected_roi

def test_calculate_saving(mock_data):
    """Test che verifica il calcolo corretto del risparmio."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    expected_saving = mock_data["budget"] - mock_data["consumo"]
    assert calculator.calculate_saving() == expected_saving

def test_calculate_incentives(mock_data):
    """Test che verifica il calcolo corretto degli incentivi."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    expected_incentives = mock_data["budget"] * 0.1
    assert calculator.calculate_incentives() == expected_incentives

def test_calculate_co2_saving(mock_data):
    """Test che verifica il calcolo corretto della quantità di CO₂ risparmiata."""
    calculator = SolarCalculator()
    calculator.set_data(**mock_data)
    expected_co2_saving = mock_data["consumo"] * 0.05
    assert calculator.calculate_co2_saving() == expected_co2_saving

def test_run(mock_data):
    """Test che verifica l'esecuzione corretta del metodo run."""
    calculator = SolarCalculator()
    result = calculator.run()
    assert isinstance(result, dict)
    assert "cost" in result
    assert "roi" in result
    assert "saving" in result
    assert "incentives" in result
    assert "co2_saving" in result

def test_calculate_roi_zero_budget():
    """Test che verifica il calcolo del ROI con budget zero."""
    calculator = SolarCalculator()
    calculator.set_data(superficie=50, località="Roma", consumo=8000, budget=0)
    with pytest.raises(ZeroDivisionError):
        calculator.calculate_roi()

def test_calculate_cost_zero_values():
    """Test che verifica il calcolo del costo con valori zero."""
    calculator = SolarCalculator()
    calculator.set_data(superficie=0, località="Roma", consumo=0, budget=0)
    assert calculator.calculate_cost() == 0

def test_calculate_saving_negative():
    """Test che verifica il calcolo del risparmio con valori negativi."""
    calculator = SolarCalculator()
    calculator.set_data(superficie=50, località="Roma", consumo=25000, budget=20000)
    assert calculator.calculate_saving() == -5000

def test_calculate_incentives_zero_budget():
    """Test che verifica il calcolo degli incentivi con budget zero."""
    calculator = SolarCalculator()
    calculator.set_data(superficie=50, località="Roma", consumo=8000, budget=0)
    assert calculator.calculate_incentives() == 0
```