from config.database import base
from sqlalchemy import Column, Integer, String 


class User(base):
    __tablename__ = "user"

    id_document = Column(Integer, primary_key=True, index=True, unique=True)
    name = Column(String(70), nullable=False)
    email = Column(String(70), unique=True, index=True, nullable=False)
    password = Column(String(70),index=True, nullable=False)
    phone = Column(Integer, nullable=False)
    address = Column(String(70), nullable=False)

