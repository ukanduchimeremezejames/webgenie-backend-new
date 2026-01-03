from fastapi import APIRouter
from app.services.network_engine import generate_network_graph

router = APIRouter()

@router.get("/graph")
def graph():
    return generate_network_graph()
