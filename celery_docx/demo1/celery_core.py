# !/usr/bin/env python
# -*-coding:utf-8 -*-
# PROJECT    : project-structure-collections
# Time       ：2020/12/8 15:16
# Warning    ：The Hard Way Is Easier
from celery import Celery

"""
TIP:
- 当前文件夹必须命名为celery，才能启动成功。
- include = ["moduleName.pyName"]


启动命令：
在 celery_docx 目录下：
celery -A demo1 worker -c 2 -l INFO
celery -A demo1.celery_core:app worker -c 2 -l INFO
"""

app = Celery("module_name",
             broker='redis://localhost:6379/0',
             backend='redis://localhost:6379/0',
             include=['demo1.tasks']
             )


@app.task
def mainExample(x, y):
    print(x + y)
    return x + y


print(type(mainExample))
print(mainExample.__evaluated__())
print(mainExample.name)
print(mainExample.__evaluated__())

# if __name__ == '__main__':
#     app.worker_main()
