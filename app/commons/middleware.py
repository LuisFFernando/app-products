"""."""
from app.respository.persistence_repository import OrmRepository
from app.core import models
# constants
from app.commons.constants import USER_ADMIN


class ValidateRoleUser:
    """."""

    @classmethod
    def is_admin(cls, user_id: int = 0):

        try:
            # validate user is admin
            user_profile = OrmRepository(models.UserProfile).get({"user_id": user_id})

            if user_profile.profile.name != USER_ADMIN:
                raise Exception("User is not admin")
                
        except Exception:
            raise Exception("User is not admin")
