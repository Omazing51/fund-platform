from boto3 import resource
from core.config import settings

dynamodb = resource(
    "dynamodb",
    aws_access_key_id=settings.aws_access_key_id,
    aws_secret_access_key=settings.aws_secret_access_key,
    region_name=settings.region_name
)

tables = [
     {
        "TableName": "Funds",
        "KeySchema": [
            {"AttributeName": "FundId", "KeyType": "HASH"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "FundId", "AttributeType": "S"}
        ],
        "BillingMode": "PAY_PER_REQUEST"
    },
    {
        "TableName": "Accounts",
        "KeySchema": [
            {"AttributeName": "AccountId", "KeyType": "HASH"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "AccountId", "AttributeType": "S"}
        ],
        "BillingMode": "PAY_PER_REQUEST"
    },
    {
        "TableName": "Subscriptions",
        "KeySchema": [
            {"AttributeName": "SubscriptionId", "KeyType": "HASH"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "SubscriptionId", "AttributeType": "S"},
            {"AttributeName": "AccountId", "AttributeType": "S"}
        ],
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "SubscriptionsByAccountIndex",
                "KeySchema": [
                    {"AttributeName": "AccountId", "KeyType": "HASH"}
                ],
                "Projection": {"ProjectionType": "ALL"}
            }
        ],
        "BillingMode": "PAY_PER_REQUEST"
    },
    {
        "TableName": "Transactions",
        "KeySchema": [
            {"AttributeName": "TransactionId", "KeyType": "HASH"}
        ],
        "AttributeDefinitions": [
            {"AttributeName": "TransactionId", "AttributeType": "S"},
            {"AttributeName": "AccountId", "AttributeType": "S"},
            {"AttributeName": "CreatedAt", "AttributeType": "S"}
        ],
        "GlobalSecondaryIndexes": [
            {
                "IndexName": "TransactionsByAccountIndex",
                "KeySchema": [
                    {"AttributeName": "AccountId", "KeyType": "HASH"},
                    {"AttributeName": "CreatedAt", "KeyType": "RANGE"}
                ],
                "Projection": {"ProjectionType": "ALL"}
            }
        ],
        "BillingMode": "PAY_PER_REQUEST"
    }
]

def create_tables():
    existing_tables = dynamodb.meta.client.list_tables()["TableNames"]
    for table_def in tables:
        if table_def["TableName"] not in existing_tables:
            print(f"Creando tabla: {table_def['TableName']}")
            dynamodb.create_table(**table_def)
        else:
            print(f"La tabla {table_def['TableName']} ya existe.")

if __name__ == "__main__":
    create_tables()