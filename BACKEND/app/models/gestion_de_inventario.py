from dataclasses import dataclass, field
from datetime import date
from sqlalchemy import PrimaryKeyConstraint, String, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from db.Session import Base



@dataclass(frozen=True)
class Inventario(Base):
    __tablename__ = 'inventarios'
    __slots__ = ['__ID_INVENTARIO', '__NOMBRE']

    __ID_INVENTARIO: Mapped[str] = mapped_column('ID_INVENTARIO', String, primary_key= True)
    __NOMBRE: Mapped[str] = mapped_column('NOMBRE', String)

    @property
    def ID_INVENTARIO(self) -> str:
        return self.__ID_INVENTARIO
    
    @property
    def NOMBRE(self) -> str:
        return self.__NOMBRE
    
    def __del__(self) -> None: ...

    def __hash__(self) -> int: ...

@dataclass
class Categoria(Base):
    __tablename__ = 'categorias'
    __table_args__ = (PrimaryKeyConstraint('__ID_CATEGORIA', '__INVENTARIO_ID'))
    __slots__ = ['__ID_CATEGORIA', '__nombre', '__INVENTARIO_ID', '__INVENTARIO']

    __ID_CATEGORIA: Mapped[str] = mapped_column('ID_CATEGORIA', String)
    __nombre: Mapped[str] = mapped_column('ID_CATEGORIA', String)
    __INVENTARIO_ID: Mapped[str] = mapped_column(String, ForeignKey('inventarios.ID_INVENTARIO'), nullable=False, repr=False, init=False)
    __INVENTARIO: Mapped[Inventario] = relationship('Inventario')

    def __init__(self, nom: str, id_cat: str, inve: Inventario) -> None:
        object.__setattr__(self, '__ID_categoria', id_cat)
        object.__setattr__(self, '__INVENTARIO', inve)
        object.__setattr__(self, '__INVENTARIO_ID', inve.ID_INVENTARIO)

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
    
    def __del__(self) -> None: ...


@dataclass(order=True)
class Producto(Base):
    __slots__ = ['__ID_PRODUCTO', '__NOMBRE', '__CADUCO', '__CATEGORIA', '__LOTE', '__existencias', '__sort_index']
    __tablename__ = 'productos'
    __table_args__ = (PrimaryKeyConstraint('__ID', '__LOTE', '__CATEGORIA_id'),)

    __sort_index: date = field(init=False, repr=False)

    __ID_PRODUCTO: Mapped[str] = mapped_column('ID', String)
    __NOMBRE: Mapped[str] = mapped_column('NOMBRE', String, nullable=False)
    __CADUCO: Mapped[date] = mapped_column('CADUCO', Date, nullable=False)
    __CATEGORIA_ID: Mapped[str] = mapped_column(ForeignKey('categorias.__ID_categoria'), nullable=False, init=False, repr=False)
    __CATEGORIA: Mapped[Categoria] = relationship("Categoria", init=False)
    __LOTE: Mapped[str] = mapped_column('LOTE', String, nullable=False)
    __existencias: Mapped[int] = mapped_column('existencias', Integer, default=0)

    def __init__(self, ID: str, NOMBRE: str, CADUCO: date, CATEGORIA: Categoria, LOTE: str):
        object.__setattr__(self, '__ID_PRODUCTO', ID)
        object.__setattr__(self, '__NOMBRE', NOMBRE)
        object.__setattr__(self, '__CADUCO', CADUCO)
        object.__setattr__(self, '__CATEGORIA', CATEGORIA)
        object.__setattr__(self, '__CATEGORIA_id', CATEGORIA.ID_categoria)
        object.__setattr__(self, '__LOTE', LOTE)
        
        self.__existencias = 0

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
    def CATEGORIA(self) -> str:
        return self.__CATEGORIA

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
        return hash(self.__CADUCO, self.__ID_PRODUCTO, self.__NOMBRE, self.__LOTE, self.__CATEGORIA_ID)
    
    def __del__(self) -> None: ...