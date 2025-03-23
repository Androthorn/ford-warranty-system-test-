from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    model = Column(String)
    year = Column(Integer)
    propulsion = Column(String)
    price = Column(Float)

    parts = relationship("Part", back_populates="vehicle")
    warranties = relationship("Warranty", back_populates="vehicle") 