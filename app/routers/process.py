from fastapi import Depends, Body
from sqlalchemy.orm import Session

# from app.run_state import run_state
from app.database import get_db, SessionLocal
import time
import json

from fastapi import APIRouter

import multiprocessing as mp

router = APIRouter()

run_process = None
run_state = None

# import asyncio
# from concurrent.futures import ProcessPoolExecutor

def cpu_bound_func(param, run_state):
    run_state['node'] = 'running'
    time.sleep(param)  # Pretend this is expensive calculations
    run_state['node'] = 'completed'

    # db = SessionLocal()
    # process = db.query(Process).get(1)
    # process.counter = param
    # db.add(process)
    # db.commit()

    return param + 1

# async def do_cpu_task(param: int):
#     loop = asyncio.get_event_loop()
#     executor = ProcessPoolExecutor()
#     result = await loop.run_in_executor(executor, cpu_bound_func, param)
#     print('Task finished')
#     return result


# @router.post("/process/start")
# async def start_process(counter: int = Body(...), db: Session = Depends(get_db)):
#     res = await do_cpu_task(counter)
#     return {"message": f"Result {res}"}

@router.post("/process/start")
def start_process(counter: int = Body(...), db: Session = Depends(get_db)):

    global run_process, run_state

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
    run_state['node'] = 'failed'

    return run_state.copy()


@router.get("/process/get-state")
def get_state():
    return run_state.copy()
