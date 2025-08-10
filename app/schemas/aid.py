from pydantic import BaseModel, Field, field_validator

import datetime


class AidCreate(BaseModel):
    user_id: int = Field(..., description="User ID must be provided")
    amount: float = Field(..., ge=1, description="Amount must be at least 1")
    date: datetime.date = Field(..., description="Date must be today")

    @field_validator('date')
    def validate_date(cls, v):
        if v != datetime.date.today():
            raise ValueError("Date must be today")
        return v
