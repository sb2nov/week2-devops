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
    expected_quotes = [
        "Test quote 1",
        "Test quote 2",
        "Test quote 3",
    ]
    mocker.patch("random.randrange", return_value=0)
    mocker.patch("app.quotes", expected_quotes)
    response = client.get("/quote")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == expected_quotes[0]
