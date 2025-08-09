from decimal import Decimal
from core.exceptions import AppException

class SubscriptionService:
    def __init__(self, repository):
        self.repo = repository
        self.DEFAULT_ACCOUNT_ID = "DEFAULT_ACCOUNT"

    def subscribe(self, fund_id: str, notification_method: str):
        fund = self.repo.get_fund(fund_id)
        if not fund:
            raise AppException(f"Fondo con ID {fund_id} no existe")

        account = self.repo.get_account(self.DEFAULT_ACCOUNT_ID)
        if not account:
            raise AppException("Cuenta no encontrada")

        balance = Decimal(account["Balance"])
        min_amount = Decimal(fund["MinAmount"])

        if balance < min_amount:
            raise AppException(f"No tiene saldo disponible para vincularse al fondo {fund['Name']}")

        subscription = self.repo.create_subscription(self.DEFAULT_ACCOUNT_ID, fund_id)

        new_balance = balance - min_amount
        self.repo.update_account_balance(self.DEFAULT_ACCOUNT_ID, new_balance)

        self.repo.create_transaction(self.DEFAULT_ACCOUNT_ID, fund_id, min_amount, "APERTURA")

        if notification_method == "email":
            print(f"Enviando email a {account['Email']} confirmando suscripción")
        else:
            print(f"Enviando SMS a {account['Phone']} confirmando suscripción")

        return subscription
