from fastapi import APIRouter, Request
from fastapi import HTTPException
from pydantic import ValidationError
from fastapi import File
from fastapi import Form

from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

# serializers
from app.api.serializers.user_serializer import CreateUserSerializer
from app.api.serializers.user_serializer import ParamUserGetSerializer


from uuid import UUID

# handlers
from app.api.handler.user_handler import HandlerUser

router = APIRouter()


@router.post("/user", tags=["User"])
def create_customer(request: CreateUserSerializer):
    """Create Section."""

    try:
        handler_create = HandlerUser.create_user(request.dict(exclude_none=True))
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=dict(
                success=True,
                code=0,
                locale="es",
                message="OK",
                data=handler_create
            )
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            dict(
                error=True,
                description=str(e)
            ),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )


@router.get("/user", tags=["User"])
def get_section(request: Request):
    """Get User by params
    :: Params
        - id
        - nid
        - email
        - phone
        - name
    """

    try:
        serializers = ParamUserGetSerializer(**request.query_params).dict(exclude_none=True)
        response = HandlerUser.get_user(serializers)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=dict(
                success=True,
                code=0,
                locale="es",
                message="OK",
                data=response
            )
        )
    except Exception as e:
        capture_exception(e)
        return JSONResponse(
            dict(
                error=True,
                description=str(e)
            ),
            status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )