from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, Enum
from config.db import meta

users = Table(
    "users",meta,
    Column('id', Integer, primary_key=True),
    Column('full_name', String(100)),
    Column('email', String(100), unique=True),
    Column('password_hash', String(100)),
    Column('created_at', TIMESTAMP(True))
)

