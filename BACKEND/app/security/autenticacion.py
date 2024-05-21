from security import seguridad
from modelos_seguridad import User, UserInBD, TokenData
from fastapi import Depends, HTTPException, status
from jose import jwt, JWTError

db = dict(
        Moya004= dict(
        username='Moya004',
        iD='1043639890',
        fullname='Mario Andres Martinez Moya',
        hashed_password='$2b$12$dHagR6wVUZA1sk/PuRSc0u3BPae6ILjouay0tf4z1zp4DZ1.y8SFe',
        disable=False
    ),
)



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
    if not seguridad.verify_password(password, user.hashed_password):
        return None
    return user


async def get_current_user(token:str = Depends(seguridad.oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credantials",
        headers={"WWW-Authenticate": "Bearer"}
    )

    try:
        payload = jwt.decode(token, seguridad.SECRET_KEY, algorithms=[seguridad.ALGORITHM])
        username = payload.get('sub')
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user

async def get_current_active_user(curr_user: User = Depends(get_current_user)):
    if curr_user.isDisable:
        raise HTTPException(status_code=400, detail='Inactive user')
    return curr_user