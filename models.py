#models.py is for declaring what your database tables look like — it's where you define your tables and columns.
from database import Base
from sqlalchemy import Column, Integer, String , ForeignKey
from sqlalchemy.orm import relationship

class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    phone_number = Column(String)