""" Cloud Scene Screen Service
"""
import uvicorn
from fastapi import FastAPI

from backend.core.config import Settings

settings = Settings()
app = FastAPI()


@app.get('/info')
async def get_info():
    return {
        'name': __name__,
        'title': __doc__,
        **settings.info()
    }

if __name__ == '__main__':
    """ Run in service
    """
    uvicorn.run(
        app,
        host=settings.host,
        port=settings.port
    )
