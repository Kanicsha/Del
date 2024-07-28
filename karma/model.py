from sqlalchemy import TIMESTAMP, Column, ForeignKey,Index,Integer,String, text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from pydantic import BaseModel
from .database import Base
from time import timezone
#models are used to represent the structure of the tabel in database

#Base=declarative_base()

class User(Base):
    __tablename__="User"
    id=Column(Integer,primary_key=True,autoincrement=True)
    name=Column(String,nullable=False,unique=True)
    karmaPoints=Column(Integer,default=100)
    password = Column(String, nullable=False)
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'))
    
class Task(Base):
    __tablename__="Task"
    #cascade will make sure that when the user is deleted in the "User" table , the user's tasks get deleted automatically
    #ForeignKey("User.id",ondelete="CASCADE",nullable=False)
    owner_id=Column(Integer,ForeignKey("User.id",ondelete="CASCADE"),nullable=False)
    name=Column(String,nullable=False,unique=True,primary_key=True)
    karmaPoints=Column(Integer,default=100,nullable=False)
    description=Column(String(200))
    created_at=Column(TIMESTAMP(timezone=True),server_default=text('now()'))

class Transactions(Base):
      __tablename__='transaction'
      mentee=Column(Integer,ForeignKey("User.id",ondelete="CASCADE"),nullable=False)
      transaction_id=Column(Integer,primary_key=True)
      spent=Column(Integer)
      available=Column(Integer)
      bonus=Column(Integer,default=0)
      mentor=Column(Integer)

        
