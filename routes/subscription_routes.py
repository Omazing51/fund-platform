from fastapi import APIRouter
from models.subscription import SubscriptionCreate, SubscriptionResponse
from repositories.subscription_repository import SubscriptionRepository
from services.subscription_service import SubscriptionService

router = APIRouter()

repo = SubscriptionRepository()
service = SubscriptionService(repo)

@router.post("/subscriptions", response_model=SubscriptionResponse)
def subscribe_to_fund(payload: SubscriptionCreate):
    return service.subscribe(payload.FundId, payload.NotificationMethod)

@router.get("/subscriptions")
def get_subscriptions():
    subs = repo.subscriptions_table.scan().get("Items", [])
    return {"data": subs}
