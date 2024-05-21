from pydantic import BaseModel

class Token(BaseModel):
    access_token: str
    token_type : str


class TokenData(BaseModel):
    username: str | None = None

class User(BaseModel):
    username:  str
    iD: str | None = None
    fullname: str | None = None
    isDisable: bool = False

class UserInBD(User):
    hashed_password: str