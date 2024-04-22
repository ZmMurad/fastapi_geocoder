import os
import logging as log
from os import environ
from logging.handlers import TimedRotatingFileHandler
from dotenv import load_dotenv
load_dotenv()



if not os.path.exists("log"):
    os.mkdir("log")

class Environment:
    POSTGRE_HOST:str = str(environ.get("POSTGRE_HOST"))
    POSTGRE_PORT:str = str(environ.get("POSTGRE_PORT"))
    POSTGRE_USERNAME:str = str(environ.get("POSTGRES_USER"))
    POSTGRE_PASS:str = str(environ.get("POSTGRES_PASSWORD"))
    POSTGRE_DB_NAME:str = str(environ.get("POSTGRES_DB"))
    url_postgre = f"postgresql+asyncpg://{POSTGRE_USERNAME}:{POSTGRE_PASS}@{POSTGRE_HOST}:{POSTGRE_PORT}/{POSTGRE_DB_NAME}"
    LOGGING_LEVEL = 20
    URL_GEOCODER='https://api.geoapify.com/v1/geocode/search'
    APIKEY=str(environ.get("APIKEY"))




log.basicConfig(
    level=20,
    format='[%(asctime)s.%(msecs)03d] [%(levelname)-6s] [%(filename)-24s] : %(message)s',
    handlers=[
        log.StreamHandler(),
        TimedRotatingFileHandler(filename="log/application.log", when="D", backupCount=14)
    ]
)





ENV = Environment()
