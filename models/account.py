from pydantic import BaseModel
from decimal import Decimal
from datetime import datetime

class Account(BaseModel):
    AccountId: str
    Balance: Decimal
    Email: str
    Phone: str
    CreatedAt: datetime

class AccountBalanceResponse(BaseModel):
    Balance: Decimal
