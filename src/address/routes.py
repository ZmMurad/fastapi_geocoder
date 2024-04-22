import logging

from fastapi import APIRouter
from fastapi import Depends
from fastapi.responses import JSONResponse
from sqlalchemy.ext.asyncio import AsyncSession

from src.address.crud import get_address,add_new_address
from src.address.schemas import AddresGet, AddressPost, AddressPut
from src.db_utils import get_db
from src.address.utils import get_full_info

router=APIRouter()

@router.post('/address/{address}/',response_model=AddresGet)
async def post_address(address: str, db:AsyncSession=Depends(get_db)):
    full_info = await get_full_info(address)
    db_address = await get_address(db,full_info)
    if not db_address:
        db_address = await add_new_address(db,full_info)
    view_address =AddresGet.from_orm(db_address)
    return JSONResponse(status_code=200,content=view_address.dict())