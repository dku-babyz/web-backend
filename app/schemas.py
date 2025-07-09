
from pydantic import BaseModel

class UserBase(BaseModel):
    client_id: str

class UserCreate(BaseModel):
    client_id: str

class User(UserBase):
    id: int
    is_active: bool

    class Config:
        from_attributes = True
