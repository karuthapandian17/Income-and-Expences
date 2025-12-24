from fastapi import APIRouter
from config.db import conn
from models.Category import catagories
from schemas.Category import Category

category = APIRouter()

@category.get("/")
async def read_data():
    return conn.execute(catagories.select()).fetchall()

@category.get("/{id}")
async def read_category(id: int):
    return conn.execute(catagories.select().where(catagories.c.id == id)).fetchall()

@category.post("/")
async def write_category(category: Category):
     conn.execute(catagories.insert().values(
        user_id = category.user_id,
        name =  category.name,
        type = category.type,
        created_at = category.created_at
    ))
     return conn.execute(catagories.select()).fetchall()

@category.put("/{id}")
async def update_category(id: int, category: Category):
    conn.execute(catagories.update().values(
        user_id = category.user_id,
        name =  category.name,
        type = category.type,
        created_at = category.created_at
    ).where(catagories.c.id == id))
    return conn.execute(catagories.select().where(catagories.c.id == id)).fetchall()

@category.delete("/{id}")
async def delete_category(id: int):
    conn.execute(catagories.delete().where(catagories.c.id == id))
    return conn.execute(catagories.select()).fetchall()