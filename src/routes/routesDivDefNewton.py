from fastapi import APIRouter
from ..functions.divDefNewton import divididasDiferenciasNewton as ddn

router = APIRouter()
m=[18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33]
n=[16,22,12,13,10,8,8,6,7,5,6,4,3,42,2,2]

@router.get("/newtondd")

async def diferenciasDivididas():
    p , simplificated ,termValues  = ddn(m,n)
   
   
    return {
        'polinomio':p,
        'polinomioSimplificado':simplificated,
        'valores':termValues
        }
