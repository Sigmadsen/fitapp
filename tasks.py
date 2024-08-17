from celery_app import app
from datetime import datetime


@app.task
def run_script(eta: datetime = datetime.now()):
    return f"{eta}"
