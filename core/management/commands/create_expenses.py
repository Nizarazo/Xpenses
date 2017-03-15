import datetime
import random

import silly
from django.core.management.base import BaseCommand

from core.models import Expense


class Command(BaseCommand):
    help = "Creates dummy expenses"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)

    def handle(self, *args, **options):
        for i in range(options['n']):
            o = Expense(
                date=datetime.date(
                    random.randint(2010, 2017),
                    random.randint(1, 12),
                    random.randint(1, 28)
                ),
                title=silly.a_thing(),
                amount=random.randint(1, 1000),
                description=silly.paragraph(),
            )
            o.full_clean()
            o.save()
