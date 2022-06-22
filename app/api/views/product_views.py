from typing import Optional
from fastapi import APIRouter, Request

from sentry_sdk import capture_exception
from starlette import status
from starlette.responses import JSONResponse

# serializers
from app.api.serializers.product_serializers import CreateProductSerializer
from app.api.serializers.product_serializers import ParamProductGetSerializer
from app.api.serializers.product_serializers import UpdateProductSerializer

# handlers
from app.api.handler.product_handler import HandlerProduct

router = APIRouter()


@router.post("/product", tags=["Product"])
def create_product(request: CreateProductSerializer):
    """Create product."""

    try:
        handler_create = HandlerProduct.create_product(request.dict(exclude_none=True))
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


@router.get("/product", tags=["Product"])
def get_product(request: Request, id: Optional[int] = 1,
                name: Optional[str] = "",
                item_per_page: Optional[int] = 1,
                page: Optional[int] = 1):
    """Get User by params

    :: Params

        - id
        - name
        - brand
        - sku
        - item_per_page
        - page
    """

    try:
        serializers = ParamProductGetSerializer(**request.query_params).dict(exclude_none=True)
        meta, response = HandlerProduct.get_product(serializers)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content=dict(
                success=True,
                code=0,
                locale="es",
                message="OK",
                data=response,
                meta=meta
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


@router.put("/product/{id}", tags=["Product"])
def update_product(id: int, request: UpdateProductSerializer, user_id: Optional[int] = 0):
    """Update Product by id

    :: Path

        - id
    """
    try:
        HandlerProduct.update_product({"id": id, "user_id": user_id}, request.dict(exclude_none=True))
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=dict(
                success=True,
                code=0,
                locale="es",
                message="OK",
                data={"product_id": id}
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


@router.delete("/product/{id}", tags=["Product"])
def delete_product_by_id(id: int, user_id: Optional[int] = 0):
    """Delete Product by uid

    :: Path

        - id
    """
    try:
        HandlerProduct.delete_product({"id": id, "user_id": user_id})
        return JSONResponse(
            status_code=status.HTTP_201_CREATED,
            content=dict(
                success=True,
                code=0,
                locale="es",
                message="OK"
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
