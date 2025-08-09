from fastapi import FastAPI
from database.db import create_tables
from core.exceptions import AppException, app_exception_handler

app = FastAPI()

app.add_exception_handler(AppException, app_exception_handler)

create_tables()

@app.get("/")
def root():
    return {"message": "API Running"}