from typing import List

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from db.database import get_db
from schemas import User, ShowUser, UpdateUser
from repository import user

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

@router.get("/", response_model=List[ShowUser])
def get_users(db:Session = Depends(get_db)):
    data = user.get_users(db)
    return data

@router.post("/")
def create_user(new_user: User, db:Session = Depends(get_db)):
    user.create_user(new_user, db)
    return {"respons": "User created successfull"}

@router.get("/{user_id}", response_model=ShowUser)
def get_user(user_id:int, db:Session = Depends(get_db)):
    target_user = user.get_user(user_id, db)
    return target_user

@router.delete("/{user_id}")
def delete_user(user_id:int, db:Session = Depends(get_db)):
    response = user.delete_user(user_id, db)
    return response

@router.patch("/{user_id}")
def update_user(user_id:int, updateUser:UpdateUser, db:Session = Depends(get_db)):
    response = user.update_user(user_id, updateUser, db)
    return response
