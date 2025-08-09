from pydantic import BaseModel, Field, field_validator
import re


class UserCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Name must not be empty")
    phone: str = Field(..., min_length=13, max_length=13, description="Phone must be in format (99)999999999")
    password: str = Field(..., min_length=8, max_length=128, description="Password must be at least 8 characters")

    @field_validator('phone')
    def validate_phone(cls, v):
        pattern = r"^\(\d{2}\)\d{9}$"
        if not re.match(pattern, v):
            raise ValueError("Phone must be in format (99) 9 9999-9999")
        return v


class UserOut(BaseModel):
    id: int
    name: str
    phone: str

    class Config:
        from_attributes = True

    def __repr__(self):
        return f"<UserOut(id={self.id}, name='{self.name}', phone='{self.phone}')>"
