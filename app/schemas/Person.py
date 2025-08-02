from pydantic import BaseModel, Field


class PersonCreate(BaseModel):
    name: str = Field(..., min_length=1, max_length=50, description="Name must not be empty")
    cpf: str = Field(..., min_length=11, max_length=11, description="CPF must be exactly 11 characters long")


class PersonOut(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True

    def __repr__(self):
        return f"<PersonOut(id={self.id}, name='{self.name}')>"
