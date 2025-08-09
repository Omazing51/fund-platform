from fastapi import APIRouter, HTTPException
from repositories.account_repository import AccountRepository
from services.account_service import AccountService
from models.account import AccountBalanceResponse

router = APIRouter()

account_repository = AccountRepository()
account_service = AccountService(account_repository)

@router.get("/balance", response_model=AccountBalanceResponse)
def get_balance():
    account_id = "DEFAULT_ACCOUNT"  
    balance = account_service.get_balance(account_id)
    if balance is None:
        raise HTTPException(status_code=404, detail="Cuenta no encontrada")
    return {"Balance": balance}
