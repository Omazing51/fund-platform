from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Transaction(BaseModel):
    TransactionId: str
    AccountId: str
    FundId: str
    Amount: Decimal
    Type: str
    CreatedAt: datetime

    class Config:
        from_attributes = True
