from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Categoria, Inventario
from ..Schemas.modelos import CategoriaCreate, CategoriaUpdateNombre
import uuid

def get_categoria(db: Session, categoria_nombre: str) -> Categoria | None:
    return db.execute(select(Categoria).where(Categoria._Categoria__nombre == categoria_nombre))

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

def update_nombre(db: Session, Cate:Categoria, categoria_update: CategoriaUpdateNombre) -> Categoria | None:
    Cate.nombre = categoria_update.Nombre
    db.commit()
    db.refresh(Cate)
    return Cate

def get_categorias(db: Session, inve: Inventario):
    return db.execute(select(Categoria).where(Categoria._Categoria__INVENTARIO_ID == inve._Inventario__ID_INVENTARIO)).scalars().all()
