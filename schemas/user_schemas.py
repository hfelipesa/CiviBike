from pydantic import BaseModel

class UserBase(BaseModel):
    id_document: int
    name: str
    email: str
    password: str
    phone:int
    address:str
    
    class Config:
        orm_mode = True  

class UserCreate(UserBase):
    pass  # No necesitamos agregar nada nuevo aquí, pero se puede extender si se necesitan validaciones adicionales


class UserResponse(UserBase):
    class Config:
        orm_mode = True


