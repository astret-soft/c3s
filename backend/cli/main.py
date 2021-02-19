""" Command Line Interface
"""
import click

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
