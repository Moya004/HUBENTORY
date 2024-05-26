from dataclasses import dataclass, field
from datetime import date
from sqlalchemy import PrimaryKeyConstraint, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.sesion import Base



@dataclass()
class Inventario(Base):
    __tablename__ = 'inventarios'

    __ID_INVENTARIO: Mapped[str] = mapped_column('ID_INVENTARIO', String, primary_key= True)
    __nombre: Mapped[str] = mapped_column('NOMBRE', String)

    def __init__(self, id_inv: str, name: str) -> None:
        self.__ID_INVENTARIO = id_inv
        self.__nombre = name


    @property
    def ID_INVENTARIO(self) -> str:
        return self.__ID_INVENTARIO
    
    @property
    def NOMBRE(self) -> str:
        return self.__nombre
    

    @NOMBRE.setter
    def NOMBRE(self, new_name: str) -> None:
        self.__nombre = new_name

    def __hash__(self) -> int: ...

@dataclass
class Categoria(Base):
    __tablename__ = 'categorias'
    
    __ID_CATEGORIA: Mapped[str] = mapped_column('ID_CATEGORIA', String, primary_key= True)
    __nombre: Mapped[str] = mapped_column('NOMBRE', String)
    __INVENTARIO_ID: Mapped[str] = mapped_column('INVENTARIO_ID',String, ForeignKey('inventarios.ID_INVENTARIO'), nullable=False, repr=False, init=False)
    __INVENTARIO: Mapped[Inventario] = relationship('Inventario')


    def __init__(self, nom: str, id_cat: str, inve: Inventario) -> None:
        self.__ID_CATEGORIA = id_cat
        self.__INVENTARIO = inve
        self.__INVENTARIO_ID = inve.ID_INVENTARIO

        self.__nombre = nom


    @property
    def ID_CATEGORIA(self) -> str:
        return self.__ID_CATEGORIA
    
    @property
    def nombre(self) -> str:
        return self.__nombre
    
    @property
    def INVENTARIO(self) -> Inventario:
        return self.__INVENTARIO
    
    @nombre.setter
    def nombre(self, value: str) -> None:
        self.__nombre = value
    
    def __hash__(self) -> int:
        return hash(self.__ID_CATEGORIA, self.__INVENTARIO_ID)
    


@dataclass(order=True)
class Producto(Base):
    __tablename__ = 'productos'
    

    __sort_index: date = field(init=False, repr=False)

    __ID_PRODUCTO: Mapped[str] = mapped_column('ID', String)
    __NOMBRE: Mapped[str] = mapped_column('NOMBRE', String, nullable=False)
    __CADUCO: Mapped[date] = mapped_column('CADUCO', Date)
    __categoria_id: Mapped[str] = mapped_column('categoria_ID', ForeignKey('categorias.ID_CATEGORIA'), nullable=False, init=False, repr=False)
    __categoria: Mapped[Categoria] = relationship("Categoria", init=False)
    __LOTE: Mapped[str] = mapped_column('LOTE', String, nullable=False)
    __existencias: Mapped[int] = mapped_column('existencias', Integer, default=0)

    __table_args__ = (PrimaryKeyConstraint('ID', 'LOTE'),)

    def __init__(self, ID: str, NOMBRE: str, CADUCO: date, cat: Categoria, LOTE: str):
        self.__ID_PRODUCTO = ID
        self.__NOMBRE = NOMBRE
        self.__CADUCO = CADUCO
        self.__LOTE = LOTE
        self.__existencias = 0
        self.__categoria = cat
        self.__categoria_id = cat.ID_CATEGORIA


    def __post_init__(self):
        object.__setattr__(self, '__sort_index', self.__CADUCO)

    @property
    def ID(self) -> str:
        return self.__ID_PRODUCTO

    @property
    def NOMBRE(self) -> str:
        return self.__NOMBRE

    @property
    def CADUCO(self) -> str:
        return self.__CADUCO

    @property
    def categoria(self) -> str:
        return self.__categoria

    @categoria.setter
    def categoria(self, n_cat: Categoria) -> None:
        self.__categoria = n_cat
        self.__categoria_id = n_cat.ID_CATEGORIA

    @property
    def LOTE(self) -> date:
        return self.__LOTE

    @property
    def existencias(self) -> int:
        return self.__existencias

    @existencias.setter
    def existencias(self, value) -> None:
        self.__existencias = value

    def __hash__(self) -> int:
        return hash(self.__CADUCO, self.__ID_PRODUCTO, self.__NOMBRE, self.__LOTE)
