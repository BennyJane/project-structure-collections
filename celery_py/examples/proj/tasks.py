import time

from .celery_ext import app


@app.task
def core_task():
    print(' == task start ==')
    time.sleep(5)
    print('== task end ==')
