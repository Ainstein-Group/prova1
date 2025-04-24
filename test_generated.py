Ecco i test unitari per il codice Python fornito. Questi test verificano il corretto funzionamento di ciascuna classe e metodo:

```python
import pytest
from unittest.mock import patch
from your_module import (  # Sostituire con il nome del modulo reale
    DocumentAgent,
    PreprocessingAgent,
    NamedEntityRecognitionAgent,
    KeywordExtractionAgent,
    CoordinatorAgent,
    ResultVisualizerAgent,
    create_agents,
    kick_off_agents
)

@pytest.fixture
def mock_document():
    return "sample.pdf"

@pytest.fixture
def mock_text():
    return "Questo è un test di esempio."

@pytest.fixture
def mock_doc_with_numbers():
    return "Il numero 123.45 è presente nel testo."

@pytest.fixture
def mock_empty_document():
    return ""

def test_document_agent_process(mock_document, mock_text):
    with patch('pdf2text.extract_text', return_value=mock_text) as mock_extract:
        agent = DocumentAgent(mock_document)
        result = agent.process()
        assert 'text' in result
        assert result['text'] == mock_text
        mock_extract.assert_called_once()

def test_document_agent_clean_numbers(mock_document, mock_doc_with_numbers, mock_text):
    clean_text = re.sub(r'\d+\.\d+|\d+\.+\d+', '', mock_doc_with_numbers)
    with patch('pdf2text.extract_text', return_value=mock_doc_with_numbers) as mock_extract:
        agent = DocumentAgent(mock_document)
        result = agent.process()
        assert 'text' in result
        assert result['text'] == clean_text
        mock_extract.assert_called_once()

def test_preprocessing_agent_process(mock_document, mock_text):
    with patch('pdf2text.extract_text', return_value=mock_text) as mock_extract:
        agent = DocumentAgent(mock_document)
        doc_info = agent.process()
        
        preprocessing_agent = PreprocessingAgent(doc_info)
        result = preprocessing_agent.process()
        
        assert 'tokens' in result
        assert isinstance(result['tokens'], list)
        assert all(isinstance(token, tuple) and len(token) == 2 for token in result['tokens'])

def test_named_entity_recognition_agent_process(mock_document, mock_text):
    with patch('pdf2text.extract_text', return_value=mock_text) as mock_extract:
        agent = DocumentAgent(mock_document)
        doc_info = agent.process()
        
        ner_agent = NamedEntityRecognitionAgent(doc_info)
        result = ner_agent.process()
        
        assert 'entities' in result
        assert isinstance(result['entities'], list)
        assert all(isinstance(entity, tuple) and len(entity) == 2 for entity in result['entities'])

def test_keyword_extraction_agent_process(mock_document, mock_text):
    with patch('pdf2text.extract_text', return_value=mock_text) as mock_extract:
        agent = DocumentAgent(mock_document)
        doc_info = agent.process()
        
        keyword_agent = KeywordExtractionAgent(doc_info)
        result = keyword_agent.process()
        
        assert 'keywords' in result
        assert isinstance(result['keywords'], list)
        assert all(isinstance(keyword, str) for keyword in result['keywords'])

def test_coordinator_agent_process():
    agent = CoordinatorAgent()
    agent.documents = [{"text": "doc1"}, {"text": "doc2"}]
    result = agent.process()
    assert result == agent.documents

def test_result_visualizer_agent_process():
    documents = [{"text": "doc1", "tokens": [], "entities": [], "keywords": []},
                {"text": "doc2", "tokens": [], "entities": [], "keywords": []}]
    agent = ResultVisualizerAgent(documents)
    result = agent.process()
    assert result is None

def test_create_agents(mock_document):
    agents = create_agents([mock_document])
    assert len(agents) == 6  # 4 process agents + Coordinator + Visualizer

def test_kick_off_agents(mock_document):
    agents = create_agents([mock_document])
    result = kick_off_agents(agents)
    assert result is None

def test_empty_document_agent_process(mock_empty_document):
    agent = DocumentAgent(mock_empty_document)
    result = agent.process()
    assert 'text' in result
    assert result['text'] == ""
```