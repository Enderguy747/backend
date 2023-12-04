from pydantic import BaseModel

class LaGrange(BaseModel):
    xi:list[int]
    yi:list[int]
    
