# test_integration_users_mocked.py

import requests
import responses

BASE_URL = "http://127.0.0.1:8000/users"
HEADERS = {
    "Accept": "text/plain"
}

@responses.activate
def test_unauthorized_user_access():
    """Mock test for 401 response with empty body when wrong password is provided."""
    params = {
        "username": "admin",
        "password": "admin"
    }

    # Register mock response for unauthorized access
    responses.add(
        responses.GET,
        BASE_URL,
        match=[responses.matchers.query_param_matcher(params)],
        body="",
        status=401,
        content_type="text/plain"
    )

    response = requests.get(BASE_URL, params=params, headers=HEADERS)

    assert response.status_code == 401, f"Expected 401, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"


@responses.activate
def test_authorized_user_access_but_empty_response():
    """Mock test for 200 response with empty body when correct password is provided."""
    params = {
        "username": "admin",
        "password": "qwerty"
    }

    # Register mock response for authorized access with empty result
    responses.add(
        responses.GET,
        BASE_URL,
        match=[responses.matchers.query_param_matcher(params)],
        body="",
        status=200,
        content_type="text/plain"
    )

    response = requests.get(BASE_URL, params=params, headers=HEADERS)

    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    assert response.text.strip() == "", f"Expected empty response, got: {response.text}"

