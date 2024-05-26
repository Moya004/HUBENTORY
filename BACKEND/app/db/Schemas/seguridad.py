from pydantic import BaseModel
from datetime import date
from typing import Optional

class PersonaBase(BaseModel):
    ID_persona: str
    Id_inventrio: str
    Jerarquia: int
    nombre_completo: str
    email: str

class PersonaCreate(PersonaBase):
    Contraseña: str

class PersonaAuthenticate(BaseModel):
    ID_persona: str
    Contraseña: str

class PersonaResponse(PersonaBase):
    class Config:
        from_attributes = True

class PersonaUpdatePassword(BaseModel):
    Contraseña: str

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    ID_persona: Optional[str] = None
