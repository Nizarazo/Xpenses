from django.test import TestCase

from . import models


class CoreTests(TestCase):
    def test_simple_expense(self):
        n = models.Expense.objects.count()

        o = models.Expense(
            date="2016-02-25",
            title="pizza",
            amount="19.90",
        )
        o.full_clean()
        o.save()

        self.assertEqual(models.Expense.objects.count(), n + 1)
