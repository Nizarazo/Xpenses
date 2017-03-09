from django.db import models


class Expense(models.Model):
    date = models.DateField()
    amount = models.DecimalField(decimal_places=2,
                                 max_digits=10)
    title = models.CharField(max_length=300)
    comments = models.TextField(null=True, blank=True)

