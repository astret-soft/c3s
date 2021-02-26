""" Core API
"""
from fastapi import APIRouter

from backend import settings

router = APIRouter()


@router.get('/version')
async def get_version():
    """ Get current version
    """
    return {
        'version': settings.version
    }


@router.get('/')
async def get_info():
    """ Get full information about backend
    """
    return settings.info()
