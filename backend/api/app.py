""" REST API
"""
from fastapi import FastAPI

from api.core.config import Settings

__all__ = (
    'app',
    'settings',
)

settings = Settings()
app = FastAPI()  # take api and api as synonyms


@app.get('/version')
async def get_version():
    return {
        'version': settings.version
    }


@app.get('/info')
async def get_info():
    return {settings.info()}
