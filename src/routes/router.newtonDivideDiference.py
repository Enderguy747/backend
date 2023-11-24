from fastapi import APIRouter

router = APIRouter()


@router.get("/newtondd")
async def getNewtonDivideDifference():
    return {"fd"}

