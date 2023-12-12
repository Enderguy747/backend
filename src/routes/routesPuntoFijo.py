from fastapi import APIRouter
from ..functions.puntoFijo import puntoFijo as pf
from ..models.PuntoFijo import PuntoFijo

router = APIRouter()

@router.post("/mincuadrados")
def minimosCuadrados(body:PuntoFijo):
 
    ecuation = mc(body.xAxis,body.yAxis,body.Parabola)
   
    return {
        'EcuacionRecta':ecuation,
        }