from pydantic import BaseModel

class User(BaseModel):
    full_name: str
    email: str
    password_hash: str
    created_at: str

  