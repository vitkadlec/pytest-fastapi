from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello, FastAPI!"}

def test_read_item():
    response = client.get("/items/42?q=test")
    assert response.status_code == 200
    assert response.json() == {"item_id": 42, "query": "test"}

def test_add_numbers():
    response = client.get("/add?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 8}

def test_multiply_numbers():
    response = client.get("/multiply?a=3&b=5")
    assert response.status_code == 200
    assert response.json() == {"result": 15}

def test_divide_numbers():
    response = client.get("/divide?a=10&b=2")
    assert response.status_code == 200
    assert response.json() == {"result": 5.0}

def test_divide_by_zero():
    response = client.get("/divide?a=10&b=0")
    assert response.status_code == 400
    assert response.json()["detail"] == "Division by zero is not allowed"