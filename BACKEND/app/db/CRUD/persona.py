from sqlalchemy.orm import Session
from security.modelos_seguridad import Persona
from ..Schemas.modelos import InventarioCreate, CategoriaCreate
from ..Schemas.seguridad import PersonaCreate
from security.verificacion_credenciales import get_password_hash
from .inventario import get_inventario, create_inventario
from .categoria import create_categoria

def get_persona(db: Session, persona_id: str) -> Persona | None:
    return db.query(Persona).filter(Persona._Persona__ID_PERSONA == persona_id).scalar()

def create_persona(db: Session, persona: PersonaCreate) -> Persona:
    # Verificar si el inventario existe
    inventario = get_inventario(db, persona.Id_inventrio)

    if not inventario:
        # Crear el inventario si no existe
        inventario = create_inventario(db, InventarioCreate(ID_inventrio=persona.Id_inventrio, Nombre="Inventario Default"))
        
        # Crear categorías 'no_categoria' y 'retirado'
        create_categoria(db, CategoriaCreate(ID_inventario=inventario.ID_INVENTARIO, Nombre='sin_categoria'), inventario)
        create_categoria(db, CategoriaCreate(ID_inventario=inventario.ID_INVENTARIO, Nombre='retirado'), inventario)
    
    # Crear la persona
    hashed_password = get_password_hash(persona.Contraseña)
    db_persona = Persona(
        idp=persona.ID_persona,
        inv=inventario,
        jer=persona.Jerarquia,
        nom=persona.nombre_completo,
        mail=persona.email,
        contra=hashed_password
    )
    db.add(db_persona)
    db.commit()
    db.refresh(db_persona)
    
    return db_persona

def delete_persona(db: Session, persona_id: str) -> Persona | None:
    db_persona = get_persona(db, persona_id)
    if db_persona:
        db.delete(db_persona)
        db.commit()
    return db_persona

def update_password(db: Session, db_persona: Persona, new_password: str) -> Persona:

    db_persona._Persona__password = get_password_hash(new_password)
    db.commit()
    db.refresh(db_persona)
    return db_persona

def get_personas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Persona).offset(skip).limit(limit).all()
