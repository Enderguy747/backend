##this is an example how router works

from fastapi import APIRouter

router = APIRouter()

@router.post("/index/{name}")
async def readParams(name):
        return {"nombre":name}


@router.get("/indexx")
async def printHello():
        return "hello"