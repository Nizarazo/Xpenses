from django.contrib import admin

from . import models


class ExpenseAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'date',
        'amount',
        'title',
    )
    search_fields = (
        'id',
        'date',
        'amount',
        'title',
    )
    date_hierarchy = "date"


admin.site.register(models.Expense, ExpenseAdmin)
