```python
import pytest
from unittest.mock import patch, Mock
from your_module import (  # Replace 'your_module' with the actual module name
    GroqLLM,
    create_agents,
    GitHubUploaderAgent,
    run_pipeline
)

@pytest.fixture
def mock_llm():
    llm = Mock(spec=GroqLLM)
    llm._call.return_value = "Test response"
    return llm

@pytest.fixture
def mock_github():
    with patch("github.Github") as mock_github:
        yield mock_github

@pytest.fixture
def mock_requests_post():
    with patch("requests.post") as mock_post:
        yield mock_post

@pytest.fixture
def mock_temp_dir():
    with patch("tempfile.mkdtemp") as mock_temp:
        yield mock_temp

@pytest.fixture
def mock_zipfile():
    with patch("zipfile.ZipFile") as mock_zip:
        yield mock_zip

class TestGroqLLM:
    def test__call(self, mock_requests_post):
        llm = GroqLLM("test_model", "test_key")
        response = Mock()
        response.json.return_value = {"choices": [{"message": {"content": "test"}}]}
        mock_requests_post.return_value = response
        
        result = llm._call("test prompt")
        assert result == "test"
        
        # Verify the request was made correctly
        mock_requests_post.assert_called_once_with(
            "https://api.groq.com/openai/v1/chat/completions",
            headers={
                "Authorization": "Bearer test_key",
                "Content-Type": "application/json"
            },
            json={
                "model": "test_model",
                "messages": [{"role": "user", "content": "test prompt"}],
                "temperature": 0.7
            }
        )
        
    def test__call_raises_exception(self, mock_requests_post):
        llm = GroqLLM("test_model", "test_key")
        mock_response = Mock()
        mock_response.raise_for_status.side_effect = Exception("Test error")
        mock_requests_post.return_value = mock_response
        
        with pytest.raises(Exception):
            llm._call("test prompt")

class TestCreateAgents:
    def test_create_agents(self, mock_llm):
        llm1 = Mock()
        llm2 = Mock()
        llm3 = Mock()
        llm4 = Mock()
        
        prompt_writer, code_writer, code_tester, doc_writer = create_agents(llm1, llm2, llm3, llm4)
        
        # Verify all agents are created with correct parameters
        assert prompt_writer.role == "Prompt Writer"
        assert code_writer.role == "Code Writer"
        assert code_tester.role == "Tester"
        assert doc_writer.role == "Doc Writer"

class TestGitHubUploaderAgent:
    def test_upload_files(self, mock_github, mock_temp_dir, mock_zipfile):
        # Setup mock directory and files
        mock_temp_dir.return_value = "test_dir"
        test_file = "test_file.py"
        test_content = "test_content"
        
        # Create the uploader
        uploader = GitHubUploaderAgent("test_key", "test_repo", "test_dir")
        
        # Mock the file reading
        with patch("builtins.open", new=Mock()) as mock_open:
            mock_file = Mock()
            mock_file.read.return_value = test_content
            mock_open.return_value.__enter__.return_value = mock_file
            
            # Call upload files
            uploader.upload_files()
            
            # Verify files are uploaded
            uploader.repo.create_file.assert_called_with(test_file, "Caricamento file", test_content)
            
    def test_ignore_non_text_files(self, mock_github, mock_temp_dir):
        # Setup mock directory and files
        mock_temp_dir.return_value = "test_dir"
        
        # Create the uploader
        uploader = GitHubUploaderAgent("test_key", "test_repo", "test_dir")
        
        # Test that non-text files are ignored
        uploader.upload_files()
        
        # Verify that create_file was not called for non-text files
        uploader.repo.create_file.assert_not_called()

class TestRunPipeline:
    def test_run_pipeline(self, mock_llm, mock_github, mock_temp_dir, mock_zipfile, mock_requests_post):
        # Mock all dependencies
        llm1 = Mock()
        llm2 = Mock()
        llm3 = Mock()
        llm4 = Mock()
        
        # Run the pipeline
        optimized_prompt, generated_code, generated_tests, generated_docs, zip_path = run_pipeline("test_prompt")
        
        # Verify that all components are called
        llm1._call.assert_called_once()
        llm2._call.assert_called_once()
        llm3._call.assert_called_once()
        llm4._call.assert_called_once()
        
        # Verify that files are created and uploaded
        assert zip_path.endswith("generated_package.zip")
        # Add more assertions as needed
        
        # Verify that GitHub upload was called
        uploader = GitHubUploaderAgent("test_key", "test_repo", "test_dir")
        uploader.upload_files.assert_called_once()
```