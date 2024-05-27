from fastapi import APIRouter
from fastapi import Depends, HTTPException, status
from db.Schemas.modelos import InventarioUpdateNombre, CategoriaResponse, InventarioResponse, CategoriaCreate, ProductoUpdateCategoria, ProductoResponse
from security.autenticacion import get_current_Persona
from db.CRUD import inventario as inventario_crud, categoria as categoria_crud, producto as producto_crud
from db.sesion import get_db

router = APIRouter()

@router.put('/AEI/modificar/inventario', response_model=InventarioResponse)
def update_nombre_inventario(update_nombre: InventarioUpdateNombre, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    inve = curr_persona.INVENTARIO
    result = inventario_crud.update_nombre(db, inve, update_nombre.Nombre)
    return InventarioResponse(Nombre=result.NOMBRE, ID_inventrio=result.ID_INVENTARIO)

@router.post('/AEI/agregar/categoria', response_model=CategoriaResponse)
def create_categoria(nueva_categoria: str, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    inve = curr_persona.INVENTARIO
    if categoria_crud.get_categoria(db, nueva_categoria, inve):
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail="Esta categoria ya existe.",
        )
    result = categoria_crud.create_categoria(db, CategoriaCreate(Nombre=nueva_categoria, ID_inventario=inve.ID_INVENTARIO), inve)
    return CategoriaResponse(Nombre=result.nombre, ID_inventario=result.INVENTARIO.ID_INVENTARIO, ID_categoria=result.ID_CATEGORIA)

@router.put('/AEI/modificar/categoria/{nombre_categoria}', response_model=CategoriaResponse)
def update_nombre_inventario(nombre_categoria:str, update_nombre: str, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    categoria = categoria_crud.get_categoria(db, nombre_categoria, curr_persona.INVENTARIO)
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoria no existe en inventario")
    result = categoria_crud.update_nombre(db, categoria, update_nombre)
    return CategoriaResponse(Nombre=result.nombre, ID_inventario=result.INVENTARIO.ID_INVENTARIO, ID_categoria=result.ID_CATEGORIA)

@router.delete('/AEI/eliminar/categoria/{nombre_categoria}', response_model=CategoriaResponse)
def delete_categoria(nombre_categoria:str, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    categoria = categoria_crud.get_categoria(db, nombre_categoria, curr_persona.INVENTARIO)
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoria no existe en inventario")
    no_categoria = categoria_crud.get_categoria_null(db, curr_persona.INVENTARIO)
    related_products = producto_crud.get_productos_Categoria(db, categoria)
    if related_products:
        for producto in related_products:
            producto_crud.update_categoria_producto(db, producto, no_categoria)
    result = categoria_crud.delete_categoria(db, categoria)
    return CategoriaResponse(Nombre=result.nombre, ID_inventario=result.INVENTARIO.ID_INVENTARIO, ID_categoria=result.ID_CATEGORIA)


@router.put('/AEI/modificar/producto/', response_model=ProductoResponse)
def update_categoria_producto(modificado: ProductoUpdateCategoria, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    in_inventario = producto_crud.get_producto(db, modificado.ID, modificado.LOTE, curr_persona.INVENTARIO.ID_INVENTARIO)
    if not in_inventario:
        raise HTTPException(status_code=404, detail="el producto no se encuentra en inventario")
    categoria = categoria_crud.get_categoria(db, modificado.nombre_categoria, curr_persona.INVENTARIO)
    if not categoria:
        raise HTTPException(status_code=404, detail="La categoria no existe en inventario")
    result = producto_crud.update_categoria_producto(db, in_inventario, categoria)
    return ProductoResponse(ID=result.ID, NOMBRE=result.NOMBRE, CADUCO=result.CADUCO, LOTE=result.LOTE, existencias=result.existencias)