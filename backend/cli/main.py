""" Command Line Interface
"""
import click

from api.core.config import Settings
from api import app

settings = Settings()

__all__ = (
    'cli',
)


@click.group(context_settings={'help_option_names': ['-h', '--help']})
@click.version_option(version=settings.version)
def cli():
    """ Command Line Interface (CLI)
    """
    pass


@cli.command()
@click.option('--host', default=settings.host)
@click.option('--port', default=settings.port)
def api(**kwargs):
    """ Start backend REST API server (API)
    """
    import uvicorn
    uvicorn.run(app, **kwargs)
