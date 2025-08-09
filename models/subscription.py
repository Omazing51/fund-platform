from pydantic import BaseModel, Field
from datetime import datetime
from typing import Literal

class SubscriptionCreate(BaseModel):
    FundId: str = Field(..., description="ID del fondo")
    NotificationMethod: Literal["email", "sms"] = Field(..., description="Método de notificación")

class SubscriptionResponse(BaseModel):
    SubscriptionId: str
    FundId: str
    AccountId: str
    CreatedAt: datetime
