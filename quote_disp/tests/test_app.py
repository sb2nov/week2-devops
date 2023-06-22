import random
from flask import Flask, render_template
from flask.testing import FlaskClient
import pytest

from ..app import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.data == b"healthy"
    
def test_home(client):
    response = client.get("/")
    assert response.status_code == 200


def test_quote(client, mocker):
    expected_quote = "Test quote"
    mocker.patch("requests.get", return_value=MockResponse(expected_quote))
    response = client.get("/get_quote")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == render_template("quote.html", quote=expected_quote)


class MockResponse:
    def __init__(self, text):
        self.text = text