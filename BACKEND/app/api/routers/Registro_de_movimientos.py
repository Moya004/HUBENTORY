from fastapi import APIRouter, File, UploadFile
from fastapi import Depends, HTTPException, status
from typing import List
from datetime import date
from db.Schemas.modelos import ProductoResponse, ProductoCreate
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
    

@router.put('/RM/entrada', response_model=List[ProductoResponse])
def entrada_productos(archivo: UploadFile = File(...), curr_persona = Depends(get_current_Persona), db = Depends(get_db)):
    file_ext = archivo.filename.split('.').pop()
    if file_ext != 'txt':
        raise HTTPException(status_code=400, detail="El archivo debe ser un .txt")
    
    validos = parse_file(archivo)
    to_return = []
    sin_categoria = categoria_crud.get_categoria_null(db, curr_persona.INVENTARIO)
    for valido in validos:
        in_inventario = producto_crud.get_producto(db, valido[0], valido[1])
        if not in_inventario:
            date_str = valido[3].split('/')
            fecha = date(day=int(date_str[0]), month=int(date_str[1]), year=int(date_str[2]))
            added = producto_crud.create_producto(db, ProductoCreate(NOMBRE=valido[2], ID=valido[0], LOTE=valido[1], CADUCO=fecha, ID_categoria=sin_categoria.ID_CATEGORIA), sin_categoria)
            if int(valido[4]) < 0:
                new_existencias = 0
            else:
                new_existencias = int(valido[4])
        else:
            if int(valido[4]) < 0:
                new_existencias = in_inventario.existencias
            else:
                new_existencias = int(valido[4]) + in_inventario.existencias
        
        
        added = producto_crud.update_existencias(db, in_inventario, new_existencias)
        to_return.append(ProductoResponse(NOMBRE=added.NOMBRE, CADUCO=added.CADUCO, ID_categoria=added.categoria.ID_CATEGORIA, LOTE=added.LOTE, ID=added.ID, existencias=added.existencias))
    
    return to_return 

