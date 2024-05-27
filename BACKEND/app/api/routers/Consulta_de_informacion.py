from typing import List, Dict, Tuple
from fastapi import Depends, APIRouter
from db.CRUD import categoria as categoria_crud, producto as producto_crud
from db import sesion
from db.Schemas.modelos import CategoriaResponse, InventarioResponse, ProductoResponse
from db.Schemas.seguridad import PersonaResponse
from security.autenticacion import get_current_Persona

router = APIRouter()

@router.get('/me', response_model=PersonaResponse)
async def persona_me(curr_persona = Depends(get_current_Persona)):
    response = PersonaResponse(ID_persona=curr_persona.ID_PERSONA, Id_inventrio=curr_persona.INVENTARIO.ID_INVENTARIO, Jerarquia=curr_persona.JERARQUIA, nombre_completo=curr_persona.NOMBRE_COMPLETO, email=curr_persona.EMAIL)
    return response


@router.get('/me/Inventario', response_model=InventarioResponse)
def inventario_me(curr_persona = Depends(get_current_Persona)):
    inve = curr_persona.INVENTARIO
    return InventarioResponse(Nombre=inve.NOMBRE, ID_inventrio=inve.ID_INVENTARIO)

@router.get('/me/Categorias', response_model=List[CategoriaResponse])
def categorias_me(curr_per = Depends(get_current_Persona), db = Depends(sesion.get_db)):
    categorias = categoria_crud.get_categorias(db, curr_per.INVENTARIO)
    response = []
    for categoria in categorias:
        response.append(CategoriaResponse(Nombre=categoria.nombre, ID_inventario=categoria.INVENTARIO.ID_INVENTARIO, ID_categoria=categoria.ID_CATEGORIA))
    return response

@router.get('/me/productos_por_categoria', response_model=Dict[str, Tuple[ProductoResponse, ...]])
def productos_me(curr_per = Depends(get_current_Persona), db = Depends(sesion.get_db)):
    categorias = categoria_crud.get_categorias(db, curr_per.INVENTARIO)
    to_return = {}
    for categoria in categorias:
        productos = producto_crud.get_productos_Categoria(db, categoria)
        key = categoria.nombre
        value = []
        for producto in productos:
            value.append(ProductoResponse(ID=producto.ID, NOMBRE=producto.NOMBRE, CADUCO=producto.CADUCO, existencias=producto.existencias, LOTE=producto.LOTE))
        to_return[key] = tuple(value)
    
    return to_return