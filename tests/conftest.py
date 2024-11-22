import pytest
from website import create_app, db
from website.models import User
import os

@pytest.fixture(scope='module')
def test_client():
    # Set the Testing configuration prior to creating the Flask application
    os.environ['CONFIG_TYPE'] = 'config.TestingConfig'
    flask_app = create_app()

    # Create a test client using the Flask application configured for testing
    with flask_app.test_client() as test_client:
        yield test_client # this is where the testing happens!


@pytest.fixture(scope='module')
def init_database(test_client):

    test_client.post('/signup', data=dict(username='test', password='test'), follow_redirects=True)

    yield # this is where the testing happens!

    # Delete the user after the tests run
    with test_client.application.app_context():
        db.drop_all()


@pytest.fixture(scope='module')
def login_user(test_client, init_database):
    test_client.post('/login', data=dict(username='test', password='test'), follow_redirects=True)

    yield

    test_client.get('/logout', follow_redirects=True)