from fastapi import APIRouter
from ..functions.biseccion import biseccion
from ..models.Biseccion import Biseccion

router = APIRouter()

@router.post("/biseccion")
def diferenciasDivididasNewton(body:Biseccion):
    
    iteraciones = biseccion(body.funcion_str, body.intervalo_inicial, body.intervalo_final, body.tolerancia)
   
    return {
       "teraciones":iteraciones
        }
