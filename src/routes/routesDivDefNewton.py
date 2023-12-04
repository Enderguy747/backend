from fastapi import APIRouter
from ..functions.divDefNewton import divDifNewton as ddn
from ..models.DivDifNewton import DivDifNewton

router = APIRouter()

@router.post("/newtondd")
def diferenciasDivididasNewton(coordenadas:DivDifNewton):
    
    polinomio , simplificated ,termValues  = ddn(coordenadas.xAxis,coordenadas.yAxis)
   
    return {
        'polinomio':polinomio,
        'polinomioSimplificado':simplificated,
        'valores':termValues
        }
