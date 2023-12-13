from fastapi import APIRouter
from ..functions.puntoFijo import puntoFijo as pf
from ..models.PuntoFijo import PuntoFijo

router = APIRouter()

@router.post("/puntofijo")
def minimosCuadrados(body:PuntoFijo):
 
    valor_iteracion,error_actual,iteracion_actual,iteraciones =pf(body.originalFunction, body.clearedFunction, body.initialPoint, body.tolerance)
   ## 
   
    return {
            'valorIteracion':valor_iteracion,
            'errorActual':error_actual,
            'iteracionActual':iteracion_actual,
            'iteraciones':str(iteraciones)
            }
 