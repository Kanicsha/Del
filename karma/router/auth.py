from pydantic import BaseModel
from karma import database, oauth2, operations,model
from ..model import User
from fastapi import APIRouter, Depends, status, HTTPException, Response
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session

from karma import model, oauth2
from ..database import get_db

# seperates the user, posts in swagger UI
router=APIRouter(tags=['Authentication'])

@router.post("/login")
def login_user(user_credentials:OAuth2PasswordRequestForm=Depends(),db: Session = Depends(get_db)):

    #in form_data
    user = db.query(model.User).filter(
       model.User.name == user_credentials.username).first()
    print(user_credentials.username)
    if not user :
        print("not found")
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED
                            ,detail=f"User name or password is incorrect"
                            )
    access_token = oauth2.create_access_token(data={"id":user.id})
    print("Access token:: ",access_token)
    return {"access_token": access_token, "token_type": "bearer"}


@router.post("/refresh-token")
async def refresh_token(token: str = Depends(oauth2.oauth2_scheme)):
    # Refresh the token
    new_token = oauth2.create_access_token(data={"id": token.id})
    return {"access_token": new_token}




