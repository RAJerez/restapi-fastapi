from datetime import datetime
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship

from db.database import Base

class User(Base):
    __tablename__ = "user"
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True)
    password = Column(String)
    name = Column(String)
    lastname = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True)
    create_user = Column(DateTime, default=datetime.now(), onupdate=datetime.now())
    state = Column(Boolean, default=False)
    sales = relationship("Sales", backref="user", cascade="delete,merge")
    
class Sales(Base):
    __tablename__ = "sales"
    sale_id = Column(Integer, primary_key=True, autoincrement=True)
    user_id = Column(Integer, ForeignKey("user.user_id", ondelete="CASCADE"))
    sale = Column(Integer)
    sales_products = Column(Integer)
        
