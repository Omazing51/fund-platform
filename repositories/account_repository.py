from database.db import dynamodb
from core.exceptions import AppException
from botocore.exceptions import ClientError

class AccountRepository:
    def __init__(self):
        self.table = dynamodb.Table("Accounts")

    def get_balance(self, account_id: str):
        try:
            response = self.table.get_item(Key={"AccountId": account_id})
            item = response.get("Item")
            if not item:
                return None
            return item["Balance"]
        except ClientError as e:
            raise AppException(f"Error al acceder a DynamoDB: {e.response['Error']['Message']}")
