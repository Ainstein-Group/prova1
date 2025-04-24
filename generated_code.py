```
from crewai import Agent, Task, Crew
from pdf2text import extract_text
import re
import spacy
from spacy import displacy
import networkx as nx
import matplotlib.pyplot as plt

class DocumentAgent(Agent):
    def __init__(self, document):
        super().__init__()
        self.document = document

    def process(self):
        text = extract_text(self.document)
        text = re.sub(r'\d+\.\d+|\d+\.+\d+', '', text)
        self.document_info = {'text': text}
        return self.document_info

class PreprocessingAgent(Agent):
    def __init__(self, document):
        super().__init__()
        self.document_info = document

    def process(self):
        nlp = spacy.load('it_core_web_sm')
        doc = nlp(self.document_info['text'])
        self.document_info['tokens'] = [(token.text, token.pos_) for token in doc]
        return self.document_info

class NamedEntityRecognitionAgent(Agent):
    def __init__(self, document):
        super().__init__()
        self.document_info = document

    def process(self):
        nlp = spacy.load('it_core_web_sm')
        doc = nlp(self.document_info['text'])
        self.document_info['entities'] = [(entity.text, entity.label_) for entity in doc.ents]
        return self.document_info

class KeywordExtractionAgent(Agent):
    def __init__(self, document):
        super().__init__()
        self.document_info = document

    def process(self):
        nlp = spacy.load('it_core_web_sm')
        doc = nlp(self.document_info['text'])
        frequencies = {}
        for token in doc:
            if token.text in frequencies:
                frequencies[token.text] += 1
            else:
                frequencies[token.text] = 1
        self.document_info['keywords'] = sorted(frequencies, key=frequencies.get, reverse=True)
        return self.document_info

class CoordinatorAgent(Agent):
    def __init__(self):
        super().__init__()
        self.documents = []

    def process(self):
        for document in self.documents:
            self.sender.send(document)
        return self.documents

class ResultVisualizerAgent(Agent):
    def __init__(self, documents):
        super().__init__()
        self.documents = documents

    def process(self):
        for document in self.documents:
            print('Text:', document['text'])
            print('Tokens:', [(token, pos) for token, pos in document['tokens']])
            print('Entities:', [(entity, label) for entity, label in document['entities']])
            print('Keywords:', document['keywords'])
        return None

def create_agents(documents):
    agents = []
    coord = CoordinatorAgent()
    result_visualizer = ResultVisualizerAgent(documents)
    agents.append(DocumentAgent(documents[0]))
    agents.append(PreprocessingAgent(documents[0]))
    agents.append(NamedEntityRecognitionAgent(documents[0]))
    agents.append(KeywordExtractionAgent(documents[0]))
    agents.append(coord)
    agents.append(result_visualizer)
    return agents

def kick_off_agents(agents):
    for agent in agents:
        agent.process()
    return None

documents = ['document1.pdf', 'document2.pdf', ...]
agents = create_agents(documents)
kick_off_agents(agents)
```