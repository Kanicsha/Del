
import datetime
from fastapi import Depends, HTTPException,status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError,jwt
from sqlalchemy import null
from sqlalchemy.orm import Session
from karma import database, model


SecretKey="09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
Algorithm="HS256"
access_token_expire_time=15 #in minutes


#oauth2_scheme is an instance of Oauth2PasswordBearer class .
oauth2_scheme=OAuth2PasswordBearer(tokenUrl="login") 
 #the url where the username and password is sent by the front end to ./token (relative url )


def create_access_token(data:dict):
    to_encode=data.copy()
    expire_time=datetime.datetime.now()+ datetime.timedelta(minutes=access_token_expire_time)

    to_encode.update({"exp":expire_time})

    encoded_jwt=jwt.encode(to_encode,SecretKey,algorithm=Algorithm)
    print("encoded jwt:: ",encoded_jwt)

    return encoded_jwt


def authenticate_user(token:str):
        try:
                payload=jwt.decode(token=token,key=SecretKey,algorithms=Algorithm)
                id:int=payload.get("id")
                if id is null:
                        print("NULL id")
                        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        
        
        except JWTError:
                        print("JwTERROR")
                        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
        return id

def get_current_user(token: str = Depends(oauth2_scheme), db: Session = Depends(database.get_db)):
        id=authenticate_user(token)
        user=db.query(model.User).filter(model.User.id==id).first()
        print("Inside Current User")
        return user



# def authenticate_user(token:str=Depends(oauth2_scheme),db:Session=Depends(database.get_db)):
#         token_id_data=verify_token(token)
#         user=db.query(model.User).filter(model.User.id==token_id_data.id).first()
#         return user
        
