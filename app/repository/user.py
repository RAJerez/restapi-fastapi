from sqlalchemy.orm import Session

from db import models

def create_user(user, db:Session):
    user = user.dict()
    new_user = models.User(
    username=user["username"],
    password=user["password"],
    name=user["name"],
    lastname=user["lastname"],
    address=user["address"],
    phone_number=user["phone_number"],
    email=user["email"]
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
def get_users(db:Session):
    data = db.query(models.User).all()
    return data
    
def get_user(user_id, db:Session):
    target_user = db.query(models.User).filter(models.User.user_id == user_id).first()
    if not target_user:
        return {"response": "User not found."}
    return target_user

def delete_user(user_id, db:Session):
    target_user = db.query(models.User).filter(models.User.user_id == user_id)
    if not target_user.first():
        return {"response": "User not found."}
    target_user.delete(synchronize_session=False)
    db.commit()
    return {"response": "User deleted successfully"}

def update_user(user_id, updateUser, db:Session):
    target_user = db.query(models.User).filter(models.User.user_id == user_id)
    if not target_user.first():
        return {"response": "User not found."}
    target_user.update(updateUser.dict(exclude_unset=True))
    db.commit()
    return {"response": "User updated successfully"}