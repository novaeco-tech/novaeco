import pytest
import sys
import os

# Ensure we can import from src/
sys.path.append(os.path.join(os.path.dirname(__file__), '../src'))

from main import app

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    # Enable testing mode (propagates exceptions, etc.)
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.requirement("REQ-CORE-OPS-001")
def test_health_endpoint_contract(client):
    """
    Verifies that the service exposes a standardized /health endpoint.
    Requirement: REQ-CORE-OPS-001 (Container Health)
    """
    response = client.get('/health')
    
    # 1. Check HTTP Status
    assert response.status_code == 200
    
    # 2. Check Payload Structure
    json_data = response.get_json()
    assert json_data["status"] == "ok"
    assert json_data["service"] == "novaeco-api-gateway"