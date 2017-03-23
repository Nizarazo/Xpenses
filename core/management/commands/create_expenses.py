import datetime
import random

import silly
from django.contrib.auth.models import User
from django.core.management.base import BaseCommand
from django.db import IntegrityError, transaction
from django.utils.text import slugify

from core.models import Expense


def paragraph(length=6):
    return "\n".join([silly.sentence().title() for x in range(0, length)])


class Command(BaseCommand):
    help = "Creates dummy expenses"

    def add_arguments(self, parser):
        parser.add_argument('n', type=int)
        parser.add_argument('--delete', default=False, action='store_true')

    def handle(self, *args, **options):
        if options['delete']:
            Expense.objects.all().delete()

        for i in range(10):
            try:
                User.objects.create_user("user{}".format(i),
                                         password="abcd1234")
            except IntegrityError:
                pass

        users = list(User.objects.all())

        for u in users:
            while u.categories.count() < 4:
                s = silly.a_thing().title()  # "Beautiful cat"
                u.categories.create(
                    title=s,
                    slug=slugify(s),
                )

        for i in range(options['n']):
            with transaction.atomic():
                o = Expense(
                    user=random.choice(users),
                    date=datetime.date(
                        random.randint(2010, 2017),
                        random.randint(1, 12),
                        random.randint(1, 28)
                    ),
                    title=silly.a_thing(),
                    amount=random.randint(1, 1000),
                    description=paragraph(random.randint(2, 4)),
                )
                o.full_clean()
                o.save()

                cats = random.sample(list(o.user.categories.all()),
                                       random.randint(0, 2))

                o.categories = cats

                # for c in cats:
                #     o.categories.create(category=c)

                for j in range(random.randint(3, 10)):
                    o.comments.create(
                        user=random.choice(users),
                        content=paragraph(random.randint(1, 6)),
                    )
