from pydantic import BaseModel
from datetime import datetime
from decimal import Decimal

class Transaction(BaseModel):
    FundId: str
    Category: str
    FundId: str
    MinAmount: Decimal
    Name: str
    
    class Config:
        from_attributes = True
	
	
	