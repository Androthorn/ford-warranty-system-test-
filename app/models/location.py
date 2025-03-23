from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Location(Base):
    __tablename__ = "locations"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    city = Column(String)
    state = Column(String)
    country = Column(String)
    postal_code = Column(String)

    suppliers = relationship("Supplier", back_populates="location")
    warranties = relationship("Warranty", back_populates="location") 