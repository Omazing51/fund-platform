from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_subscribe_and_unsubscribe_success():
    # Suscribir al fondo
    payload = {"FundId": "1", "NotificationMethod": "email"}
    response = client.post("/subscriptions", json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "SubscriptionId" in data
    assert data["FundId"] == "1"
    assert data["AccountId"] == "DEFAULT_ACCOUNT"

    # Retirarse del fondo
    unsubscribe_payload = {"FundId": "1"}
    response_unsub = client.request("DELETE", "/subscriptions", json=unsubscribe_payload)
    assert response_unsub.status_code == 200
    data_unsub = response_unsub.json()
    assert "message" in data_unsub
    assert f"Se eliminó la suscripción al fondo 1" in data_unsub["message"]
    assert "Balance" in data_unsub
    assert isinstance(data_unsub["Balance"], float)
