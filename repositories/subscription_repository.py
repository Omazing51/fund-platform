import uuid
from datetime import datetime, timezone
from decimal import Decimal
from database.db import dynamodb

class SubscriptionRepository:
    def __init__(self):
        self.subscriptions_table = dynamodb.Table("Subscriptions")
        self.funds_table = dynamodb.Table("Funds")
        self.accounts_table = dynamodb.Table("Accounts")
        self.transactions_table = dynamodb.Table("Transactions")

    def get_fund(self, fund_id: str):
        resp = self.funds_table.get_item(Key={"FundId": fund_id})
        return resp.get("Item")

    def get_account(self, account_id: str):
        resp = self.accounts_table.get_item(Key={"AccountId": account_id})
        return resp.get("Item")

    def create_subscription(self, account_id: str, fund_id: str):
        sub_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        self.subscriptions_table.put_item(Item={
            "SubscriptionId": sub_id,
            "AccountId": account_id,
            "FundId": fund_id,
            "CreatedAt": now
        })
        return {"SubscriptionId": sub_id, "AccountId": account_id, "FundId": fund_id, "CreatedAt": now}

    def update_account_balance(self, account_id: str, new_balance: Decimal):
        self.accounts_table.update_item(
            Key={"AccountId": account_id},
            UpdateExpression="SET Balance = :b",
            ExpressionAttributeValues={":b": new_balance}
        )

    def create_transaction(self, account_id: str, fund_id: str, amount: Decimal, transaction_type: str):
        txn_id = str(uuid.uuid4())
        now = datetime.now(timezone.utc).isoformat()
        self.transactions_table.put_item(Item={
            "TransactionId": txn_id,
            "AccountId": account_id,
            "FundId": fund_id,
            "Amount": amount,
            "Type": transaction_type,
            "CreatedAt": now
        })
