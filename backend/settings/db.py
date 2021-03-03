""" Settings for using DB
"""
from typing import Union

from pydantic import AnyUrl, BaseSettings, PostgresDsn, RedisDsn


class MySqlDsn(AnyUrl):
    allowed_schemes = {'mysql'}
    user_required = True


class DbSettings(BaseSettings):
    """ Settings for using DB
    """
    class Config:
        env_prefix = 'db_'

    sql: Union[PostgresDsn, MySqlDsn] = 'postgres://c3s:test@localhost:5432/c3s'
    redis: RedisDsn = 'redis://user:pass@localhost:6379/1'
