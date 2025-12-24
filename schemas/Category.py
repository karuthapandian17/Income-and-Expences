from pydantic import BaseModel

class Category(BaseModel):
    user_id: int
    name: str
    type: str  # 'income' or 'expense'
    created_at: str  