import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

import sentry_sdk
from sentry_sdk.integrations.asgi import SentryAsgiMiddleware
from config import urls
from config.base import API_VERSION

from config.base import SENTRY_DSN

sentry_sdk.init(
    SENTRY_DSN,
    # environment=ENVIRONMENT,
    traces_sample_rate=1.0
)

itemsInit = {}

app = FastAPI(
    title="Products Api",
    description="FastApi",
    version=API_VERSION,
    redoc_url="/api/v1/redoc",
    docs_url='/api/v1/docs',
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(
    urls.urls
)


SentryAsgiMiddleware(app)
