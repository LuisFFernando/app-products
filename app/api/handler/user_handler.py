
from app.core.service_user import UserService


class HandlerUser:

    @staticmethod
    def create_user(kwargs: dict):
        return UserService(kwargs).create()

    @staticmethod
    def reset_password(kwargs):
        return kwargs

    @staticmethod
    def get_user(kwargs: dict):
        return UserService(kwargs).get()

    @staticmethod
    def get_one_user(kwarg: dict):
        """ Retorna """
        return

    @ staticmethod
    def update_user(kwarg):
        return
