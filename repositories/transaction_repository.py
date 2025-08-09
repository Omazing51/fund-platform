from database.db import dynamodb
import uuid
from datetime import datetime, timezone
from decimal import Decimal

def iso_now():
    return datetime.now(timezone.utc).isoformat()

class TransactionRepository:
    def __init__(self):
        self.table = dynamodb.Table("Transactions")

    def create_transaction(self, account_id: str, fund_id: str, amount: float, type_: str):
        transaction_id = str(uuid.uuid4())
        self.table.put_item(Item={
            "TransactionId": transaction_id,
            "AccountId": account_id,
            "FundId": fund_id,
            "Amount": Decimal(str(amount)),
            "Type": type_,
            "CreatedAt": iso_now()
        })
        return transaction_id

    def get_recent_transactions(self, account_id: str, limit: int = 10):
        resp = self.table.scan(
            FilterExpression="AccountId = :acc",
            ExpressionAttributeValues={":acc": account_id}
        )
        items = sorted(resp.get("Items", []), key=lambda x: x["CreatedAt"], reverse=True)
        return items[:limit]
