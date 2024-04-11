from pydantic import BaseModel

from typing import Optional
from datetime import datetime

class User(BaseModel):
    username: str
    password: str
    name: str
    lastname: str
    address: Optional[str]
    phone_number: str
    email: str
    create_user: datetime = datetime.now()
    
class UpdateUser(BaseModel):
    username:str = None
    password:str = None
    name:str = None
    lastname:str = None
    address:str = None
    phone_number:str = None
    email:str = None

class UserId(BaseModel):
    user_id:int
    
class ShowUser(BaseModel):
    username: str
    name: str
    lastname: str
    email: str
    class Config():
        orm_mode = True