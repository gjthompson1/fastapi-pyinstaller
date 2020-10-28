from fastapi import Depends
from sqlalchemy.orm import Session

from app.models import Process
from app.database import get_db
import time

from fastapi import APIRouter

router = APIRouter()

import asyncio
from concurrent.futures import ProcessPoolExecutor

def cpu_bound_func(param):
    time.sleep(param)  # Pretend this is expensive calculations
    return param + 1

async def do_cpu_task(param: int):
    loop = asyncio.get_event_loop()
    executor = ProcessPoolExecutor()
    print("task finished")
    return await loop.run_in_executor(executor, cpu_bound_func, param)  # wait result


@router.get("/process/start")
def start_process(db: Session = Depends(get_db)):

    process = Process(counter=1)
    db.add(process)
    db.commit()

    return {"ping": "pong"}

@router.get("/process/cancel")
def cancel_process(db: Session = Depends(get_db)):

    process = Process(counter=1)
    db.add(process)
    db.commit()

    return {"ping": "pong"}
