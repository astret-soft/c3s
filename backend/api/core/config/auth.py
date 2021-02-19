""" Settings for authorization
"""
from pydantic import BaseSettings


class AuthSettings(BaseSettings):
    """ Settings for authorization
    """
    class Config:
        env_prefix = 'auth_'

    expiration = 365
    retries = -1
