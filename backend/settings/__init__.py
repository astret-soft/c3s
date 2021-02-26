""" Settings
"""
from pydantic import BaseSettings

from .auth import AuthSettings
from .db import DbSettings
from .paging import PagingSettings

__all__ = (
    'Settings',
)

version = '##version##'


class Settings(BaseSettings):
    """ Settings
    """
    class Config:
        env_prefix = 'app_'

    title: str = 'c3s'
    description: str = 'Cloud Scene Screen Service'
    version: str = version
    auth: AuthSettings = AuthSettings()
    db: DbSettings = DbSettings()
    paging: PagingSettings = PagingSettings()
    host: str = '127.0.0.1'
    port: int = 4242
    debug: bool = False

    def info(self) -> dict:
        """ Information about APP depends of settings
        """
        return self.dict(
            exclude=None if self.debug else {  # todo: check before prod!!!
                'db', 'host', 'port', 'debug'
            }
        )
