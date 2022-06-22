
from app.api.serializers.product_serializers import ProductDeserializer
from app.commons.service_interface import InterfaceService
from app.respository.persistence_repository import OrmRepository

from app.core import models

from app.commons.middleware import ValidateRoleUser


class ProductService(InterfaceService):
    """."""

    def __init__(self, kwargs: dict) -> None:
        self.kwargs = kwargs

    def create(self):
        """Create Product."""

        try:

            # validate user is admin
            ValidateRoleUser.is_admin(self.kwargs.get("user_id"))

            # create Product
            instance_product = OrmRepository(models.Product).create(self.kwargs)

            return ProductDeserializer.from_orm(instance_product).dict()

        except Exception as e:

            raise Exception(e)

    def get(self):
        """Get data Users
        ::Param
            - id
            - name
            - brand
            - sku
        """

        page = self.kwargs.get("page")
        item_per_page = self.kwargs.get("item_per_page")
        self.kwargs.pop("page")
        self.kwargs.pop("item_per_page")

        _instance = OrmRepository(models.Product).filter(self.kwargs, page, item_per_page)

        response = _instance[0]
        data = [ProductDeserializer.from_orm(data).dict() for data in _instance[1]]

        return response, data

    def update(self, params: dict):
        """."""

        # validate user is admin
        ValidateRoleUser.is_admin(params.get("user_id"))
        params.pop("user_id")

        OrmRepository(models.Product).update(params, self.kwargs)

        # notify changes
        

        return

    def delete(self):
        """."""

        # validate user is admin
        ValidateRoleUser.is_admin(self.kwargs.get("user_id"))
        self.kwargs.pop("user_id")

        OrmRepository(models.Product).delete(self.kwargs, {"active": False})

        return

    def filter(self):
        pass
