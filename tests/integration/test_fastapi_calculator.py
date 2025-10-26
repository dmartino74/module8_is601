import pytest
from fastapi.testclient import TestClient
from main import app

@pytest.fixture
def client():
    with TestClient(app) as client:
        yield client

def test_add_api(client):
    response = client.post('/add', json={'a': 10, 'b': 5})
    assert response.status_code == 200
    assert response.json()['result'] == 15

def test_subtract_api(client):
    response = client.post('/subtract', json={'a': 20, 'b': 8})
    assert response.status_code == 200
    assert response.json()['result'] == 12

def test_multiply_api(client):
    response = client.post('/multiply', json={'a': 6, 'b': 7})
    assert response.status_code == 200
    assert response.json()['result'] == 42

def test_divide_api(client):
    response = client.post('/divide', json={'a': 10, 'b': 2})
    assert response.status_code == 200
    assert response.json()['result'] == 5.0

def test_divide_by_zero_api(client):
    response = client.post('/divide', json={'a': 10, 'b': 0})
    assert response.status_code == 400
    assert 'error' in response.json()
    assert "Cannot divide by zero!" in response.json()['error']

def test_invalid_input_api(client):
    response = client.post('/add', json={'a': 'abc', 'b': 5})
    assert response.status_code == 400  # Your app returns 400 for manual validation
    assert 'error' in response.json()
    assert "Input should be a valid number" in response.json()['error']
