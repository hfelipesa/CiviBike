from pydantic import BaseModel

class BikeBase(BaseModel):
    brand: str
    model: str
    is_available: bool = True 

    class Config:
        orm_mode = True


class BikeCreate(BikeBase):
    pass 


class BikeResponse(BikeBase):
    id: int  

    class Config:
        orm_mode = True
