from datetime import timedelta, datetime, timezone
from pydantic import BaseModel
from jose import JWTError, jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer

#no se, creo que las pondre como variables de entorno en la instancia

SECRET_KEY = '41958AA7F6CCC9A49E76E12AB5DFB'
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 30

class Token(BaseModel):
    access_token: str
    token_type : str


class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username:  str
    iD: str | None = None
    fullname: str | None = None
    disable: bool = False

class UserInBD(User):
    hashed_password: str



#crea el token de acceso
def create_acces_token(data: dict, expires_delta: timedelta | None = None) -> str:
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


# Verifica la contrasena digitada con la que esta en la base de datos
def verify_password(plainPassword: str, hashedPassword: str) -> bool:
    return CryptContext(schemes=['bcrypt'], deprecated='auto').verify(plainPassword, hashedPassword)

#te da el hash de la contrasena
def get_password_hash(password: str) -> bool: 
    return CryptContext(schemes=['bcrypt'], deprecated='auto').hash(password)

#te da al usuario si se encuentra en la base de datos
def get_user(DB, username: str) -> UserInBD | None:
    if username in DB:
        user_dict = DB[username]
        return UserInBD(**user_dict)

#autenticacion de usuario y contrasena
def authenticate_user(DB, username: str, password: str) -> UserInBD:
    user = get_user(DB, username)
    if not user:
        return None
    if not verify_password(password, user.hashed_password):
        return None
    return user
