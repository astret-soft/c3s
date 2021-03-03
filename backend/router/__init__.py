""" Router
"""
from fastapi import FastAPI

from core.router import router as core
from user.router import router as user

__all__ = (
    'init_routers',
)


def init_routers(app: FastAPI):
    app.include_router(core)
    app.include_router(user)
