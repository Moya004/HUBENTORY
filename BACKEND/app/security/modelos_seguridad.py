from dataclasses import dataclass
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.Session import Base
from models.modelos import Inventario
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@dataclass
class Persona(Base):
    __tablename__ = 'personas'
    __slots__ = ['__ID_PERSONA', '__NOMBRE_COMPLETO', '__INVENTARIO', '__INVENTARIO_ID', '__JERARQUIA', '__EMAIL', '__password']

    __ID_PERSONA: Mapped[str] = mapped_column('ID_PERSONA', String, primary_key= True)
    __NOMBRE_COMPLETO: Mapped[str] = mapped_column('NOMBRE_COMPLETO', String, nullable=False)
    __INVENTARIO: Mapped[Inventario] = relationship('Inventario')
    __INVENTARIO_ID: Mapped[str] = mapped_column(String, ForeignKey('inventarios.ID_INVENTARIO'), nullable= False, repr=False)
    __JERARQUIA: Mapped[int] = mapped_column('JERARQUIA', Integer)
    __EMAIL: Mapped[str] = mapped_column('EMAIL', String, nullable=False)
    __password: Mapped[str] = mapped_column('password', String, nullable=False)

    def __init__(self, idp: str, nom: str, inv: Inventario, jer: int, mail: str, contra: str) -> None:
        object.__setattr__(self, '__ID_PERSONA', idp)
        object.__setattr__(self, '__NOMBRE_COMPLETO', nom)
        object.__setattr__(self, '__INVENTARIO', inv)
        object.__setattr__(self, '__INVENTARIO_ID', inv.ID_INVENTARIO)
        object.__setattr__(self, '__JERARQUIA', jer)
        object.__setattr__(self, '__EMAIL', mail)
        
        self.__password = self.hash_password(contra)

    def verify_password(self, plain_password: str) -> bool:
        return pwd_context.verify(plain_password, self.__Contraseña)

    def hash_password(self, plain_password: str) -> str:
        return pwd_context.hash(plain_password)

    @property
    def ID_PERSONA(self) -> str:
        return self.__ID_PERSONA
        
    @property
    def NOMBRE_COMPLETO(self) -> str:
        return self.__NOMBRE_COMPLETO
    
    @property
    def INVENTARIO(self) -> Inventario:
        return self.__INVENTARIO
    
    @property
    def JERARQUIA(self) -> str:
        return self.__JERARQUIA
    
    @property
    def EMAIL(self) -> str:
        return self.__EMAIL
    
