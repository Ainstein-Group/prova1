Ecco il codice per i test unitari:

```python
import unittest
from agent import Agent  # Sostituire 'agent' con il modulo corretto

class TestAgentMethods(unittest.TestCase):

    def setUp(self):
        self.agent = Agent("test_agent")

    def test_get_id(self):
        self.assertEqual(self.agent.get_id(), "test_agent")

    def test_get_state(self):
        self.assertIsInstance(self.agent.get_state(), dict)

    def test_send_message(self):
        self.agent.send_message("agent2", "Hello")
        self.assertEqual(len(self.agent.messages), 1)
        self.assertEqual(self.agent.messages[0], {"receiver": "agent2", "content": "Hello"})

    def test_receive_message(self):
        self.agent.receive_message("agent1", "Hi there")
        self.assertEqual(self.agent.state["messages"][0], "Hi there")

    def test_update_state(self):
        new_state = {"status": "active", "messages": []}
        self.agent.update_state(new_state)
        self.assertDictEqual(self.agent.get_state(), new_state)

if __name__ == "__main__":
    unittest.main()
```