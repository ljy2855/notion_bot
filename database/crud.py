from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_key(db: Session, key: str):
    return db.query(models.User).filter(models.User.key == key).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(key=user.key)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def get_group_by_page_id(db: Session, page_id:str):
    return db.query(models.Group).filter(models.Group.page_id == page_id).first()

def create_group(db: Session, group: schemas.GroupCreate):
    db_group = models.Group(page_id=group.page_id,title=group.title)
    db.add(db_group)
    db.commit()
    db.refresh(db_group)
    return db_group

# def get_items(db: Session, skip: int = 0, limit: int = 100):
#     return db.query(models.Item).offset(skip).limit(limit).all()


# def create_user_item(db: Session, item: schemas.ItemCreate, user_id: int):
#     db_item = models.Item(**item.dict(), owner_id=user_id)
#     db.add(db_item)
#     db.commit()
#     db.refresh(db_item)
#     return db_item