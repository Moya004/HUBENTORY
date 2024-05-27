from datetime import timedelta, datetime, timezone
from jose import  jwt
from passlib.context import CryptContext
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, ALGORITHM




pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

oauth2_scheme = OAuth2PasswordBearer(tokenUrl= '/token')

#crea el token de acceso
def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
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
    return pwd_context.verify(plainPassword, hashedPassword)

#te da el hash de la contrasena
def get_password_hash(password: str) -> str: 
    return pwd_context.hash(password)
