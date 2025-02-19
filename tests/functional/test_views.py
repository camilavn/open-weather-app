import json
import pytest
from datetime import datetime
from website import create_app

def fake_requests_get(url, *args, **kwargs):
    if "weather?" in url:
        dummy_weather = {
            "dt": 1738728439,
            "main": {
                "temp": 4.93,
                "temp_min": 3.08,
                "pressure": 1033,
                "humidity": 88
            },
            "weather": [{
                "description": "clear sky",
                "icon": "01n"
            }],
            "wind": {"speed": 3.6},
            "visibility": 10000
        }
        # Format the time as "1:28 pm"
        dummy_weather['formatted_time'] = datetime.utcfromtimestamp(dummy_weather['dt']).strftime('%-I:%M %p').lower()
        class DummyResponse:
            status_code = 200
            text = json.dumps(dummy_weather)
            def json(self):
                return dummy_weather
        return DummyResponse()
    elif "forecast?" in url:
        dummy_forecast = {
            "list": [
                {
                    "dt_txt": "2025-02-20 12:00:00",
                    "main": {"temp_min": 2, "temp_max": 6},
                    "weather": [{"description": "clear sky", "icon": "01n"}]
                },
                {
                    "dt_txt": "2025-02-21 12:00:00",
                    "main": {"temp_min": 1, "temp_max": 5},
                    "weather": [{"description": "partly cloudy", "icon": "02n"}]
                }
            ]
        }
        class DummyResponse:
            status_code = 200
            text = json.dumps(dummy_forecast)
            def json(self):
                return dummy_forecast
        return DummyResponse()
    else:
        class DummyResponse:
            status_code = 404
            text = ""
            def json(self):
                return {}
        return DummyResponse()

@pytest.fixture
def test_client():
    app = create_app()
    app.testing = True
    with app.test_client() as client:
        yield client

def test_index_get(test_client):
    """
    GIVEN a Flask application configured for testing (user not logged in)
    WHEN the '/' page is requested via GET
    THEN the response status code is 200 and the page contains the 'Weather' dropdown button.
    """
    response = test_client.get('/', follow_redirects=True)
    assert response.status_code == 200
    assert b"Weather" in response.data

def test_index_post_current_weather(test_client, monkeypatch):
    """
    GIVEN a Flask application configured for testing and a valid POST request with city, state, and country
    WHEN the '/' page is posted to with valid input
    THEN the response status code is 200 and the page displays the current weather details ( temperature, description).
    """
    monkeypatch.setattr("requests.get", fake_requests_get)
    data = {"city": "London", "state": "", "country": "GB"}
    response = test_client.post("/", data=data, follow_redirects=True)
    assert response.status_code == 200
    # Verify that the current weather section appears with dummy data.
    assert b"Current Weather" in response.data
    assert b"4.93" in response.data
    assert b"clear sky" in response.data

def test_index_post_forecast(test_client, monkeypatch):
    """
    GIVEN a Flask application configured for testing and a valid POST request with city, state, and country
    WHEN the '/' page is posted to with valid input
    THEN the response contains the '5-Day Forecast' header and at least one forecast date from the dummy forecast data.
    """
    monkeypatch.setattr("requests.get", fake_requests_get)
    data = {"city": "London", "state": "", "country": "GB"}
    response = test_client.post("/", data=data, follow_redirects=True)
    assert response.status_code == 200
    # Verify that the 5-Day Forecast header is present.
    assert b"5-Day Forecast" in response.data
    # Verify that one of the dummy forecast dates (e.g., "2025-02-20") is present.
    assert b"2025-02-20" in response.data
