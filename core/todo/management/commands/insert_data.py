from django.core.management.base import BaseCommand
from faker import Faker
import random

from accounts.models import User
from todo.models import Task


class Command(BaseCommand):
    help = "inserting dummy data"

    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create_user(
            username=self.fake.user_name(), password="test@123123"
        )

        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.word(),
                completed=random.choice([True, False]),
            )
