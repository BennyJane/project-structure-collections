# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : celery_docx
# Time       ：2020/12/8 15:58
# Warning    ：The Hard Way Is Easier

from celery import Celery

app = Celery(__name__,
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             )

app.config_from_object("demo2.config")

