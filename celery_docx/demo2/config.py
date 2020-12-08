# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : celery_docx
# Time       ：2020/12/8 15:58
# Warning    ：The Hard Way Is Easier
from celery.schedules import crontab

broker_url = 'redis://127.0.0.1:6379/0'
result_backend = 'redis://127.0.0.1:6379/0'

task_serializer = 'json'
result_serializer = 'json'
accent_serializer = 'json'
timezone = 'Asia/Shanghai'
worker_hijack_root_logger = False  # celery默认开启自己的日志，可关闭自定义日志，不关闭自定义日志输出为空
result_expires = 60 * 60 * 24  # 存储结果过期时间（默认1天）

# 导入任务所咋模块
imports = [
    "demo2.periodic_tasks.tasks"
]

# 导入定时任务所在模块
beat_schedule = {
    "task1": {
        "task": "demo2.periodic_tasks.tasks.add",
        "schedule": crontab(minute="*/1"),
        "args": (10, 20)
    }
}
