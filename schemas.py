# The schemas.py file is for defining the data models that will be used for request and response validation in your API endpoints. These models are typically defined using Pydantic, which allows you to specify the structure of the data and perform validation automatically.
from pydantic import BaseModel 
from typing import Optional


class ContactCreate(BaseModel):
    name: str
    email: str
    phone_number: str


class ContactUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None
    phone_number: Optional[str] = None


class ContactResponse(BaseModel):
    id: int
    name: str
    email: str
    phone_number: str

    class Config:
        from_attributes = True