from fastapi import FastAPI
from database.db import create_tables
from core.exceptions import AppException, app_exception_handler
from routes.account_routes import router as account_router
from routes.subscription_routes import router as subscription_router
from routes.unsubscribe_routes import router as unsubscribe_router
from routes.transaction_routes import router as transaction_router
from routes.fund_routes import router as fund_router

app = FastAPI()

app.add_exception_handler(AppException, app_exception_handler)

create_tables()

app.include_router(account_router, prefix="/accounts", tags=["Accounts"])

app.include_router(subscription_router)

app.include_router(unsubscribe_router)

app.include_router(transaction_router)

app.include_router(fund_router)

@app.get("/")
def root():
    return {"message": "API Running"}