from fastapi import FastAPI
from .routers import users

hubentory = FastAPI()

hubentory.include_router(users.router)

@hubentory.get('/')
def root():
    return {'Hello' : 'World'}


