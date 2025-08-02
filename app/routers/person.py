from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.models.Person import Person
from app.schemas.Person import PersonCreate, PersonOut
from app.database import SessionLocal


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/person", response_model=list[PersonOut])
def read_persons(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    persons = db.query(Person).offset(skip).limit(limit).all()
    return persons


@router.get("/person/{person_id}", response_model=PersonOut)
def read_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@router.post("/person/", response_model=PersonOut)
def create_person(person: PersonCreate, db: Session = Depends(get_db)):
    db_person = Person(name=person.name, cpf=person.cpf)
    db.add(db_person)
    db.commit()
    db.refresh(db_person)
    return db_person


@router.delete("/person/{person_id}")
def delete_person(person_id: int, db: Session = Depends(get_db)):
    db_person = db.query(Person).filter(Person.id == person_id).first()
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    db.delete(db_person)
    db.commit()
    return {'"detail": "Person ${db_person.name} successfully"'}
