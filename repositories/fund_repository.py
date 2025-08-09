from database.db import dynamodb

class FundRepository:
    def __init__(self):
        self.table = dynamodb.Table("Funds")

    def get_fund_by_id(self, fund_id: str):
        response = self.table.get_item(Key={"FundId": fund_id})
        return response.get("Item")
