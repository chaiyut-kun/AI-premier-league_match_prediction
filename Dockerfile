
FROM python:3.11

WORKDIR /code

COPY ./requirements.txt /code/requirements.txt

RUN pip install --upgrade pip 

RUN pip install --no-cache-dir  -r /code/requirements.txt


COPY ./src/api /code

EXPOSE 8000

CMD ["fastapi", "run", "server.py", "--port", "8000"]