""" DB module
"""
from tortoise.contrib.fastapi import register_tortoise
from api import app


register_tortoise(
    app,
    db_url='sqlite://db.sqlite3',
    modules={'models': ['main']},
    generate_schemas=True,
    add_exception_handlers=True
)