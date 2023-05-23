from celery import Celery
import os
import time

Celery_app = Celery(__name__)

Celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
Celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")


@Celery_app.task(name="create_task")
def create_task(task_type):
    print("-"*25)
    print("-"*25, task_type)
    result = task_type * 10
    print("-"*25)
    time.sleep(int(result))
    print("-"*25, result)
    return result