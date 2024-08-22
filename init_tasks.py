from datetime import datetime, timedelta
from tasks import run_script


def schedule_tasks():
    # Task after 1 min
    eta_time = datetime.now() + timedelta(minutes=1)
    run_script.apply_async(eta=eta_time)


if __name__ == "__main__":
    for i in range(5):
        schedule_tasks()
