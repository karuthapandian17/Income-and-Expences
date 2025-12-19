from fastapi import FastAPI
from database import databaseConfigration

app=FastAPI()

databaseConfigration.create_database()

def get_db():
    connection = databaseConfigration.create_database()
    if connection is None:
        raise Exception(status_code=500, detail="Database connection error")

    try:
        yield connection
    finally:
        if connection and connection.is_connected():
            print("connected Successfully")

@app.get("/")
def home():
    return {"message":"Welcome to Income and Expense Tracker API"}                