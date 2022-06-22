from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
import os
from sqlalchemy.orm import declarative_base
import logging


try:
    connect = os.environ.get('DB_URI', 'test')
    engine = create_engine(connect)
    Session = scoped_session(sessionmaker(bind=engine))
    session = Session()
    Base = declarative_base()

except Exception as e:
    logging.error("Error conexion DB")
    raise Exception("Error conexion DB", e)
