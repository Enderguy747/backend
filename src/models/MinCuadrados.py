from typing import Optional
from pydantic import BaseModel

class MinCuadrados(BaseModel):
    xAxis:list[int]
    yAxis:list[int]
    Parabola:int