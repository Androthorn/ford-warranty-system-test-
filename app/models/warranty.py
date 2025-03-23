from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Warranty(Base):
    __tablename__ = "warranties"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))
    location_id = Column(Integer, ForeignKey("locations.id"))
    failure_type = Column(String)
    failure_date = Column(Date)
    description = Column(String)
    status = Column(String)
    resolution_date = Column(Date, nullable=True)
    resolution_description = Column(String, nullable=True)

    vehicle = relationship("Vehicle", back_populates="warranties")
    part = relationship("Part", back_populates="warranties")
    location = relationship("Location", back_populates="warranties")
    warranty_parts = relationship("WarrantyPart", back_populates="warranty") 