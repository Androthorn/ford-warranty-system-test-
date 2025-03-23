from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from app.db.base_class import Base

class WarrantyPart(Base):
    __tablename__ = "warranty_parts"

    id = Column(Integer, primary_key=True, index=True)
    warranty_id = Column(Integer, ForeignKey("warranties.id"))
    part_id = Column(Integer, ForeignKey("parts.id"))
    supplier_id = Column(Integer, ForeignKey("suppliers.id"))
    quantity = Column(Integer)
    unit_price = Column(Float)
    total_price = Column(Float)
    notes = Column(String, nullable=True)

    warranty = relationship("Warranty", back_populates="warranty_parts")
    part = relationship("Part", back_populates="warranty_parts")
    supplier = relationship("Supplier", back_populates="warranty_parts") 