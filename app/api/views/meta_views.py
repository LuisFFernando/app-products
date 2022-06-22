from fastapi import APIRouter
from starlette import status
from starlette.responses import JSONResponse
from config.base import API_VERSION

router = APIRouter()


@router.get("/", tags=["meta"])
async def root():
    return {"MicroService": "Products"}


@router.get("/version", tags=["meta"])
async def version():
    response = {
        "version": API_VERSION,
        "message": "Products"
    }
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )


@router.get("/health", tags=["meta"])
async def health_check():
    response = {"satus": "ok"}
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content=response
    )
