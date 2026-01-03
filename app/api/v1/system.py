from fastapi import APIRouter
from app.services.beeline_sync import sync_beeline

router = APIRouter()

@router.post("/sync-beeline")
async def sync():
    return await sync_beeline()
