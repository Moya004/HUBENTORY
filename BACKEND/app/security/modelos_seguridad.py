from dataclasses import dataclass
from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.sesion import Base
from models.modelos import Inventario




@dataclass
class Persona(Base):
    __tablename__ = 'personas'
    
    __ID_PERSONA: Mapped[str] = mapped_column('ID_PERSONA', String, primary_key= True)
    __NOMBRE_COMPLETO: Mapped[str] = mapped_column('NOMBRE_COMPLETO', String, nullable=False)
    __INVENTARIO_ID: Mapped[str] = mapped_column('INVENTARIO_ID', String, ForeignKey('inventarios.ID_INVENTARIO'), nullable= False, repr=False)
    __INVENTARIO: Mapped[Inventario] = relationship('Inventario')
    __JERARQUIA: Mapped[int] = mapped_column('JERARQUIA', Integer)
    __EMAIL: Mapped[str] = mapped_column('EMAIL', String, nullable=False)
    __password: Mapped[str] = mapped_column('password', String, nullable=False)

    def __init__(self, idp: str, nom: str, inv: Inventario, jer: int, mail: str, contra: str) -> None:
        self.__ID_PERSONA = idp
        self.__NOMBRE_COMPLETO = nom
        self.__INVENTARIO = inv
        self.__INVENTARIO_ID = inv.ID_INVENTARIO
        self.__JERARQUIA = jer
        self.__EMAIL = mail
        
        self.__password = contra

    # def verify_password(self, plain_password: str) -> bool:
    #     return pwd_context.verify(plain_password, self.__Contraseña)


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
    
