# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : project-structure-collections
# Time       ：2020/12/8 15:16
# Warning    ：The Hard Way Is Easier
from celery import Celery

app = Celery(broker='redis://localhost:6379/0')


@app.task
def add(x, y):
    print(x + y)
    return x + y
