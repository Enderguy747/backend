from pydantic import BaseModel

class PuntoFijo(BaseModel):
    originalFunction:str
    clearedFunction:str
    initialPoint:int
    tolerance:float