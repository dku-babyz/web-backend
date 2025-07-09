
from sqlalchemy.orm import Session
from . import models, schemas
from passlib.context import CryptContext

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