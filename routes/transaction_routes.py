from fastapi import APIRouter, Query
from repositories.transaction_repository import TransactionRepository
from services.transaction_service import TransactionService

router = APIRouter()
repo = TransactionRepository()
service = TransactionService(repo)

@router.get("/transactions")
def get_recent_transactions(limit: int = Query(10, ge=1, le=50)):
    return service.get_recent_transactions(limit)
