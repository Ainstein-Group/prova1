Your final answer must be the great and the most complete as possible, it must be outcome described.

```python
import pytest
from unittest.mock import Mock, patch
from typing import List, Dict
from your_module import (
    NLPEngine,
    ContextManager,
    AgentModule,
    create_agents,
    main
)

@pytest.fixture
def llm_list() -> List[str]:
    """Fixture providing a list of LLM models for testing."""
    return ['bert-base-uncased', 'roberta-base']

@pytest.fixture
def agent_module(llm_list) -> AgentModule:
    """Fixture providing an instance of AgentModule."""
    return AgentModule(llm_list)

@pytest.fixture
def context_manager() -> ContextManager:
    """Fixture providing an instance of ContextManager."""
    return ContextManager()

def test_nlpe_engine_init():
    """Test initialization of NLPEngine with a valid model."""
    model = "test-model"
    engine = NLPEngine(model)
    assert engine.model == model

def test_nlpe_process_text():
    """Test process_text method of NLPEngine."""
    engine = NLPEngine("test-model")
    result = engine.process_text("test-text")
    assert isinstance(result, Dict)

def test_context_manager_update(context_manager):
    """Test update_context method of ContextManager."""
    key = "test-key"
    value = "test-value"
    context_manager.update_context(key, value)
    assert context_manager.get_context(key) == value

def test_context_manager_get_missing(context_manager):
    """Test get_context with a missing key."""
    key = "missing-key"
    assert context_manager.get_context(key) == ''

def test_agent_module_init(llm_list):
    """Test initialization of AgentModule with valid LLMs."""
    module = AgentModule(llm_list)
    assert module.llms == llm_list
    assert isinstance(module.nlp_engine, NLPEngine)
    assert isinstance(module.context_manager, ContextManager)

def test_agent_module_process_input(agent_module, llm_list):
    """Test process_input method of AgentModule."""
    input_text = "test-input"
    with patch.object(agent_module.nlp_engine, 'process_text') as mock_process:
        mock_process.return_value = {"output": "test-output"}
        result = agent_module.process_input(input_text)
        assert result == {"output": "test-output"}
        mock_process.assert_called_once_with(input_text)

def test_agent_module_process_input_error(agent_module, llm_list):
    """Test error handling in process_input method."""
    input_text = "test-input"
    error_message = "Test error"
    with patch.object(agent_module.nlp_engine, 'process_text', side_effect=Exception(error_message)):
        result = agent_module.process_input(input_text)
        assert result == 'Error processing input'

def test_agent_module_get_response(agent_module, llm_list):
    """Test get_response method of AgentModule."""
    input_text = "test-input"
    with patch.object(agent_module.nlp_engine, 'process_text') as mock_process:
        mock_process.return_value = {"response": "test-response"}
        result = agent_module.get_response(input_text)
        assert result == {"response": "test-response"}
        mock_process.assert_called_once_with(input_text)

def test_agent_module_get_response_error(agent_module, llm_list):
    """Test error handling in get_response method."""
    input_text = "test-input"
    error_message = "Test error"
    with patch.object(agent_module.nlp_engine, 'process_text', side_effect=Exception(error_message)):
        result = agent_module.get_response(input_text)
        assert result == 'Error generating response'

def test_create_agents(llm_list):
    """Test create_agents function."""
    agents = create_agents(llm_list)
    assert len(agents) == len(llm_list)
    for i, agent in enumerate(agents):
        assert agent.role == "Code Writer"
        assert agent.goal == "Scrivere codice Python per agenti CrewAI"
        assert agent.backstory == "Esperto di multi-agente."
        assert agent.llm == llm_list[i]

def test_main(mocker, llm_list):
    """Test main function."""
    mock_crew = mocker.Mock()
    with patch('your_module.Crew', mock_crew), patch('your_module.AgentModule') as mock_agent_module:
        main()
        mock_agent_module.assert_called_once_with(llm_list)
        assert len(mock_crew.call_args_list) > 0
```