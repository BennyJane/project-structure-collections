# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : celery_docx
# Time       ：2020/12/8 22:13
# Warning    ：The Hard Way Is Easier

from demo2.celery import app


@app.task
def add(x, y):
    print(x + y)
    return x + y
