""" Core API
"""
from fastapi import APIRouter

from backend.settings import settings

router = APIRouter(
    tags=['core']
)


@router.get('/')
async def get_info():
    """ Get full information about backend
    """
    return settings.info


@router.get('/version')
async def get_version():
    """ Get current version
    """
    return {
        'version': settings.version
    }
