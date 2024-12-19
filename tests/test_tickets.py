from fastapi.testclient import TestClient
from src.main import app


client = TestClient(app)


async def test_create_ticket():
    response = client.post("/desk/", json={
        "user_email": "test@example.com",
        "user_name": "Test User",
        "message": "My issue"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "open"


async def test_list_tickets():
    response = client.post("/desk/", json={
        "user_email": "test@example.com",
        "user_name": "Test User",
        "message": "My issue"
    })
    assert response.status_code == 200
    assert response.json()["status"] == "open"

    stmp = client.get("/desk/")
    assert stmp.status_code == 200
    assert stmp.json()
