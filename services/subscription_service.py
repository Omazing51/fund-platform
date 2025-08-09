from decimal import Decimal
from core.exceptions import AppException
from services.notification_service import NotificationService  # nuevo import

class SubscriptionService:
    def __init__(self, repository):
        self.repo = repository
        self.DEFAULT_ACCOUNT_ID = "DEFAULT_ACCOUNT"
        self.notifier = NotificationService()

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

        mensaje = f"Te has suscrito al fondo {fund['Name']}."
        if notification_method == "email":
            self.notifier.send_email(
            to_email=account["Email"],
            subject="Confirmación de suscripción",
            body=mensaje
)
        else:
            self.notifier.send_sms(
                phone_number=account["Phone"],
                message=mensaje
            )

        return subscription

    def unsubscribe(self, fund_id: str):
        subscription = self.repo.get_subscription(self.DEFAULT_ACCOUNT_ID, fund_id)
        if not subscription:
            raise AppException(f"No está suscrito al fondo {fund_id}")

        fund = self.repo.get_fund(fund_id)
        if not fund:
            raise AppException(f"Fondo con ID {fund_id} no existe")

        min_amount = Decimal(fund["MinAmount"])

        self.repo.delete_subscription(subscription["SubscriptionId"])

        account = self.repo.get_account(self.DEFAULT_ACCOUNT_ID)
        new_balance = Decimal(account["Balance"]) + min_amount
        self.repo.update_account_balance(self.DEFAULT_ACCOUNT_ID, new_balance)

        self.repo.create_transaction(self.DEFAULT_ACCOUNT_ID, fund_id, min_amount, "CANCELACION")

        return {
            "message": f"Se eliminó la suscripción al fondo {fund_id}",
            "Balance": float(new_balance)
        }
