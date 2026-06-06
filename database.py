# database.py is for declaring how to connect to your database — it's the foundation everything else sits on.
from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker , declarative_base

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:clement@localhost:5432/Contact"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db=SessionLocal()
    try:
        yield db
    finally:
        db.close()

def create_table():
    Base.metadata.create_all(bind=engine)