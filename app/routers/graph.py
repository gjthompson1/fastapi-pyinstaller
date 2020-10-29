from fastapi import Depends, Body
from sqlalchemy.orm import Session

from app.graph import G
from app.database import get_db

from fastapi import APIRouter

router = APIRouter()

@router.post("/graphs")
def create_item_for_user(node_id: int = Body(...)):
    G.add_node(node_id)
    return {'nodes': G.nodes}


@router.get("/graph/get_nodes")
def get_nodes(db: Session = Depends(get_db)):
    return {'nodes': G.nodes}
