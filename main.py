from fastapi import FastAPI
from database.db import create_tables
from core.exceptions import AppException, app_exception_handler
from routes.account_routes import router as account_router

app = FastAPI()

app.add_exception_handler(AppException, app_exception_handler)

create_tables()

app.include_router(account_router, prefix="/accounts", tags=["Accounts"])

@app.get("/")
def root():
    return {"message": "API Running"}