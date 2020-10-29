from fastapi import FastAPI

from .database import engine
from .models import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI()

from .routers import items, users, process, graph

app.include_router(users.router)
app.include_router(items.router)
app.include_router(process.router)
app.include_router(graph.router)
