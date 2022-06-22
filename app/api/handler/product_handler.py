
from app.core.service_products import ProductService


class HandlerProduct:

    @staticmethod
    def create_product(kwargs: dict):
        return ProductService(kwargs).create()

    @staticmethod
    def get_product(kwargs: dict):
        return ProductService(kwargs).get()

    @ staticmethod
    def update_product(params, kwargs):
        return ProductService(kwargs).update(params)

    @ staticmethod
    def delete_product(params):
        return ProductService(params).delete()
