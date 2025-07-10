
from fastapi import APIRouter
from app.api.endpoints import users, words, images

api_router = APIRouter()
api_router.include_router(users.router, prefix="/users", tags=["users"])
api_router.include_router(words.router, prefix="/words", tags=["words"])
api_router.include_router(images.router, prefix="/images", tags=["images"])
