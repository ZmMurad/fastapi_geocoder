from fastapi import FastAPI
from src.address.routes import router
from alembic.config import Config
from alembic import command
import asyncio
import uvicorn

app = FastAPI()


import alembic.config
alembicArgs = [
    '--raiseerr',
    'upgrade', 'head',
]
alembic.config.main(argv=alembicArgs)




app.include_router(router,prefix='')

if __name__ == "__main__":


    uvicorn.run(
        app, host="0.0.0.0", port=8000, proxy_headers=True, forwarded_allow_ips="*"
    )