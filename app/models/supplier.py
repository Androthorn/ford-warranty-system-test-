from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Supplier(Base):
    __tablename__ = "suppliers"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    contact_person = Column(String)
    email = Column(String)
    phone = Column(String)
    location_id = Column(Integer, ForeignKey("locations.id"))

    location = relationship("Location", back_populates="suppliers")
    parts = relationship("Part", back_populates="supplier")
    warranty_parts = relationship("WarrantyPart", back_populates="supplier") 