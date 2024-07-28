
from fastapi import Depends


from karma import model
from .database import session

from passlib.context import CryptContext


# def fetch_user(id:int, db: Session = Depends(get_db)):
#     db.query()

pwd_context = CryptContext(schemes=['bcrypt'], deprecated="auto")

def hash_pwd(password:model.User.password):
    hashed_password=pwd_context.hash(password)
    return hashed_password

def verify_pwd(plainPassword:str,hashedPassword:str):
    print(pwd_context.verify(plainPassword,hashedPassword))
    return pwd_context.verify(plainPassword,hashedPassword)


# def user_register(user:model.User):

    

