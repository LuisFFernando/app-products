
from app.api.serializers.user_serializer import UserDeserializer
from app.commons.service_interface import InterfaceService
from app.respository.persistence_repository import OrmRepository

from app.core import models

class UserService(InterfaceService):
    """."""

    def __init__(self, kwargs: dict) -> None:
        self.kwargs = kwargs

    def create(self):
        """Create User."""

        profile_id = self.kwargs.get("user_profile")
        self.kwargs.pop("user_profile")

        try:

            _profile = OrmRepository(models.Profile).get({"id": profile_id})

        except Exception:

            raise Exception("Profile not found")

        # create user
        _user = OrmRepository(models.User).create(self.kwargs)

        # create user_profile
        OrmRepository(models.UserProfile).create({"profile_id": _profile.id, "user_id": _user.id})

        return UserDeserializer.from_orm(_user).dict()

    def get(self):
        """Get data Users
        ::Param
            - id
            - nid
            - email
            - phone            
        """

        _instance = OrmRepository(models.User).get(self.kwargs)

        rest = [UserDeserializer.from_orm(data).dict() for data in _instance]

        return rest

    def update(self):
        pass

    def delete(self):
        pass

    def filter(self):
        pass
