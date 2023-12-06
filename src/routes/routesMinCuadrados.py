from fastapi import APIRouter
from ..functions.minCuadrados import minCuadrados as mc
from ..models.MinCuadrados import MinCuadrados

router = APIRouter()

@router.post("/mincuadrados")
def minimosCuadrados(body:MinCuadrados):
 
    ecuation = mc(body.xAxis,body.yAxis,body.Parabola)
   
    return {
        'EcuacionRecta':ecuation,
        }