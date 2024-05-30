from datetime import timedelta, datetime, timezone
from jose import  jwt
import bcrypt
from fastapi.security import OAuth2PasswordBearer
from config import SECRET_KEY, ALGORITHM




#pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

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
    password_byte_enc = plainPassword.encode('utf-8')
    hashedPassword = hashedPassword.encode('utf-8')
    print('verificando...')
    verify = bcrypt.checkpw(password = password_byte_enc , hashed_password = hashedPassword)
    print('funciono!!!')
    return verify

#te da el hash de la contrasena
def get_password_hash(password: str) -> str: 
    pwd_bytes = password.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password=pwd_bytes, salt=salt)
    return hashed_password
