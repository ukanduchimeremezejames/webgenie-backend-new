from fastapi import APIRouter
router = APIRouter()
jobs = {}

@router.get("/")
def list_jobs():
    return jobs
