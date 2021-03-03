""" DB module
"""
from tortoise.contrib.fastapi import register_tortoise

from backend.settings import settings


def attach(app):
    # no doc
    print(settings.db)
    register_tortoise(
        app,
        db_url=settings.db.sql,
        modules={'models': ['user.models']},
        generate_schemas=True,
        add_exception_handlers=True
    )
