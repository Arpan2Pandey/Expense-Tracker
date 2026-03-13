from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "postgresql://postgres:1234@localhost/expense_tracker"

engine = create_engine(DATABASE_URL)  #connects Python to PostgreSQL

SessionLocal = sessionmaker(bind=engine) #creates database sessions

Base = declarative_base() #parent class for database models

