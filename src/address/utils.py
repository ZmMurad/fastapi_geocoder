import httpx
from sqlalchemy.ext.asyncio import create_async_engine, AsyncEngine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.engine import URL
from src.env import ENV
import logging


def create_engine(url:URL|str) -> AsyncEngine:
    return create_async_engine(url=url, echo=False, future=True)

# async def  proceed_schemas(engine:AsyncEngine, metadata:MetaData) -> None:
#     async with engine.begin() as conn:
#         await conn.run_sync(metadata.create_all())

def get_session_maker(engine:AsyncEngine) -> sessionmaker:
    return sessionmaker(engine, class_ = AsyncSession, expire_on_commit=False)


async def get_full_info(address:str)->dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(f"{ENV.URL_GEOCODER}",params={'text':address,'apiKey':ENV.APIKEY})
        if response.status_code==200:
            json_object_full = response.json()
            json_object=json_object_full.get('features')[0].get('properties')
            dump_model_info = {}
            dump_model_info['full_address'] = address
            dump_model_info['longitude'] = json_object.get('lon')
            dump_model_info['latitude'] = json_object.get('lat')
            dump_model_info['country'] = json_object.get('country')
            dump_model_info['postcode'] = json_object.get('postcode')
            dump_model_info['city'] = json_object.get('city')
            dump_model_info['address_line'] = json_object.get('address_line2')
            return dump_model_info


engine=create_engine(ENV.url_postgre)
logging.warning(ENV.url_postgre)
Session = get_session_maker(engine)