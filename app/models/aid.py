from sqlalchemy import Column, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from app.models.user import User

Base = declarative_base()

class Aid(Base):
    __tablename__ = 'aid'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    user = relationship('User')
    amount = Column(Integer, nullable=False)
    date = Column(Date, nullable=False)

    def __repr__(self):
        return f"<Aid(user_id='{self.user_id}', amount='{self.amount}', date='{self.date}')>"
