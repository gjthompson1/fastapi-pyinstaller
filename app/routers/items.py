from typing import List

from fastapi import Depends
from sqlalchemy.orm import Session

from app import crud, schemas
from app.database import get_db

from fastapi import APIRouter

router = APIRouter()

@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items
