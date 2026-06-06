from models import Contact
from schemas import ContactCreate, ContactUpdate
from sqlalchemy.orm import Session


def get_all_contacts(db: Session):
    return db.query(Contact).all()


def get_contact_by_id(db: Session, contact_id: int):
    return db.query(Contact).filter(Contact.id == contact_id).first()
# The contact:ContactCreate is a Pydantic model that defines the structure of the data required to create a new contact. It includes fields for name, email, and phone number. The add_contact function takes a database session and a ContactCreate object as input, creates a new Contact instance, adds it to the database, commits the transaction, and returns the newly created contact.
def add_contact(db: Session, contact: ContactCreate):
    print("1. Received data from FastAPI")
    new_contact = Contact(
        name=contact.name,
        email=contact.email,
        phone_number=contact.phone_number
    )
    print("2. Created SQLAlchemy object")
    
    db.add(new_contact)
    print("3. Added to session")
    
    db.commit() 
    print("4. Committed to Database") # If it stops here, it's a Postgres error
    
    db.refresh(new_contact)
    print("5. Refreshed object")
    
    return new_contact



def update_contact(db: Session, contact_id: int, contact: ContactUpdate):
    existing_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not existing_contact:
        return None
    if contact.name is not None:
        existing_contact.name = contact.name
    if contact.email is not None:
        existing_contact.email = contact.email
    if contact.phone_number is not None:
        existing_contact.phone_number = contact.phone_number
    db.commit()
    db.refresh(existing_contact)
    return existing_contact


def delete_contact(db: Session, contact_id: int):
    existing_contact = db.query(Contact).filter(Contact.id == contact_id).first()
    if not existing_contact:
        return None
    db.delete(existing_contact)
    db.commit()
    return existing_contact


def search_contacts(db: Session, query: str):
    existing_contacts = db.query(Contact).filter(Contact.name.contains(query) | Contact.email.contains(query)).all()
    return existing_contacts
