



### demo2
实现定义任务

```shell script
#在项目根目录 celery_docx 目录下：

# 先发布定时任务
celery -A demo2 beat


# 启动命令

celery -A demo2 worker -c 2 -l INFO
celery -A demo2.celery:app worker -c 2 -l INFO
```

