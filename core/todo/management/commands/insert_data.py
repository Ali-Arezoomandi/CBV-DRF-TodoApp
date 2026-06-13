from django.core.management.base import BaseCommand
from faker import Faker
import random
from datetime import datetime

from accounts.models import User
from todo.models import Task


class Command(BaseCommand):
    help = "inserting dummy data"
    
    def __init__(self, *args, **kwargs):
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **options):
        user = User.objects.create(
            username=self.fake.name(),
            password='test@123123'
        )
        
        for _ in range(5):
            Task.objects.create(
                user=user,
                title=self.fake.paragraph(nb_sentences=1),
                completed=random.choice([True, False]),
            )
    