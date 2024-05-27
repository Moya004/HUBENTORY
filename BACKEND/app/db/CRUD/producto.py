from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Producto, Categoria
from ..Schemas.modelos import ProductoCreate


def get_producto(db: Session, producto_id: str, producto_lote: str) -> Producto | None:
    return db.execute(select(Producto).where(Producto._Producto__ID_PRODUCTO == producto_id, Producto._Prodcuto.__LOTE == producto_lote)).scalar()

def create_producto(db: Session, producto: ProductoCreate) -> Producto:
    db_producto = Producto(
        ID=producto.ID,
        _Producto__CATEGORIA=producto.CATEGORIA,
        _Producto__existencias=producto.existencias,
        _Producto__LOTE=producto.LOTE,
        _Producto__NOMBRE=producto.NOMBRE,
        _Producto__CADUCO=producto.CADUCO
    )
    db.add(db_producto)
    db.commit()
    db.refresh(db_producto)
    return db_producto

def delete_producto(db: Session, producto_id: str) -> Producto | None:
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db.delete(db_producto)
        db.commit()
    return db_producto

def update_existencias(db: Session, producto_id: str, new_existencias: int) -> Producto | None:
    db_producto = get_producto(db, producto_id)
    if db_producto:
        db_producto._Producto__existencias = new_existencias
        db.commit()
        db.refresh(db_producto)
    return db_producto

def update_categoria(db: Session, producto: Producto, nueva_categoria: Categoria) -> Producto:
    producto.categoria = nueva_categoria
    db.commit()
    db.refres(producto)
    return producto

def get_productos_Categoria(db: Session, cate: Categoria):
    
    return db.execute(select(Producto).where(Producto._Producto__categoria == cate)).scalars().all()
