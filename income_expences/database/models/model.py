from pydantic import BaseModel

class UserModel(BaseModel):
    id: int
    full_name: str
    email: str
    password_hash: str
    created_at: str

class CategoryModel(BaseModel):
    id: int
    user_id: int
    name: str
    type: str  # 'income' or 'expense'
    created_at: str    