```python
import unittest
from unittest.mock import Mock
from your_module import CodeWriterAgent, create_agents  # Sostituisci 'your_module' con il nome del modulo

class TestCodeWriterAgent(unittest.TestCase):
    def test_code_generator_import(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "import random"
        expected_code = "import random\n"
        self.assertEqual(agent.code_generator(prompt), expected_code)

    def test_code_generator_class(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "class TestClass"
        expected_code = "class TestClass:\n"
        self.assertEqual(agent.code_generator(prompt), expected_code)

    def test_code_generator_def(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "def test_function"
        expected_code = "def test_function:\n"
        self.assertEqual(agent.code_generator(prompt), expected_code)

    def test_code_generator_multiple_commands(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "import random class TestClass def test_function"
        expected_code = "import random\nclass TestClass:\ndef test_function:\n"
        self.assertEqual(agent.code_generator(prompt), expected_code)

    def test_task_handler(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        task = Mock()
        task.description = "Scrivere codice di test"
        result = agent.task_handler(task)
        self.assertIsInstance(result, str)

    def test_create_agents(self):
        llm1 = Mock()
        llm2 = Mock()
        agents = create_agents(llm1, llm2)
        self.assertEqual(len(agents), 1)
        self.assertIsInstance(agents[0], CodeWriterAgent)

    def test_code_generator_edge_cases(self):
        agent = CodeWriterAgent(role="Test", goal="Test", backstory="Test", llm=Mock())
        prompt = "   "  # Stringa vuota o con spazi
        self.assertEqual(agent.code_generator(prompt), "\n")

if __name__ == "__main__":
    unittest.main()
```