from celery import shared_task
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)


@shared_task
def my_daily_training():
    from fitapp.models import User

    users = User.objects.all()
    for user in users:
        my_daily_training_for_user.delay(user.id)


@shared_task
def my_daily_training_for_user(user_id):
    from fitapp.models import TrainingTask, User

    user = User.objects.get(id=user_id)
    for training_task in TrainingTask.objects.filter(repeat=True, user=user):
        TrainingTask.objects.create(user=user, description=training_task.description)
