import pytest
from flask import Flask

from import app

def test_disp_health():
    client = app.test_client()

    response = client.get("/health")
    data = response.data.decode()

    assert response.status_code == 200
    assert data == "healthy"

def test_disp_root_page():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200