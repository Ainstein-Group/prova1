# Multi-Agent System Documentation

This directory contains the source code and documentation for a multi-agent system.

## Overview

The multi-agent system consists of multiple independent agents that can interact with each other. Each agent has its own state and can send and receive messages to other agents. Agents can update their state based on incoming messages and their own internal logic.

## Components

* **Agent:**
    * Represents a single agent in the system.
    * Has an identifier (ID), a state, and methods for sending and receiving messages.
    * Can update its state based on messages and internal logic.

## Usage

To run the multi-agent system, follow these steps:

1. Install the required dependencies (see `requirements.txt`).
2. Create instances of the `Agent` class, providing unique IDs for each agent.
3. Implement agent behavior by defining the logic within the `__init__` method of each agent's class.
4. Agents can then communicate by sending and receiving messages using the `send_message` and `receive_message` methods.
5. Agents can update their state using the `update_state` method.

## Example

```python
# Example usage
from agent import Agent

# Create two agents
agent1 = Agent("agent1")
agent2 = Agent("agent2")

# Send a message from agent1 to agent2
agent1.send_message("agent2", "Hello from agent1!")

# Agent2 receives the message
agent2.receive_message("agent1", "Hello from agent1!")
```

## Testing

The `test_agent_methods.py` file contains unit tests for the `Agent` class. To run the tests, execute the following command:

```bash
python -m unittest tests/test_agent_methods.py
```