from sqlalchemy import Column, Integer, String, Date, Text, ForeignKey, Enum, Float
from sqlalchemy.orm import relationship
from app.models.base import BaseModel
import enum

class PropulsionType(enum.Enum):
    ELECTRIC = "eletric"
    HYBRID = "hybrid"
    GAS = "gas"

class PurchaseType(enum.Enum):
    BULK = "bulk"
    WARRANTY = "warranty"

class Location(BaseModel):
    __tablename__ = "dim_locations"

    market = Column(String(50), nullable=False)
    country = Column(String(50), nullable=False)
    province = Column(String(50), nullable=False)
    city = Column(String(50), nullable=False)

    # Relacionamentos
    suppliers = relationship("Supplier", back_populates="location")
    warranties = relationship("Warranty", back_populates="location")

class Supplier(BaseModel):
    __tablename__ = "dim_suppliers"

    name = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey("dim_locations.id"), nullable=False)

    # Relacionamentos
    location = relationship("Location", back_populates="suppliers")
    parts = relationship("Part", back_populates="supplier")

class Vehicle(BaseModel):
    __tablename__ = "dim_vehicles"

    model = Column(String(255), nullable=False)
    prod_date = Column(Date, nullable=False)
    year = Column(Integer, nullable=False)
    propulsion = Column(Enum(PropulsionType), nullable=False)

    # Relacionamentos
    warranties = relationship("Warranty", back_populates="vehicle")

class Part(BaseModel):
    __tablename__ = "dim_parts"

    name = Column(String(255), nullable=False)
    supplier_id = Column(Integer, ForeignKey("dim_suppliers.id"), nullable=False)
    last_purchase_id = Column(Integer, ForeignKey("dim_purchases.id"), nullable=False)

    # Relacionamentos
    supplier = relationship("Supplier", back_populates="parts")
    last_purchase = relationship("Purchase", foreign_keys=[last_purchase_id])
    purchases = relationship("Purchase", back_populates="part")
    warranties = relationship("Warranty", back_populates="part")

class Purchase(BaseModel):
    __tablename__ = "dim_purchases"

    purchase_type = Column(Enum(PurchaseType), nullable=False)
    purchase_date = Column(Date, nullable=False)
    part_id = Column(Integer, ForeignKey("dim_parts.id"), nullable=False)

    # Relacionamentos
    part = relationship("Part", back_populates="purchases")
    warranties = relationship("Warranty", back_populates="purchase")

class Warranty(BaseModel):
    __tablename__ = "fact_warranties"

    vehicle_id = Column(Integer, ForeignKey("dim_vehicles.id"), nullable=False)
    repair_date = Column(Date, nullable=False)
    client_comment = Column(Text)
    tech_comment = Column(Text, nullable=False)
    part_id = Column(Integer, ForeignKey("dim_parts.id"), nullable=False)
    classified_failure = Column(String(50), nullable=False)
    location_id = Column(Integer, ForeignKey("dim_locations.id"), nullable=False)
    purchase_id = Column(Integer, ForeignKey("dim_purchases.id"), nullable=False)

    # Relacionamentos
    vehicle = relationship("Vehicle", back_populates="warranties")
    part = relationship("Part", back_populates="warranties")
    location = relationship("Location", back_populates="warranties")
    purchase = relationship("Purchase", back_populates="warranties") 