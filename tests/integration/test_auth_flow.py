import requests
import os
import time

# Service URLs are based on the docker-compose.yml service names
AUTH_URL = "http://auth:9000"
API_URL = "http://api:8000"

def test_auth_service_is_live():
    """Test that the auth service is up and responding."""
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(f"{AUTH_URL}/health")
            assert response.status_code == 200
            return
        except requests.ConnectionError:
            time.sleep(5)
    assert False, "Auth service was not ready in time."

def test_api_service_is_live():
    """Test that the api service is up and responding."""
    retries = 5
    for i in range(retries):
        try:
            response = requests.get(f"{API_URL}/health")
            assert response.status_code == 200
            return
        except requests.ConnectionError:
            time.sleep(5)
    assert False, "API service was not ready in time."

def test_full_login_and_api_call():
    """
    Integration Test:
    1. Get a test token from the /auth service.
    2. Use that token to call a protected endpoint on the /api service.
    """
    
    # Step 1: Get token from Auth service
    # (This is a simplified example; your service might have a /login route)
    token_response = requests.post(f"{AUTH_URL}/get-test-token")
    assert token_response.status_code == 200
    token = token_response.json().get("access_token")
    assert token is not None

    # Step 2: Use token to call protected API service
    headers = { "Authorization": f"Bearer {token}" }
    api_response = requests.get(f"{API_URL}/v1/protected/me", headers=headers)
    
    assert api_response.status_code == 200
    assert api_response.json().get("user_id") == "test-user"