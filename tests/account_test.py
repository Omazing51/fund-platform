from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_get_balance_success(monkeypatch):
    from services.account_service import AccountService
    def mock_get_balance(self, account_id):
        return 500000
    monkeypatch.setattr(AccountService, "get_balance", mock_get_balance)

    response = client.get("/accounts/balance")
    assert response.status_code == 200
    assert response.json() == {"Balance": "500000"}

def test_get_balance_not_found(monkeypatch):
    from services.account_service import AccountService
    def mock_get_balance(self, account_id):
        return None
    monkeypatch.setattr(AccountService, "get_balance", mock_get_balance)

    response = client.get("/accounts/balance")
    assert response.status_code == 404
    assert response.json()["detail"] == "Cuenta no encontrada"
