from decimal import Decimal
from datetime import datetime, timezone
from database.db import dynamodb

def iso_now():
    return datetime.now(timezone.utc).isoformat()

def seed_funds():
    table = dynamodb.Table("Funds")
    funds = [
        {"FundId": "1", "Name": "FPV_EL CLIENTE_RECAUDADORA", "MinAmount": Decimal(75000), "Category": "FPV"},
        {"FundId": "2", "Name": "FPV_EL CLIENTE_ECOPETROL", "MinAmount": Decimal(125000), "Category": "FPV"},
        {"FundId": "3", "Name": "DEUDAPRIVADA", "MinAmount": Decimal(50000), "Category": "FIC"},
        {"FundId": "4", "Name": "FDO-ACCIONES", "MinAmount": Decimal(250000), "Category": "FIC"},
        {"FundId": "5", "Name": "FPV_EL CLIENTE_DINAMICA", "MinAmount": Decimal(100000), "Category": "FPV"},
    ]
    for fund in funds:
        table.put_item(Item=fund)
    print("Fondos inicializados.")

def seed_account():
    table = dynamodb.Table("Accounts")
    account = {
        "AccountId": "DEFAULT_ACCOUNT",
        "Balance": Decimal(500000),
        "Email": "omaryesid1215@gmail.com",
        "Phone": "+573052463288",
        "CreatedAt": iso_now()
    }
    table.put_item(Item=account)
    print("Cuenta inicial creada con saldo COP $500.000.")

if __name__ == "__main__":
    seed_funds()
    seed_account()
    print("Seed completado.")
