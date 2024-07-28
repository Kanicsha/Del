from fastapi import FastAPI
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2

DB_NAME = "postgres"
DB_USER = "postgres"
DB_PASS = "postgres123"
DB_HOST = "localhost"
DB_PORT = "5432"

def get_db():
    db=session()
    try:
        yield db
    except Exception as error:
        print("Error in connecting to db:",error)
        db.close()

fake_db_users=[
    {'id':12,'name':'kani','karmaPoints':10,'password':'paos'},
    {'id':32,'name':'koh','karmaPoints':120,'password':'pass'}
]

#mysql://user:password@localhost/karma
database_url= "postgresql://postgres:postgres123@localhost:5432/postgres"
db_engine=create_engine(database_url)
session=sessionmaker(bind=db_engine,autoflush=False)

Base=declarative_base()

session_op=session()

