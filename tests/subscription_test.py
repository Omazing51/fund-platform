from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_subscribe_success():
    payload = {"FundId": "1", "NotificationMethod": "email"}
    response = client.post("/subscriptions", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "SubscriptionId" in data
    assert data["FundId"] == "1"
    assert data["AccountId"] == "DEFAULT_ACCOUNT"
