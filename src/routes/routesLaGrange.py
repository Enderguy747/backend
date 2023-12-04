from fastapi import APIRouter
from ..models.LaGrange import LaGrange
from ..functions.lagrange import valoresDelPolinomio as vdp

router = APIRouter()


@router.post("/lagrange")
def lagrange(coordenadas:LaGrange):
  
    pxi,pyi,polinomio,polinomioSimplificado=vdp(coordenadas.xi,coordenadas.yi)
   
    return {
        'polinomio':polinomio,
        'polinomioSimplificado':polinomioSimplificado,
        'valoresDeX':pxi,
        'valoresDey':pyi
        }
