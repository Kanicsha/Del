
from fastapi import Depends, FastAPI
from karma.router import auth,user
from .database import db_engine,Base


# response model is the way you want to structure your response and may not include all the fields to be dislayed to the user
#dependency
Base.metadata.create_all(db_engine)


app=FastAPI()

app.include_router(auth.router)
#app.include_router(task.router)
app.include_router(user.router)

 #app.include_router(vote.router)


@app.get("/items")
def root():
    return {"token": "HEllo"}   




