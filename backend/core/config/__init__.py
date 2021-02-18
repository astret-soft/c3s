""" Settings
"""
from pydantic import BaseSettings

from .auth import AuthSettings
from .db import DbSettings
from .paging import PagingSettings

__all__ = (
    'Settings',
)

version = '0.0.1'


class Settings(BaseSettings):
    """ Settings
    """
    class Config:
        env_prefix = 'app_'

    version = version
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
            exclude=None if self.debug else {
                'db', 'host', 'port', 'debug'
            }
        )
