from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health():
    assert client.get("/health").status_code == 200

def test_memory_recall():
    client.post("/v1/run", json={"value": "first"})
    response = client.post("/v1/run", json={"value": "second"})
    data = response.json()
    assert data["recall"][0]["text"] == "second"
