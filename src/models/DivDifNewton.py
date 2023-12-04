from pydantic import BaseModel


class DivDifNewton(BaseModel):
    xAxis:list[int]
    yAxis:list[int]