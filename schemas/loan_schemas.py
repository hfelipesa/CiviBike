from pydantic import BaseModel
from datetime import datetime

class LoanBase(BaseModel):
    user_id: str
    bike_id: int
    loan_date: datetime
    return_date: datetime

    class Config:
        orm_mode = True


class LoanCreate(LoanBase):
    pass


class LoanResponse(LoanBase):
    id: int  

    class Config:
        orm_mode = True

