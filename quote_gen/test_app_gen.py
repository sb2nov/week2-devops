import pytest
from flask import Flask, render_template

import app

def test_gen_health():
    client = app.app.test_client()

    response = client.get("/health")
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "healthy"

def test_gen_root_page():
    client = app.app.test_client()

    response = client.get("/")

    assert response.status_code == 200

def test_gen_quote():
    client = app.app.test_client()

    response = client.get("/quote")
    data = response.data.decode('utf-8')

    assert response.status_code == 200
    assert data in app.quotes