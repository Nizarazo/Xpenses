from django.conf import settings
from django.db import models
from django.urls import reverse


class Category(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='categories',
                             on_delete=models.CASCADE)
    title = models.CharField(max_length=300)  # "Food!!!"
    slug = models.CharField(
        max_length=300)  # "food" for /expense/category/food/
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title


class Expense(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='expenses',
                             on_delete=models.CASCADE)
    date = models.DateField(db_index=True)
    amount = models.DecimalField(decimal_places=2,
                                 max_digits=10)
    title = models.CharField(max_length=300)
    description = models.TextField(null=True, blank=True)

    categories = models.ManyToManyField(
        Category, related_name='expenses', blank=True,
    )

    def __str__(self):
        return "[#{}] {} {:,}@{}".format(
            self.id,
            self.title,
            self.amount,
            self.date,
        )

    def get_absolute_url(self):
        return reverse("expenses:detail", args=(self.id,))


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             related_name='comments',
                             on_delete=models.CASCADE)
    expense = models.ForeignKey(Expense, related_name='comments',
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    # TODO: add user
    content = models.TextField()

    class Meta:
        ordering = (
            '-created_at',
        )
