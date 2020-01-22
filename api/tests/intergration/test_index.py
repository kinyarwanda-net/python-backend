from api import app
import pytest


@pytest.fixture
def app():
    app_server = app()
    return app_server


# def test_index(client):
#     r = client.get('/')  # Assumes that it has a path of "/"
#     assert r.status_code == 200  # Assumes that it will return a 200 response
