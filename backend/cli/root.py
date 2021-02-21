""" Command Line Interface
"""
import click
import uvicorn
from api import app
from api.core.config import Settings

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
@click.option('--host', '-h', default=settings.host)
@click.option('--port', '-p', default=settings.port)
def api(**kwargs):
    """ Start backend REST API server (API)
    """
    uvicorn.run(app, **kwargs)


@cli.command()
@click.argument('content')
def ping(content: str):
    """ Just working like ping pong in CLI: print in console what you typed
    """
    click.echo(content)