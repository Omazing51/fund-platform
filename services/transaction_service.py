class TransactionService:
    def __init__(self, repository):
        self.repo = repository
        self.DEFAULT_ACCOUNT_ID = "DEFAULT_ACCOUNT"

    def get_recent_transactions(self, limit: int = 10):
        return self.repo.get_recent_transactions(self.DEFAULT_ACCOUNT_ID, limit)
