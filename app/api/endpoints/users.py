
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_client_id(db, client_id=user.client_id)
    if db_user:
        raise HTTPException(status_code=400, detail="Client already registered")
    return crud.create_user(db=db, user=user)

@router.get("/", response_model=List[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@router.get("/{client_id}", response_model=schemas.User)
def read_user(client_id: str, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, client_id=client_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user
