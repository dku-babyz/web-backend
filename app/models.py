
from sqlalchemy import Boolean, Column, Integer, String
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    client_id = Column(String(128), unique=True, index=True)
    is_active = Column(Boolean, default=True)

class AlterWord(Base):
    __tablename__ = "alter_word"

    id = Column(Integer, primary_key=True, index=True)
    original_word = Column(String(255))
    alter_word = Column(String(255))
    site_url = Column(String(255))
    client_id = Column(String(128), index=True)