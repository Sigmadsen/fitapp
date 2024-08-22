from celery import Celery

app = Celery(
    "my_tasks",
    broker="redis://redis:6379/0",
    backend="redis://redis:6379",
    include=["tasks"],
)

app.conf.update(
    result_expires=3600,
)
