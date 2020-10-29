from fastapi import Depends, Body
from sqlalchemy.orm import Session

# from app.run_state import run_state
from app.database import get_db, SessionLocal
from app import models
import time

from fastapi import APIRouter

import multiprocessing as mp

router = APIRouter()

run_process = None
run_state = None

# import asyncio
# from concurrent.futures import ProcessPoolExecutor

def cpu_bound_func(param, run_state):
    run_state['node'] = 'running'

    db = SessionLocal()
    process = db.query(models.Process).get(1)
    process.counter = param
    process.run_state = 'running'
    db.add(process)
    db.commit()

    time.sleep(param)  # Pretend this is expensive calculations

    process.run_state = 'completed'
    db.add(process)
    db.commit()

    run_state['node'] = 'completed'

    return param + 1

@router.post("/process/start")
def start_process(counter: int = Body(...), db: Session = Depends(get_db)):

    global run_process, run_state

    process = db.query(models.Process).get(1)
    if not process:
        process = models.Process()
    db.add(process)
    db.commit()

    run_state = mp.Manager().dict()
    run_process = mp.Process(target=cpu_bound_func, args=(counter, run_state))
    run_process.start()
    run_process.join()

    return run_state.copy()

@router.get("/process/cancel")
def cancel_process(db: Session = Depends(get_db)):

    global run_process

    run_process.terminate()
    run_process.join()
    run_state['node'] = 'canceled'

    process = db.query(models.Process).get(1)
    process.run_state = 'canceled'
    db.add(process)
    db.commit()

    return run_state.copy()


@router.get("/process/get-state")
def get_state():
    return run_state.copy()

