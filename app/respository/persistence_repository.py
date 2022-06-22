
from sentry_sdk import capture_exception
from sqlalchemy import false
from sqlalchemy.exc import NoResultFound
from sqlalchemy.exc import DatabaseError
from sqlalchemy.exc import IntegrityError
from sqlalchemy_paginator import Paginator
from sqlalchemy_paginator.exceptions import EmptyPage
# from .exceptions import FileNotFound
# from .exceptions import GeneralException

# interface

from app.respository.crud_interface import InterfaceCrud

from config.postgres_conection import session


class OrmRepository(InterfaceCrud):
    """
    """

    def __init__(self, entity):
        self.entity = entity

    def filter(self,
               data,
               page,
               per_page):
        """
        Get one data include filters, order_by, columns to orders
        """
        try:
            _instance = session.query(self.entity).filter_by(
                **data).order_by()

            _paginator = Paginator(_instance, per_page, allow_empty_first_page=False)
            _page = _paginator.page(page)

            meta = {
                "current_page": str(_page),
                "item_per_page": per_page,
                "total_page": _page.paginator.total_pages,
                "total_items": len(_page.object_list),
                "available_orders": [
                    "ASC",
                    "DESC"
                ]
            }
            return meta, _page.object_list,

        except EmptyPage:
            session.rollback()
            raise Exception("That page contains no results")

    def delete(self,params, kwargs):
        try:
            session.query(self.entity).filter_by(**params).update(kwargs)
            session.commit()
            return

        except DatabaseError as e:
            session.rollback()
            capture_exception(e)
            raise Exception(str(e))

        finally:
            session.close()

    def create(self, kwargs):
        try:

            _instance = self.entity(**kwargs)
            session.add(_instance)
            session.commit()

            return _instance

        except IntegrityError as error:

            session.rollback()
            capture_exception(error)
            raise Exception(str(error))

        except Exception as e:
            session.rollback()
            capture_exception(e)
            raise Exception(e)

    def update(self, param, kwargs):
        """."""
        try:

            session.query(self.entity).filter_by(**param).update(kwargs)
            session.commit()
            return

        except Exception as e:
            session.rollback()
            capture_exception(e)
            raise Exception(e)

    def get(self, kwargs):
        """Return one Object."""
        try:

            _instance = session.query(self.entity).filter_by(**kwargs).one()
            return _instance

        except NoResultFound:

            session.rollback()
            capture_exception(NoResultFound(f"{kwargs} not found"))
            raise Exception(f"{kwargs} not found")

        except Exception as e:

            session.rollback()
            capture_exception(Exception)
            raise Exception(e)
