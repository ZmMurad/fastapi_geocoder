from typing import Optional
from pydantic import BaseModel





class AddressSchema(BaseModel):
    id:int
    full_address:str


class AddressPost(BaseModel):
    full_address: str
    country:Optional[str]=None
    postcode:Optional[str]=None
    address_line:Optional[str]=None
    city:Optional[str]=None



class AddressPut(BaseModel):
    id:int
    country: Optional[str]
    postcode: Optional[str]
    address_line: Optional[str]
    city: Optional[str]


class AddresGet(AddressSchema):
    longitude:float
    latitude:float
    country:Optional[str]=None
    postcode:Optional[str]=None
    address_line:Optional[str]=None
    city:Optional[str]=None

    class Config:
        from_attributes=True



