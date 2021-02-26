""" DB
"""
from .sql import attach as sql_attach


def attach(app):
    # no doc
    sql_attach(app)
