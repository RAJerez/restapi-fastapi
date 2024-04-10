from fastapi import APIRouter, Depends
from schemas import User, UserId
from db.database import get_db
from sqlalchemy.orm import Session
from db import models

router = APIRouter(
    prefix="/user",
    tags=["Users"]
)

users = []

@router.get("/route1")
def ruta1():
    return {"mensaje": "Welcome to the API"}

@router.get("/")
def get_users(db:Session = Depends(get_db)):
    data = db.query(models.User).all()
    print(data)
    return users

@router.post("/")
def create_user(user: User):
    new_user = user.dict()
    users.append(new_user)
    return {"respons": "User created successfull"}

@router.get("/{user_id}")
def get_user(user_id:int):
    for user in users:
        if user["id"] == user_id:
            return {"user": user}
    return {"response": "User not found."}

@router.post("/get_user")
def get_user_2(user_id:UserId):
    for user in users:
        if user["id"] == user_id.id:
            return {"user": user}
    return {"response": "User not found."}

@router.delete("/{user_id}")
def delete_user(user_id:int):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users.pop(index)
            return {"response": "User deleted successfully"}
    return {"response": "User not found."}

@router.put("/{user_id}")
def update_user(user_id:int, updateUser:User):
    for index, user in enumerate(users):
        if user["id"] == user_id:
            users[index]["id"] = updateUser.dict()["id"]
            users[index]["name"] = updateUser.dict()["name"]
            users[index]["lastname"] = updateUser.dict()["lastname"]
            users[index]["address"] = updateUser.dict()["address"]
            users[index]["phone_number"] = updateUser.dict()["phone_number"]
            return {"response": "User updated successfully"}
    return {"response": "User not found."}