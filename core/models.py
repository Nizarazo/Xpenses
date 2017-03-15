from django.db import models
from django.urls import reverse


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2,
                                 max_digits=10)
    title = models.CharField(max_length=300)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return "[#{}] {} {:,}@{}".format(
            self.id,
            self.title,
            self.amount,
            self.date,
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id, ))