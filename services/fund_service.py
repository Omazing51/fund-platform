from repositories.fund_repository import FundRepository

class FundService:
    def __init__(self):
        self.repository = FundRepository()

    def get_fund_by_id(self, fund_id: str):
        fund = self.repository.get_fund_by_id(fund_id)
        if not fund:
            raise ValueError(f"No se encontro el fondo {fund_id}")
        return fund

    def get_all_funds(self):
        funds = self.repository.get_all_funds()
        return funds
