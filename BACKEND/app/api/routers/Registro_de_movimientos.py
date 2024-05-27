from fastapi import APIRouter, File, UploadFile
from fastapi import Depends, HTTPException, status
from typing import List
from datetime import date
from db.Schemas.modelos import ProductoResponse, ProductoCreate, ProductoUpdateExistensias
from security.autenticacion import get_current_Persona
from db.CRUD import categoria as categoria_crud, producto as producto_crud
from db.sesion import get_db

router = APIRouter()

def parse_file(entrada: File) -> list[tuple]:
    import re
    parsed = []
    fecha = r'(?:3[01]|[12][0-9]|0?[1-9])(\/)(0?[1-9]|1[1-2])(\/)\d{4}'
    renglon_valido = re.compile(r'^(\w+;\w+;\w+;(no|{});\-?\d+)$'.format(fecha))
    
    lineas = entrada.file.read().decode('utf-8').splitlines()
    for line in lineas:
        if renglon_valido.match(line):
            parsed.append(tuple(line.strip().split(';')))
        
    
    return parsed
    

@router.post('/RM/entrada', response_model=List[ProductoResponse])
def entrada_productos(archivo: UploadFile = File(...), curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    file_ext = archivo.filename.split('.').pop()
    if file_ext != 'txt':
        raise HTTPException(status_code=400, detail="El archivo debe ser un .txt")
    
    validos = parse_file(archivo)
    to_return = []
    sin_categoria = categoria_crud.get_categoria_null(db, curr_persona.INVENTARIO)
    for valido in validos:
        in_inventario = producto_crud.get_producto(db, valido[0], valido[1], curr_persona.INVENTARIO.ID_INVENTARIO)
        if not in_inventario:
            if len(valido[3]) != 2:
                date_str = valido[3].split('/')
                fecha = date(day=int(date_str[0]), month=int(date_str[1]), year=int(date_str[2]))
            else:
                fecha = None
            added = producto_crud.create_producto(db, ProductoCreate(NOMBRE=valido[2], ID=valido[0], LOTE=valido[1], CADUCO=fecha, ID_categoria=sin_categoria.ID_CATEGORIA, existencias=0), sin_categoria)
            if int(valido[4]) < 0:
                new_existencias = 0
            else:
                new_existencias = int(valido[4])
        else:
            if int(valido[4]) < 0:
                new_existencias = in_inventario.existencias
            else:
                new_existencias = int(valido[4]) + in_inventario.existencias
        
        if in_inventario:
            result = producto_crud.update_existencias(db, in_inventario, new_existencias)
        else:
            result = producto_crud.update_existencias(db, added, new_existencias)
        to_return.append(ProductoResponse(NOMBRE=result.NOMBRE, CADUCO=result.CADUCO, ID_categoria=result.categoria.ID_CATEGORIA, LOTE=result.LOTE, ID=result.ID, existencias=result.existencias))
    
    return to_return 

@router.put('/RM/retiro', response_model=List[ProductoResponse])
def terminate_productos(curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    expirado = categoria_crud.get_categoria_expired(db, curr_persona.INVENTARIO)
    productos_inv = producto_crud.get_productos(db, curr_persona.INVENTARIO.ID_INVENTARIO)
    result = []
    hoy = date.today()
    for producto in productos_inv:
        if producto.CADUCO:
            if producto.CADUCO <= hoy:
                result.append(producto_crud.update_categoria_producto(db, producto, expirado))
        else:
            continue
    if not productos_inv:
        raise HTTPException(status_code=400, detail="el inventario no tiene productos")
    result = list(map(lambda x: ProductoResponse(NOMBRE=x.NOMBRE, CADUCO=x.CADUCO, ID_categoria=x.categoria.ID_CATEGORIA, LOTE=x.LOTE, ID=x.ID, existencias=x.existencias), result))
    return productos_inv


@router.put('/RM/salida', response_model=ProductoResponse)
def salidad_producto(saliente: ProductoUpdateExistensias, curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    in_inventario = producto_crud.get_producto(db, saliente.ID, saliente.LOTE, curr_persona.INVENTARIO.ID_INVENTARIO)
    if not in_inventario:
        raise HTTPException(status_code=404, detail="El producto no existe")
    hoy = date.today()
    if in_inventario.CADUCO <= hoy:
        raise HTTPException(status_code=400, detail="El producto esta expirado")

    remain = in_inventario.existencias - saliente.existencias
    if remain < 0:
        raise HTTPException(status_code=400, detail="no hay suficientes existencias")
    
    result = producto_crud.update_existencias(db, in_inventario, remain)
    return ProductoResponse(NOMBRE=result.NOMBRE, CADUCO=result.CADUCO, LOTE=result.LOTE, ID= result.ID, existencias=result.existencias)
