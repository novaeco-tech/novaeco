import pytest
import sys
import os

# Point sys.path to the 'app' directory (the parent of 'src')
# This allows us to see 'src' as a package.
SEARCH_PATH_PRIORITY_INDEX = 0
sys.path.insert(SEARCH_PATH_PRIORITY_INDEX, os.path.join(os.path.dirname(__file__), '../../'))

# Import via the package name
# NEW: from src.app_service import app
from src.app_service import app

@pytest.fixture
def client():
    """Creates a test client for the Flask application."""
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@pytest.mark.requirement("REQ-CORE-FUNC-003")
def test_dashboard_loads(client):
    """
    Sanity Check:
    Ensures the Mission Control dashboard renders (HTTP 200).
    Verifies REQ-CORE-FUNC-003 (Launchpad Discovery).
    """
    response = client.get('/')
    
    # 1. Assert successful response
    assert response.status_code == 200
    
    # 2. Assert content is HTML and contains the title
    assert b"NovaEco Mission Control" in response.data
    assert b"Launchpad" in response.data