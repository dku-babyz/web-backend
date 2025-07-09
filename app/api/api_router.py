
from fastapi import APIRouter
from app.api.endpoints import users, words

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(words.router, prefix="/words", tags=["words"])
