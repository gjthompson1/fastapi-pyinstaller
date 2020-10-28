from fastapi import FastAPI

from .database import engine
from .models import base

base.Base.metadata.create_all(bind=engine)

app = FastAPI()

from .routers import items, users, process

app.include_router(users.router)
app.include_router(items.router)
app.include_router(process.router)

import networkx as nx
G = nx.DiGraph()
G.add_node(1)
