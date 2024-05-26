from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Categoria, Inventario
from ..Schemas.modelos import CategoriaCreate
import uuid

def get_categoria(db: Session, categoria_id: str) -> Categoria | None:
    return db.execute(select(Categoria).where(Categoria._Categoria__ID_CATEGOARIA == categoria_id))

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

def get_categorias(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Categoria).offset(skip).limit(limit).all()
