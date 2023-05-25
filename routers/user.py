from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import get_db

from services import user as UserService
from dto import user as UserDTO

router = APIRouter()


@router.post('/', tags=['user'])
async def create(user: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.create_user(user, db)


@router.get('/{user_id}', tags=['user'])
async def get(user_id: int = None, db: Session = Depends(get_db)):
    return UserService.get_user(user_id, db)


@router.put('/{user_id}', tags=['user'])
async def update(user_id: int = None, data: UserDTO.User = None, db: Session = Depends(get_db)):
    return UserService.update_user(data, db, user_id)


@router.delete('/{user_id}', tags=['user'])
async def delete(user_id: int, db: Session = Depends(get_db)):
    return UserService.delete_user(user_id, db)
