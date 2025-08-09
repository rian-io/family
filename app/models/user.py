from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(13), nullable=False)  # Format: (99)999999999
    password_hash = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}', phone='{self.phone}')>"
