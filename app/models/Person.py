from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)

    def __repr__(self):
        return f"<Person(id={self.id}, name='{self.name}')>"
