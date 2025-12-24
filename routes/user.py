from fastapi import APIRouter
from config.db import conn
from models.index import users
from schemas.index import User
user = APIRouter()

@user.get("/")
async def read_data():
    return conn.execute(users.select()).fetchall()

@user.get("/{id}")
async def read_user(id: int):
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.post("/")
async def Write_user(user: User):
     conn.execute(users.insert().values(
        full_name = user.full_name,
        email = user.email,
        password_hash = user.password_hash,
        created_at = user.created_at
    ))
     return conn.execute(users.select()).fetchall()

@user.put("/{id}")
async def update_user(id: int, user: User):
    conn.execute(users.update(
        full_name = user.full_name,
        email = user.email,
        password_hash = user.password_hash,
        created_at = user.created_at
    ).where(users.c.id == id))
    return conn.execute(users.select().where(users.c.id == id)).fetchall()

@user.delete("/{id}")
async def delete_user(id: int):
    conn.execute(users.delete().where(users.c.id == id))
    return conn.execute(users.select()).fetchall()