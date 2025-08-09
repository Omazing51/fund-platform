from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_recent_transactions():
    response = client.get("/transactions?limit=5")
    assert response.status_code == 200
    data = response.json()
    assert isinstance(data, list)
    if data:
        first = data[0]
        assert "TransactionId" in first
        assert "AccountId" in first
        assert "FundId" in first
        assert "Amount" in first
        assert "Type" in first
        assert "CreatedAt" in first
