from fastapi import APIRouter
from ..models.LaGrange import LaGrange
from ..functions.lagrange import valoresDelPolinomio as vdp

router = APIRouter()
##ejemplo de query
##xi=[0,6,10,13,17,20,28]
##yi=[6.67,17.33,42.97,37.33,30.10,29.31,28.74]

@router.post("/lagrange")
def diferenciasDivididas(coordenadas:LaGrange):
  
    pxi,pyi,polinomio,polinomioSimplificado=vdp(coordenadas.xi,coordenadas.yi)
   
    return {
        'polinomio':polinomio,
        'polinomioSimplificado':polinomioSimplificado,
        'valoresDeX':pxi,
        'valoresDey':pyi
        }
