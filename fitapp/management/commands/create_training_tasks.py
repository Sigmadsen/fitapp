from fitapp.models import User
from django.core.management.base import BaseCommand

from fitapp.models import TrainingTask


class CreateDailyTask(BaseCommand):
    help = "Create 3 training tasks with management command"

    def add_arguments(self, parser):
        parser.add_argument("user_id", type=int)

    def handle(self, *args, **kwargs):
        user_id = kwargs["user_id"]
        try:
            user = User.objects.get(id=user_id)
            TrainingTask.objects.create(user=user, description="100 push-ups")
            TrainingTask.objects.create(user=user, description="100 squats")
            TrainingTask.objects.create(user=user, description="100 push-ups")
            self.stdout.write(self.style.SUCCESS("Successfully created the tasks."))
        except User.DoesNotExist:
            self.stdout.write(self.style.ERROR("User does not exist."))
