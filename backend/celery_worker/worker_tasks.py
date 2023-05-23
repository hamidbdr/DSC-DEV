from celery import Celery
import os
import time

Celery_app = Celery(__name__)

Celery_app.conf.broker_url = os.environ.get("CELERY_BROKER_URL", "redis://redis:6379")
Celery_app.conf.result_backend = os.environ.get("CELERY_RESULT_BACKEND", "redis://redis:6379")


@Celery_app.task(name="create_task",bind=True)
def create_task(self, task_type):
    print("-"*25)
    print("-"*25, task_type)
    result = task_type * 10
    print("-"*25)
    #n = 60
    #for i in range(0, n):
    #    print(i)
    #    self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
    #    time.sleep(1)    
    
    time.sleep(int(result))
    print("-"*25, result)
    
    return result

@Celery_app.task(name="task_with_progression",bind=True)
def task_with_progression(self):
    n = 60
    for i in range(0, n):
        print(i)
        self.update_state(state='PROGRESS', meta={'done': i, 'total': n})
        time.sleep(1)
    return n