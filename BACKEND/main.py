from fastapi import FastAPI


hubentory = FastAPI()

@hubentory.get('/')
def root():
    return {'Hello' : 'World'}