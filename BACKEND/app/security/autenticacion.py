from security import verificacion_credenciales
from .modelos_seguridad import Persona
from db.Schemas.seguridad import TokenData
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError
from sqlalchemy.orm import Session
from db.Session import get_db


#te da al usuario si se encuentra en la base de datos
def get_Persona(DB: Session, personaID: str) -> Persona | None:
    return DB.query(Persona).filter(Persona.ID_PERSONA == personaID).first()

#autenticacion de usuario y contrasena
def authenticate_Persona(DB, personaID: str, password: str) -> Persona | None:
    user = get_Persona(DB, personaID)
    if not user or not verificacion_credenciales.verify_password(password, user._Persona__password):
        return None
    return user


async def get_current_Persona(db: Session = Depends(get_db), token:str = Depends(verificacion_credenciales.oauth2_scheme)) -> Persona:
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credantials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, verificacion_credenciales.SECRET_KEY, algorithms=[verificacion_credenciales.ALGORITHM])
        personaID = payload.get('sub')
        if personaID is None:
            raise credentials_exception
        token_data = TokenData(ID_persona=personaID)
    except JWTError:
        raise credentials_exception
    
    user = get_Persona(db, token_data.ID_persona)
    if user is None:
        raise credentials_exception
    return user