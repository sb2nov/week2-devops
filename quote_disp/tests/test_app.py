from conftest import client

def test_should_status_code_ok(client):
    response = client.get('/')
    assert response.status_code == 200

def test_health_should_return_healthy(client):
    response = client.get('/health')
    data = response.data.decode()
    assert data == "healthy"