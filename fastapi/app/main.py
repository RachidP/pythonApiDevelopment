
from multiprocessing import synchronize
import time
from fastapi import Depends, FastAPI, Response, status, HTTPException
from fastapi.params import Body

import psycopg
from psycopg.rows import dict_row
from . import models, schemas, utils
from .database import engine, get_db
from sqlalchemy.orm import Session
from .routers import post, user, auth

models.Base.metadata.create_all(bind=engine)
app = FastAPI()


while True:
    try:
        conn = psycopg.connect(
            host='localhost', dbname='fastapi', user='postgres', password='admin', row_factory=dict_row, autocommit=True)
        cursor = conn.cursor()
        print("Database connection was succesfull")
        break
    except Exception as error:
        print("connecting to database failed")
        print("Error: ", error)
        time.sleep(5)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)


@app.get("/")
def root():
    return {"message": "Hello World"}
