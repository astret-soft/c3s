""" Settings for paging in API
"""
from pydantic import BaseSettings


class PagingSettings(BaseSettings):
    """ Settings for paging in API
    """
    class Config:
        env_prefix = 'paging_'

    size: int = 100
    allow_offset = True
