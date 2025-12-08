import os
import sys

import pytest

# Point sys.path to the 'auth' directory (the parent of 'src')
# This allows us to see 'src' as a package.
SEARCH_PATH_PRIORITY_INDEX = 0
sys.path.insert(SEARCH_PATH_PRIORITY_INDEX, os.path.join(os.path.dirname(__file__), '../../'))

# Import via the package name
from src.auth_service import app  # noqa: E402

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.requirement("REQ-CORE-OPS-001")
def test_health_check(client):
    """
    Sanity Check:
    Ensures the Auth service can start and respond to HTTP requests.
    Verifies REQ-CORE-OPS-001 (Container Health).
    """
    response = client.get('/health')

    assert response.status_code == 200
    json_data = response.get_json()
    assert json_data["status"] == "ok"
    assert json_data["service"] == "novaeco-auth"
    assert json_data["protocol"] == "http"

@pytest.mark.requirement("REQ-CORE-FUNC-001")
def test_mock_login(client):
    """
    Verifies the mock login endpoint works.
    Partial verification of REQ-CORE-FUNC-001 (Universal Identity).
    """
    response = client.post('/login')
    assert response.status_code == 200
    json_data = response.get_json()

    # Assert we got a token back
    assert "token" in json_data
    assert json_data["token"] == "mock-jwt-token-123"