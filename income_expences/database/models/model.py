from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    full_name: str
    email: str
    password_hash: str
    created_at: str