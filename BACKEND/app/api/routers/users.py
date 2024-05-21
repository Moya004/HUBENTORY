from fastapi import APIRouter, Depends, HTTPException, status
from typing import Annotated
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm
from security import seguridad, modelos_seguridad as mds
from config import ACCESS_TOKEN_EXPIRE_MINUTES
from security.autenticacion import  authenticate_user as auth, db, get_current_active_user, get_current_user
from security.modelos_seguridad import User


router = APIRouter()



@router.post('/users/token', response_model=mds.Token)
async def iniciar_sesion(
    form_data: Annotated[OAuth2PasswordRequestForm, Depends()]
) -> mds.Token:
    usuario = auth(db, form_data.username, form_data.password)
    if not usuario:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, 
            detail='CREDENCIALES INCORRECTAS',
            headers={"WWW-AUTHENTICATE" : "BEARER"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    access_token = seguridad.create_acces_token(
        data={"sub": usuario.username}, expires_delta=access_token_expires
    )
    return mds.Token(access_token= access_token, token_type='bearer')


@router.get('/users/items/')
async def read_items(token: Annotated[str, Depends(seguridad.oauth2_scheme)]):
    return {"token": token}


@router.get('/users/me', response_model=mds.User)
async def get_me(curr_user: User = Depends(get_current_active_user)):
    return curr_user

@router.get('/users/me/items')
async def read_own_items(curr_user: User = Depends(get_current_active_user)):
    return [{"item_id": "MAGERIT", "owner": curr_user.username}]