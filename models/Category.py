from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, TIMESTAMP, Enum
from config.db import meta

catagories = Table(
    "catagories",meta,
    Column('id',Integer,primary_key=True),
    Column('user_id',Integer),
    Column('name',String(100)),
    Column('type',Enum('income', 'expense')), # income or expense
    Column('created_at',TIMESTAMP(True))
    )