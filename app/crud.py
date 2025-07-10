
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext
import redis
import json

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_user(db: Session, client_id: str):
    return db.query(models.User).filter(models.User.client_id == client_id).first()

def get_user_by_client_id(db: Session, client_id: str):
    return db.query(models.User).filter(models.User.client_id == client_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(client_id=user.client_id)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_alter_word(db: Session, client_id: str, original_word: str):
    return db.query(models.AlterWord).filter(models.AlterWord.client_id == client_id, models.AlterWord.original_word == original_word).first()

def create_alter_word(db: Session, client_id: str, original_word: str):
    db_alter_word = models.AlterWord(
        client_id=client_id,
        original_word=original_word,
        alter_word='대체단어',
        site_url='<UNK>'
    )
    #TODO: AI 파트 연동 필요
    db.add(db_alter_word)
    db.commit()
    db.refresh(db_alter_word)
    return db_alter_word

def get_alter_word_from_cache(redis_db: redis.Redis, client_id: str, original_word: str):
    key = f"alter_word:{client_id}:{original_word}"
    cached_word = redis_db.get(key)
    if cached_word:
        return json.loads(cached_word)
    return None

def set_alter_word_to_cache(redis_db: redis.Redis, client_id: str, original_word: str, alter_word: schemas.AlterWord):
    key = f"alter_word:{client_id}:{original_word}"
    redis_db.set(key, json.dumps(alter_word.dict()))

def get_alter_image(db: Session, client_id: str, original_image_url: str):
    return db.query(models.AlterImage).filter(models.AlterImage.client_id == client_id, models.AlterImage.original_image_url == original_image_url).first()

def create_alter_image(db: Session, client_id: str, site_url: str, original_image: any):
    # TODO: AI 파트 연동 필요
    db_alter_image = models.AlterImage(
        client_id=client_id,
        original_image_url=original_image.filename,
        alter_image_url="https://picsum.photos/200/300",
        site_url=site_url
    )
    db.add(db_alter_image)
    db.commit()
    db.refresh(db_alter_image)
    return db_alter_image

def get_alter_image_from_cache(redis_db: redis.Redis, client_id: str, original_image_url: str):
    key = f"alter_image:{client_id}:{original_image_url}"
    cached_image = redis_db.get(key)
    if cached_image:
        return json.loads(cached_image)
    return None

def set_alter_image_to_cache(redis_db: redis.Redis, client_id: str, original_image_url: str, alter_image: schemas.AlterImage):
    key = f"alter_image:{client_id}:{original_image_url}"
    redis_db.set(key, json.dumps(alter_image.dict()))