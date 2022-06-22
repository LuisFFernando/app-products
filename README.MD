# Microservices Products

-   Language: Python3
-   Framework: FastApi
-   Database: MongoDB - Alembic
-   Container: Docker


## Installation

1.  Install Virtualenv and activate it

```
virtualenv - p python3 venv
```

```
source venv/bin/activate
```

2.  Install requirements.txt

```
pip3 install - r requirements.txt
```
-   Libraries:
    - fastapi
    - boto3
    - pymongo
    - mongoengine

3.  Set up the .env file based on the .env.example

## Documentation

- /api/v1/docs

## Status Services
- /api/v1/health


## **Execution**

**run Server**

- Local
```
$ uvicorn config.settings:app --host=localhost --port=8001 --reload --log-level=info
```
- Docker

```
$ docker-composer up --build
```


### Usage flow

1. Crear migraciones para nuevos modelos
```
alembic revision --autogenerate -m "First migration-w"
```
2. Migrar Db y seeder
```
alembic upgrade head
```
3. Import Envars
```
export $(cat .env | xargs)
```
