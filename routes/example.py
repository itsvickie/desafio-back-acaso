from fastapi import APIRouter

router = APIRouter(prefix="/example")

@router.get("")
async def hellow():
    return {"Hellow": "Vickie"}