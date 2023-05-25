from models.user import User
from sqlalchemy.orm import Session
from dto import user


def create_user(data: user.User, db):
    user_create = User(name=data.user)

    try:
        db.add(user)
        db.commit()
        db.refresh(user)
    except Exception as e:
        print(e)

    return user_create


def get_user(user_id: int, db: Session):
    return db.query(User).filter(User.id == user_id).first()


def update_user(data: user.User, db: Session, user_id: int):
    user_update = db.query(User).filter(User.id == user_id).first()
    user_update.name = data.name

    db.add(user_update)
    db.commit()
    db.refresh(user_update)

    return user_update


def delete_user(user_id: int, db: Session):
    user_delete = db.query(User).filter(User.id == user_id).first()
    db.delete(user_delete)

    db.commit()
    return user_delete
