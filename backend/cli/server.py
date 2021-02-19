""" Command Line Interface
"""
import click
import uvicorn

from api.app import app
from api.core.config import Settings
from . import cli

settings = Settings()


@cli.command()
@click.option('--host', default=settings.host)
@click.option('--port', default=settings.port)
def api(**kwargs):
    """ Start backend REST API server (API)
    """
    uvicorn.run(app, **kwargs)
