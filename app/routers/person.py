from fastapi import APIRouter, Depends, HTTPException
from app.database import SessionLocal
from app.models import Person
from app.schemas.Person import PersonCreate, PersonOut
from app.services.person import PersonService

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_person_service(db=Depends(get_db)):
    return PersonService(db)


@router.get("/person", response_model=list[PersonOut])
def read_persons(skip: int = 0, limit: int = 10, service: PersonService = Depends(get_person_service)):
    return service.get_persons(skip, limit)


@router.get("/person/{person_id}", response_model=PersonOut)
def read_person(person_id: int, service: PersonService = Depends(get_person_service)):
    db_person = service.get_person(person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return db_person


@router.post("/person/", response_model=PersonOut)
def create_person(person: PersonCreate, service: PersonService = Depends(get_person_service)):
    db_person = Person(name=person.name, cpf=person.cpf)
    return service.create_person(db_person)


@router.delete("/person/{person_id}")
def delete_person(person_id: int, service: PersonService = Depends(get_person_service)):
    db_person = service.delete_person(person_id)
    if db_person is None:
        raise HTTPException(status_code=404, detail="Person not found")
    return {"detail": f"Person {db_person.name} deleted successfully"}
