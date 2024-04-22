FROM python:3.10-slim

SHELL ["/bin/bash", "-c"]

WORKDIR /usr/

EXPOSE 8000

COPY ./src/alembic.ini .
COPY ./src/alembic.ini ./src


COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt



COPY ./src /usr/src/

ENV PYTHONPATH "${PYTHONPATH}:/usr/src"



CMD ["python", "src/main.py"]