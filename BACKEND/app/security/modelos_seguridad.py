from db.Session import Base

class Token(Base):
    access_token: str
    token_type : str


class TokenData(Base):
    username: str | None = None

class Persona(Base):
    username:  str
    iD: str | None = None
    fullname: str | None = None
    isDisable: bool = False

class UserInBD(Persona):
    hashed_password: str