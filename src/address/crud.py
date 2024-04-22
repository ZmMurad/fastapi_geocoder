from src.address.models import Address
from sqlalchemy import select, and_
from sqlalchemy.ext.asyncio import AsyncSession
from src.address.schemas import AddressSchema,AddressPut,AddressPost,AddresGet
from src.address.utils import get_full_info

async def add_new_address(db:AsyncSession, dump_model_info:dict) -> Address:
    db_address = Address(**dump_model_info)
    db.add(db_address)
    await db.commit()
    await db.refresh(db_address)
    return db_address



async def get_address(db:AsyncSession, address:dict) -> Address:
    filters = []
    for key,value in address.items():
        if value is not None:
            filters.append(getattr(Address,key) == value)
    addressess = select(Address).filter(and_(*filters))
    result = await db.execute(addressess)
    return result.scalar_one_or_none()
