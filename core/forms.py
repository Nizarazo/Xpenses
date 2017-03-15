from django import forms

from . import models


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        exclude = (
            'user',
        )


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = (
            'user',
            'expense',
        )
