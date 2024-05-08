from fastapi import APIRouter
from typing import Annotated
from datetime import timedelta
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from ..dependencies import Token, authenticate_user as auth, ACCESS_TOKEN_EXPIRE_MINUTES, create_acces_token as createT

router = APIRouter()

db = dict(
        Moya004= dict(
        username='Moya004',
        iD='1043639890',
        fullname='Mario Andres Martinez Moya',
        hashed_password='$2b$12$dHagR6wVUZA1sk/PuRSc0u3BPae6ILjouay0tf4z1zp4DZ1.y8SFe',
        disable=False
    ),
)


oauth2_scheme = OAuth2PasswordBearer(tokenUrl= 'token')

@router.post('/users/Token')
async def iniciar_sesion(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> Token:
    usuario = auth(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='Incorrect credentials',
            headers={"WWW-AUTHENTICATE" : "BEARER"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = createT(
        data={"sub": usuario.username}, expires_delta=access_token_expires
    )
    return Token(access_token= access_token, token_type='bearer')


@router.get('/users/items/')
async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
    return {"token": token}