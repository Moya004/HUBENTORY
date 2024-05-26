from sqlalchemy import select
from sqlalchemy.orm import Session
from models.modelos import Inventario
from ..Schemas.modelos import InventarioCreate

def get_inventario(db: Session, inventario_id: str) -> Inventario | None:
    return db.execute(select(Inventario).where(Inventario._Inventario__ID_INVENTARIO == inventario_id)).scalar()

def create_inventario(db: Session, inventario: InventarioCreate) -> Inventario:
    db_inventario = Inventario(
        id_inv=inventario.ID_inventrio,
        name=inventario.Nombre
    )
    db.add(db_inventario)
    db.commit()
    db.refresh(db_inventario)
    return db_inventario

def get_inventarios(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Inventario).offset(skip).limit(limit).all()
