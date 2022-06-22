# Microservices Products

We need to build a basic catalog system to manage products. A product should have basic info such as sku, name, price and brand.

In this system, we need to have at least two type of users: (i) admins to create / update / delete products and to create / update / delete other admins; and (ii) anonymous users who can only retrieve products information but can't make changes.

As a special requirement, whenever an admin user makes a change in a product (for example, if a price is adjusted), we need to notify all other admins about the change, either via email or other mechanism.

We also need to keep track of the number of times every single product is queried by an anonymous user, so we can build some reports in the future


## Installation

-   Language: Python3
-   Framework: FastApi
-   Database: MongoDB - Alembic
-   Container: Docker
-   Cloud : AWS


1.  Install local Virtualenv and activate it

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
    - sqlalchemy
    - SQLAlchemy
    - SQLAlchemy-Paginator

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
