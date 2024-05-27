from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Producto, Categoria
from ..Schemas.modelos import ProductoCreate


def get_producto(db: Session, producto_id: str, producto_lote: str) -> Producto | None:
    return db.execute(select(Producto).where(Producto._Producto__ID_PRODUCTO == producto_id, Producto._Producto__LOTE == producto_lote)).scalar()

def create_producto(db: Session, producto: ProductoCreate, no_categoria: Categoria) -> Producto:
    db_producto = Producto(
        ID=producto.ID,
        cat=no_categoria,
        LOTE=producto.LOTE,
        NOMBRE=producto.NOMBRE,
        CADUCO=producto.CADUCO
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

def update_existencias(db: Session, producto: Producto, new_existencias: int) -> Producto :
    
    producto.existencias = new_existencias
    db.commit()
    db.refresh(producto)
    return producto

def update_categoria_producto(db: Session, producto: Producto, nueva_categoria: Categoria) -> Producto:
    producto.categoria = nueva_categoria
    db.commit()
    db.refres(producto)
    return producto

def get_productos_Categoria(db: Session, cate: Categoria):
    
    return db.execute(select(Producto).where(Producto._Producto__categoria == cate)).scalars().all()
