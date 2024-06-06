from fastapi import FastAPI, Depends, HTTPException, status
from mangum import Mangum
from sqlalchemy.orm import Session
from fastapi.middleware.cors import CORSMiddleware

from typing import Annotated
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from db import sesion
from db.Schemas.seguridad import PersonaResponse, PersonaCreate, Token

from db.CRUD import persona as persona_crud

from security.autenticacion import authenticate_Persona
from security.verificacion_credenciales import create_access_token
from config import ACCESS_TOKEN_EXPIRE_MINUTES
import uvicorn
from api.routers import Administracion_de_estado_de_inventario, Registro_de_movimientos, Consulta_de_informacion

hubentory = FastAPI()


hubentory.include_router(Administracion_de_estado_de_inventario.router)
hubentory.include_router(Registro_de_movimientos.router)
hubentory.include_router(Consulta_de_informacion.router)

hubentory.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@hubentory.get('/')
def root():
    return {'Hello' : 'World'}

@hubentory.post("/Registro/", response_model=PersonaResponse)
def create_persona(persona: PersonaCreate, db: Annotated[Session, Depends(sesion.get_db)]):
    db_persona = persona_crud.create_persona(db, persona)

    response = PersonaResponse(ID_persona=db_persona.ID_PERSONA, Id_inventrio=db_persona.INVENTARIO.ID_INVENTARIO, Jerarquia=db_persona.JERARQUIA, nombre_completo=db_persona.NOMBRE_COMPLETO, email=db_persona.EMAIL)
    return response



@hubentory.post("/token", response_model=Token)
async def login_for_access_token(form_data: Annotated[OAuth2PasswordRequestForm, Depends()], db: Annotated[Session, Depends(sesion.get_db)]):
    persona = authenticate_Persona(db, form_data.username, form_data.password)
    if not persona:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect ID or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    sub = persona.ID_PERSONA
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": sub}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


handler = Mangum(hubentory)
if __name__ == '__main__':
    uvicorn.run('main:hubentory', reload=True)