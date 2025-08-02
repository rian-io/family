from sqlalchemy.orm import Session
from app.models.Person import Person
from app.database import SessionLocal


class PersonService:
    def __init__(self, db: Session):
        self.db = db

    def get_persons(self, skip: int = 0, limit: int = 10):
        return self.db.query(Person).offset(skip).limit(limit).all()

    def get_person(self, person_id: int):
        return self.db.query(Person).filter(Person.id == person_id).first()

    def create_person(self, db_person: Person):
        self.db.add(db_person)
        self.db.commit()
        self.db.refresh(db_person)
        return db_person

    def delete_person(self, person_id: int):
        db_person = self.db.query(Person).filter(Person.id == person_id).first()
        if db_person:
            self.db.delete(db_person)
            self.db.commit()
        return db_person
