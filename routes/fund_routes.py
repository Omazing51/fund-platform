from fastapi import APIRouter, HTTPException
from services.fund_service import FundService

router = APIRouter()
fund_service = FundService()

@router.get("/funds")
def get_all_funds():
    try:
        funds = fund_service.get_all_funds()
        return {"data": funds}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/funds/{fund_id}")
def get_fund_by_id(fund_id: str):
    try:
        fund = fund_service.get_fund_by_id(fund_id)
        return {"data": fund}
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
