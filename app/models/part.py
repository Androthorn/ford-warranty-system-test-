from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class Part(Base):
    __tablename__ = "parts"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    description = Column(String)
    price = Column(Float)
    vehicle_id = Column(Integer, ForeignKey("vehicles.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))

    vehicle = relationship("Vehicle", back_populates="parts")
    supplier = relationship("Supplier", back_populates="parts")
    warranties = relationship("Warranty", back_populates="part")
    warranty_parts = relationship("WarrantyPart", back_populates="part") 