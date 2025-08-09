from fastapi import APIRouter
from models.unsubscribe import UnsubscribeRequest
from repositories.subscription_repository import SubscriptionRepository
from services.subscription_service import SubscriptionService

router = APIRouter()

repo = SubscriptionRepository()
service = SubscriptionService(repo)

@router.delete("/subscriptions")
def unsubscribe(request: UnsubscribeRequest):
    return service.unsubscribe(request.FundId)
