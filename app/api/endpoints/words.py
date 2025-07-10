from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import redis

from app import crud, schemas
from app.database import get_db, get_redis_db

router = APIRouter()

@router.post("/", response_model=schemas.AlterWord)
def create_alter_words(alter_word: schemas.AlterWordCreate, db: Session = Depends(get_db), redis_db: redis.Redis = Depends(get_redis_db)):    cached_word = crud.get_alter_word_from_cache(redis_db, alter_word.client_id, alter_word.original_word)
    if cached_word:
        return cached_word
    
    db_alter_word = crud.create_alter_word(db, client_id=alter_word.client_id, original_word=alter_word.original_word)
    crud.set_alter_word_to_cache(redis_db, alter_word.client_id, alter_word.original_word, db_alter_word)
    return db_alter_word
