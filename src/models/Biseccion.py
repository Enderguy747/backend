from pydantic import BaseModel

class Biseccion(BaseModel):
    funcion_str:str
    intervalo_inicial:float
    intervalo_final:float 
    tolerancia:float