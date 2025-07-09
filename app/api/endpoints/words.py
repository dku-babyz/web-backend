from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.AlterWord)
def create_alter_words(alter_word: schemas.AlterWordCreate, db: Session = Depends(get_db)):
    return crud.create_alter_word(db, client_id=alter_word.client_id, original_word=alter_word.original_word)