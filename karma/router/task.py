
from typing import List
from fastapi import status, HTTPException, Depends, APIRouter
from karma import database, oauth2, schemas
from . import User, Task
from sqlalchemy.orm import Session


router = APIRouter(
    prefix="/tasks",
    tags=['Users']
)

@router.post("/add")
def add_task(task:schemas.Task,db:Session=Depends(database.get_db),get_current_user=Depends(oauth2.get_current_user)):
    user:User=get_current_user
    newTask=Task(name=task.title,description=task.description,karmaPoints=task.karmaPoints,owner_id=user.id)
    db.add(newTask)
    db.commit()
    db.refresh(newTask)
    return{
        "task":"Task created successfully",
        "desc":newTask
    }


@router.get("/",status_code=status.HTTP_200_OK,response_model=List[schemas.Task])
def view_all_tasks_byOwner(db:Session=Depends(database.get_db)):
    print("hellp")
    tasks=db.query(Task).all()
    print(tasks)
    return tasks



@router.delete("/del/{title}",response_model=schemas.TaskResponse)
#get_current_user=Depends(oauth2.get_current_user)
def delete_task_by_title(title:str,db:Session=Depends(database.get_db),get_current_user=Depends(oauth2.get_current_user)):
    task=db.query(Task).filter(title==Task.name).first()
    print(task.name,task.description)
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f'Task with {title} was not found')
    if get_current_user.owner_id!=task.owner_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN,detail=f'This is not your post')
    db.delete(task)
    db.commit()
    db.refresh(task)
    return task

@router.get("/reserve/{taskName}",status_code=status.HTTP_226_IM_USED)
def reserve_task(taskName:str, db:Session=Depends(),current_user=Depends(oauth2.get_current_user)):
    user:User=current_user
    task=db.query(Task).filter(taskName==Task.name).first()
    task.owner_id
