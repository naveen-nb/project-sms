from fastapi.testclient import TestClient
from ../main import app

client = TestClient(app)


def test_greeting():
    response = client.get("/api/greeting")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello from the backend!"}
