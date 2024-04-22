from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float

BaseModel=declarative_base()


class Address(BaseModel):
    __tablename__ = 'addresses'
    id = Column(Integer, primary_key=True)
    full_address = Column(String(500), nullable=False)
    longitude = Column(Float, nullable=False)
    latitude = Column(Float, nullable=False)
    country = Column(String(50), nullable=True)
    postcode = Column(String(50), nullable=True)
    address_line = Column(String(500), nullable=True)
    city=Column(String(500), nullable=True)


    def __repr__(self):
        return f"{self.id} Adress:{self.full_address}"


