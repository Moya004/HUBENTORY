from pydantic import BaseModel
from datetime import date

class ProductoBase(BaseModel):
    NOMBRE: str
    CADUCO: date
    ID_categoria: str
    LOTE: str
    existencias: int

class ProductoCreate(ProductoBase):
    ID: str

class ProductoUpdate(BaseModel):
    existencias: int

class ProductoResponse(ProductoBase):
    ID: str
    class Config:
        from_attributes = True

class CategoriaBase(BaseModel):
    Nombre: str
    ID_inventario: str

class CategoriaUpdateNombre(CategoriaBase):
    pass

class CategoriaCreate(CategoriaBase):
    pass

class CategoriaResponse(CategoriaBase):
    ID_categoria: str
    class Config:
        from_attributes = True

class InventarioBase(BaseModel):
    Nombre: str

class InventarioCreate(InventarioBase):
    ID_inventrio: str

class InventarioResponse(InventarioBase):
    ID_inventrio: str
    class Config:
        from_attributes = True
