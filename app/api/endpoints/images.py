from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
import redis

from app import crud, schemas
from app.database import get_db, get_redis_db

router = APIRouter()

@router.post("/", response_model=schemas.AlterImage)
def create_alter_images(client_id: str, site_url: str, original_image: UploadFile = File(...), db: Session = Depends(get_db), redis_db: redis.Redis = Depends(get_redis_db)):
    cached_image = crud.get_alter_image_from_cache(redis_db, client_id, original_image.filename)
    if cached_image:
        return cached_image

    db_alter_image = crud.create_alter_image(db, client_id=client_id, site_url=site_url, original_image=original_image)
    crud.set_alter_image_to_cache(redis_db, client_id, original_image.filename, db_alter_image)
    return db_alter_image
