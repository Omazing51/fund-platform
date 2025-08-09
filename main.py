from fastapi import FastAPI
from database.db import create_tables


app = FastAPI()

create_tables()