
from pydantic import BaseModel

class UserBase(BaseModel):
    client_id: str

class UserCreate(BaseModel):
    client_id: str

class User(UserBase):
    id: int
    client_id: str
    is_active: bool

    class Config:
        from_attributes = True


class AlterWordBase(BaseModel):
    original_word: str
    site_url: str
    client_id: str

class AlterWordCreate(AlterWordBase):
    original_word: str
    site_url: str
    client_id: str

class AlterWord(AlterWordBase):
    id: int
    original_word: str
    alter_word: str
    site_url: str
    client_id: str

    def dict(self, **kwargs):
        return self.model_dump(**kwargs)

    class Config:
        from_attributes = True


class AlterImageBase(BaseModel):
    original_image_url: str
    site_url: str
    client_id: str

class AlterImageCreate(AlterImageBase):
    original_image_url: str
    site_url: str
    client_id: str

class AlterImage(AlterImageBase):
    id: int
    original_image_url: str
    alter_image_url: str
    site_url: str
    client_id: str

    def dict(self, **kwargs):
        return self.model_dump(**kwargs)

    class Config:
        from_attributes = True