from fastapi import APIRouter
from ..functions.lagrange import valoresDelPolinomio as vdp

router = APIRouter()
xi=[0,6,10,13,17,20,28]
yi=[6.67,17.33,42.97,37.33,30.10,29.31,28.74]

@router.get("/lagrange")

async def diferenciasDivididas():
    pxi,pyi,polinomio,polinomioSimplificado=vdp(xi,yi)
   
    print(pxi)
    return {
        'polinomio':polinomio,
        'polinomioSimplificado':polinomioSimplificado,
        'valoresDeX':pxi,
        'valoresDey':pyi
        }
