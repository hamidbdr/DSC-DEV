from typing import Union

from fastapi import FastAPI, Body
from fastapi.responses import JSONResponse

from celery_worker.worker_tasks import create_task, Celery_app, task_with_progression
from celery.result import AsyncResult

app = FastAPI()

@app.post("/tasks", status_code=201)
def run_task(payload = Body(...)):
    task_type = payload["type"]
    print(task_type)
    print("-"*25)
    task = create_task.delay(int(task_type))
    task_p = task_with_progression.delay()
    
    return {"task_id": task.id,
           "task_id_p": task_p.id
            }

@app.get("/tasks/{task_id}")
def get_status(task_id):
    task_result = AsyncResult(task_id, app=Celery_app)

    result = {
        "task_id": task_id,
        "task_status": task_result.status,
        "task_result": task_result.result

    }
    return result

@app.get("/")
def read_root():
    return {"sanity check": "ok"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}

