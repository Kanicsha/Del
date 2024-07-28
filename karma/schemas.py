from pydantic import BaseModel,config
#contain pydantic models which define the response or request structure
class Task(BaseModel):
    name:str|None="no name"
    description:str|None="Empty"
    karmaPoints:int|None=0

class TaskResponse(BaseModel):
    name:str
    karmaPoints:int

class UserResponse(BaseModel):
    name:str
    karmaPoints:int

class User(BaseModel):
      name:str
      karmaPoints:int|None=100
      password:str
      class Config:
        arbitrary_types_allowed = True
 
class Token(BaseModel):
    name:str
    id:int

class TokenData(BaseModel):
    name:str
class Token_id(BaseModel):
    id:int

class Transaction(BaseModel):
    spent:int
    available:int
    bonus:int|None=0
    mentor:int
    mentee:int

