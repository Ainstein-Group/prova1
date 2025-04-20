Ecco il codice completo dei test unitari per il codice Python fornito, utilizzando il framework `unittest` e mock per le dipendenze:

```python
import unittest
from unittest.mock import Mock, patch
from your_module import MultiAgentSystem, EnergyAnalyst, SustainabilityAdvisor, CostEstimator, GovernmentProgramChecker

class TestMultiAgentSystem(unittest.TestCase):
    def setUp(self):
        self.energy_analyst_mock = Mock(spec=EnergyAnalyst)
        self.sustainability_advisor_mock = Mock(spec=SustainabilityAdvisor)
        self.cost_estimator_mock = Mock(spec=CostEstimator)
        self.government_program_checker_mock = Mock(spec=GovernmentProgramChecker)
        
        self.system = MultiAgentSystem()
        self.system.energy_analyst = self.energy_analyst_mock
        self.system.sustainability_advisor = self.sustainability_advisor_mock
        self.system.cost_estimator = self.cost_estimator_mock
        self.system.government_program_checker = self.government_program_checker_mock
        
        # Setup return values
        self.energy_analyst_mock.get_results.return_value = {"energy_data": "test"}
        self.sustainability_advisor_mock.get_recommendations.return_value = ["recommendation1", "recommendation2"]
        self.cost_estimator_mock.get_results.return_value = {"costs": "test"}
        self.government_program_checker_mock.get_results.return_value = {"incentives": "test"}
        
    def test_run(self):
        self.system.run()
        
        self.energy_analyst_mock.collect_data.assert_called_once()
        self.sustainability_advisor_mock.analyze_data.assert_called_once_with({"energy_data": "test"})
        self.sustainability_advisor_mock.generate_recommendations.assert_called_once()
        self.cost_estimator_mock.estimate_costs.assert_called_once_with(["recommendation1", "recommendation2"])
        self.government_program_checker_mock.check_programs.assert_called_once()
        self.cost_estimator_mock.update_incentives.assert_called_once_with({"incentives": "test"})
        
    def test_collect_initial_data(self):
        self.system.collect_initial_data()
        
        self.energy_analyst_mock.collect_data.assert_called_once()
        self.sustainability_advisor_mock.analyze_data.assert_called_once_with({"energy_data": "test"})
        
    def test_recommend_interventions(self):
        self.system.recommend_interventions()
        
        self.sustainability_advisor_mock.generate_recommendations.assert_called_once()
        
    def test_perform_cost_benefit_analysis(self):
        self.system.perform_cost_benefit_analysis()
        
        self.cost_estimator_mock.estimate_costs.assert_called_once_with(["recommendation1", "recommendation2"])
        
    def test_identify_incentives(self):
        self.system.identify_incentives()
        
        self.government_program_checker_mock.check_programs.assert_called_once()
        self.cost_estimator_mock.update_incentives.assert_called_once_with({"incentives": "test"})
        
    def test_generate_final_report(self):
        self.system.generate_final_report()
        
        self.assertEqual(self.system.generate_final_report(), {
            "Energy Analysis": {"energy_data": "test"},
            "Recommended Interventions": ["recommendation1", "recommendation2"],
            "Cost-Benefit Analysis": {"costs": "test"},
            "Incentives": {"incentives": "test"}
        })

if __name__ == "__main__":
    unittest.main()
```