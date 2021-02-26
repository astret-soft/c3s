""" Entry point for main CLI
"""
import click
import uvicorn

from backend import (
    app,
    settings
)


def start_app(**kwargs):
    """ Start backend REST API server (API)
    """
    uvicorn.run(app, **kwargs)


@click.group()
@click.version_option(version=settings.version)
def cli():
    """ Command Line Interface (CLI)
    """
    pass


@cli.command()
@click.option('--host', '-h', default=settings.host)
@click.option('--port', '-p', default=settings.port)
def start(**kwargs):
    """ Start backend REST API server (API)
    """
    start_app(**kwargs)


@cli.command()
@click.argument('content')
def ping(content: str):
    """ Just working like ping pong in CLI: print in console what you typed
    """
    click.echo(content)


if __name__ == '__main__':
    """ Entry point for main CLI
    """
    cli()
