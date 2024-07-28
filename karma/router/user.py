
from fastapi import status, HTTPException, Depends, APIRouter

from karma import schemas,model,operations
from sqlalchemy.orm import Session
from ..database import get_db



router = APIRouter(
    prefix="/users",
    tags=['Users']
)

@router.post("/",response_model=schemas.UserResponse,status_code=status.HTTP_201_CREATED)
def signup(user_data:schemas.User,db:Session=Depends(get_db)):
    hashed_password=operations.hash_pwd(user_data.password)
    user_data.password=hashed_password
    new_user = model.User(name=user_data.name,karmaPoints=int(user_data.karmaPoints),password=user_data.password)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    print(new_user)
    return new_user


@router.get("/{id}",status_code=status.HTTP_302_FOUND,response_model=schemas.UserResponse)
def by_id(id:int,db:Session=Depends(get_db)):
    user=db.query(model.User).filter(id==model.User.id).first()
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'User with {id} was not found')
    return user



