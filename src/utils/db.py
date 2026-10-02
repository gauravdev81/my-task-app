# here we'll be configuring DB connections.

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from src.utils.settings import settings

# Base is responsible to connect the models to the actual database. 
# It is a class that maintains a catalog of classes and tables relative to that database.
Base = declarative_base()

engine = create_engine(url=settings.DB_CONNECTION)

LocalSession = sessionmaker(bind=engine)

def get_db():
    session = LocalSession()
    try:
        yield session
        
    finally:
        session.close()