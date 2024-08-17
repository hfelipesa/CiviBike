from sqlalchemy import Column, Integer, String, Boolean
from config.database import base

class Bike(base):
    __tablename__ = "bike"

    id = Column(Integer, primary_key=True, index=True)
    brand = Column(String(70), nullable=False)
    model = Column(String(70), nullable=False)
    is_available = Column(Boolean, default=True)
