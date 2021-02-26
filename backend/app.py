""" Backend
"""
from fastapi import FastAPI

from settings import Settings
from db import sql_attach

settings = Settings()
app = FastAPI(
    title=settings.title,
    description=settings.description,
    version=settings.version
)
sql_attach(app)


