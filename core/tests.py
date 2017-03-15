from django.test import TestCase
from django.urls import reverse

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

    # def test_shuff(self):
    #     word = "shalom"
    #     url = reverse('shuffle', args=(word,))
    #     resp = self.client.get(url)
    #     self.assertEqual(resp.status_code, 200)
    #     data = resp.json()
    #     self.assertIn('value', data)
    #     self.assertEqual(sorted(word), sorted(data['value']))
