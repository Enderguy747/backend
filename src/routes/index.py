##this is an example how router works
''''
from fastapi import APIRouter
from ..functions.hello import sayYourName

router = APIRouter()

@router.get("/items/{name}")
async def readParams(name: str):
        return {"router works": "ok", "status": sayYourName(name)}
'''
