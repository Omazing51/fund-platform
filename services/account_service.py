class AccountService:
    def __init__(self, account_repository):
        self.account_repository = account_repository

    def get_balance(self, account_id: str):
        return self.account_repository.get_balance(account_id)
