from src.address.utils import Session
async def get_db():
    sessionlocal = Session()
    try:
        yield sessionlocal
    finally:
        await sessionlocal.close()