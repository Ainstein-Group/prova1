```python
import pytest
from unittest.mock import patch, MagicMock
import logging
from your_module import SolarCalculator  # Replace with actual module name

@pytest.fixture
def mock_api_key():
    return "TEST_API_KEY"

@pytest.fixture
def mock_api_url():
    return "https://test.api.com"

@pytest.fixture
def mock_location_data():
    return {
        "cost_per_square_meter": 100.0,
        "savings_per_kwh": 0.5,
        "co2_emissions_per_kwh": 0.2
    }

@pytest.fixture
def mock_response(mock_location_data):
    response = MagicMock()
    response.json.return_value = mock_location_data
    return response

@pytest.fixture
def solar_calculator(mock_api_key, mock_api_url):
    return SolarCalculator()

def test_calculate_cost_normal_input(solar_calculator, mock_api_key, mock_api_url, mock_location_data, mock_response):
    """
    Test calculate_cost with normal input values.
    """
    with patch('requests.get', return_value=mock_response) as mock_get:
        surface = 10.0
        location = "Test Location"
        consumption = 1000.0
        budget = 10000.0
        
        result = solar_calculator.calculate_cost(surface, location, consumption, budget)
        
        assert result == {
            "cost": 1000.0,
            "roi": (1000 - 10000)/10000 * 100,
            "savings": 500.0,
            "co2_emissions": 100.0
        }
        mock_get.assert_called_once_with(
            f"{mock_api_url}/location/Test%20Location",
            headers={"Authorization": f"Bearer {mock_api_key}"}
        )

def test_calculate_cost_zero_surface(solar_calculator, mock_api_key, mock_api_url, mock_location_data, mock_response):
    """
    Test calculate_cost with zero surface area.
    """
    with patch('requests.get', return_value=mock_response) as mock_get:
        surface = 0.0
        location = "Test Location"
        consumption = 1000.0
        budget = 10000.0
        
        result = solar_calculator.calculate_cost(surface, location, consumption, budget)
        
        assert result == {
            "cost": 0.0,
            "roi": (0 - 10000)/10000 * 100,
            "savings": 500.0,
            "co2_emissions": 100.0
        }
        mock_get.assert_called_once_with(
            f"{mock_api_url}/location/Test%20Location",
            headers={"Authorization": f"Bearer {mock_api_key}"}
        )

def test_calculate_cost_negative_budget(solar_calculator, mock_api_key, mock_api_url, mock_location_data, mock_response):
    """
    Test calculate_cost with negative budget.
    """
    with patch('requests.get', return_value=mock_response) as mock_get:
        surface = 10.0
        location = "Test Location"
        consumption = 1000.0
        budget = -10000.0
        
        result = solar_calculator.calculate_cost(surface, location, consumption, budget)
        
        assert result == {
            "cost": 1000.0,
            "roi": (1000 - (-10000))/(-10000) * 100,
            "savings": 500.0,
            "co2_emissions": 100.0
        }
        mock_get.assert_called_once_with(
            f"{mock_api_url}/location/Test%20Location",
            headers={"Authorization": f"Bearer {mock_api_key}"}
        )

def test_calculate_cost_invalid_location(solar_calculator, mock_api_key, mock_api_url):
    """
    Test calculate_cost with invalid location that returns empty data.
    """
    with patch('requests.get', return_value=MagicMock(json=MagicMock(side_effect=KeyError))) as mock_get:
        surface = 10.0
        location = "Invalid Location"
        consumption = 1000.0
        budget = 10000.0
        
        result = solar_calculator.calculate_cost(surface, location, consumption, budget)
        
        assert result == {}
        mock_get.assert_called_once_with(
            f"{mock_api_url}/location/Invalid%20Location",
            headers={"Authorization": f"Bearer {mock_api_key}"}
        )

def test_calculate_cost_api_failure(solar_calculator, mock_api_key, mock_api_url):
    """
    Test calculate_cost when API call fails.
    """
    with patch('requests.get', side_effect=Exception("API Error")) as mock_get:
        surface = 10.0
        location = "Test Location"
        consumption = 1000.0
        budget = 10000.0
        
        result = solar_calculator.calculate_cost(surface, location, consumption, budget)
        
        assert result == {}
        mock_get.assert_called_once_with(
            f"{mock_api_url}/location/Test%20Location",
            headers={"Authorization": f"Bearer {mock_api_key}"}
        )

def test_run_method(solar_calculator, mock_api_key, mock_api_url, mock_location_data, mock_response):
    """
    Test run method with mocked user input.
    """
    with patch('builtins.input', side_effect=["10.0", "Test Location", "1000.0", "10000.0"]), \
         patch('requests.get', return_value=mock_response):
        
        solar_calculator.run()
        
        # Verify calculate_cost was called with correct arguments
        solar_calculator.calculate_cost.assert_called_once_with(10.0, "Test Location", 1000.0, 10000.0)

def test_logging_error_on_api_failure(solar_calculator, mock_api_key, mock_api_url):
    """
    Test logging when API call fails.
    """
    with patch('requests.get', side_effect=Exception("API Error")), \
         patch('logging.error') as mock_logging_error:
        
        solar_calculator.calculate_cost(10.0, "Test Location", 1000.0, 10000.0)
        
        mock_logging_error.assert_called_once_with("Error calculating cost: API Error")
```