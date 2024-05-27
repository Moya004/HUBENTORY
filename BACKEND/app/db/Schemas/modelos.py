from pydantic import BaseModel
from datetime import date

class ProductoBase(BaseModel):
    NOMBRE: str
    CADUCO: date
    LOTE: str

class ProductoCreate(ProductoBase):
    ID: str
    ID_categoria: str

class ProductoUpdateExistensias(ProductoBase):
    ID: str
    existencias: int

class ProductoUpdateCategoria(ProductoBase):
    ID_categoria: str

class ProductoResponse(ProductoBase):
    ID: str
    existencias: int
    class Config:
        from_attributes = True

class CategoriaBase(BaseModel):
    Nombre: str
    ID_inventario: str


class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    ID_categoria: str
    class Config:
        from_attributes = True

class InventarioBase(BaseModel):
    Nombre: str

class InventarioUpdateNombre(InventarioBase):
    pass

class InventarioCreate(InventarioBase):
    ID_inventrio: str

class InventarioResponse(InventarioBase):
    ID_inventrio: str
    class Config:
        from_attributes = True
