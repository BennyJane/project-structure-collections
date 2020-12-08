# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : project-structure-collections
# Time       ：2020/12/8 15:16
# Warning    ：The Hard Way Is Easier
from .celery_core import app


@app.task
def add(x, y):
    return x + y


@app.task
def mul(x, y):
    return x * y


@app.task
def xsum(numbers):
    return sum(numbers)
