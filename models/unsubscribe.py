from pydantic import BaseModel

class UnsubscribeRequest(BaseModel):
    FundId: str
