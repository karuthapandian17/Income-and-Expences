from fastapi import FastAPI
from routes.index import user, category
app = FastAPI()

app.include_router(user, prefix="/user", tags=["user"])
app.include_router(category, prefix="/category", tags=["category"])