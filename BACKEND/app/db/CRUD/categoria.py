from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Categoria, Inventario
from ..Schemas.modelos import CategoriaCreate
import uuid

def get_categoria(db: Session, categoria_nombre: str, id_inventario: Inventario) -> Categoria | None:
    return db.execute(select(Categoria).where(Categoria._Categoria__nombre == categoria_nombre, Categoria._Categoria__INVENTARIO_ID == id_inventario._Inventario__ID_INVENTARIO)).scalar()

def get_categoria_null(db: Session, inv: Inventario) -> Categoria:
    return db.execute(select(Categoria).where(Categoria._Categoria__nombre == 'sin_categoria', Categoria._Categoria__INVENTARIO_ID == inv._Inventario__ID_INVENTARIO)).scalar()

def get_categoria_expired(db: Session, inv: Inventario) -> Categoria:
    return db.execute(select(Categoria).where(Categoria._Categoria__nombre == 'retirado', Categoria._Categoria__INVENTARIO_ID == inv._Inventario__ID_INVENTARIO)).scalar()

def create_categoria(db: Session, categoria: CategoriaCreate, inv: Inventario) -> Categoria:
    db_categoria = Categoria(
        id_cat=str(uuid.uuid4()),
        inve=inv,
        nom=categoria.Nombre
    )
    db.add(db_categoria)
    db.commit()
    db.refresh(db_categoria)
    return db_categoria

def update_nombre(db: Session, Cate:Categoria, categoria_update: str) -> Categoria | None:
    if Cate.nombre == 'sin_categoria' or Cate.nombre == 'retirado':
        return None
    Cate.nombre = categoria_update
    db.commit()
    db.refresh(Cate)
    return Cate

def delete_categoria(db: Session, Cate: Categoria) -> Categoria | None:
    if Cate.nombre == 'sin_categoria' or Cate.nombre == 'retirado':
        return None
    db.delete(Cate)
    db.commit()
    return Cate

def get_categorias(db: Session, inve: Inventario):
    return db.execute(select(Categoria).where(Categoria._Categoria__INVENTARIO_ID == inve._Inventario__ID_INVENTARIO)).scalars().all()
