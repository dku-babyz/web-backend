
from fastapi import FastAPI
from app.database import engine, Base
from app.api.api_router import api_router

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI backend!"}

app.include_router(api_router, prefix="/api/v1")
