import pytest
from unittest.mock import patch
from website.web_app import app


@pytest.fixture
def mock_requests_get():
    with patch('requests.get') as mock_get:
        yield mock_get


@pytest.fixture
def mock_bs4():
    with patch('bs4.BeautifulSoup') as mock_bs:
        yield mock_bs
        

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client
