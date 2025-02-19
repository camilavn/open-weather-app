import pytest
from website import create_app

@pytest.fixture(scope='session')
def app():
    """
    GIVEN a Flask application factory
    WHEN the app is created for testing
    THEN the application is configured with TESTING=True.
    """
    app = create_app()
    app.config['TESTING'] = True
    yield app

@pytest.fixture
def test_client(app):
    """
    GIVEN a Flask application configured for testing
    WHEN a test client is created
    THEN the client can be used to simulate HTTP requests.
    """
    with app.test_client() as client:
        yield client
