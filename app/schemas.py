from pydantic import BaseModel

from typing import Optional
from datetime import datetime

class User(BaseModel):
    id: int
    name: str
    lastname: str
    address: Optional[str]
    phone_number: int
    email: str
    create_user: datetime = datetime.now()

class UserId(BaseModel):
    id:int