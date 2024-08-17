from sqlalchemy import Column, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from config.database import base
from datetime import datetime


class Loan(base):
    __tablename__ = "loan"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('user.id_document'), nullable=False)
    bike_id = Column(Integer, ForeignKey('bike.id'), nullable=False)
    loan_date = Column(DateTime, nullable=False)
    return_date = Column(DateTime, nullable=True)

    # Relaciones con las otras tablas
    user = relationship("User")
    bike = relationship("Bike")