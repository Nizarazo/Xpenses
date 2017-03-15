from django import forms

from . import models


class ExpenseForm(forms.ModelForm):
    class Meta:
        model = models.Expense
        fields = "__all__"


class CommentForm(forms.ModelForm):
    class Meta:
        model = models.Comment
        exclude = (
            'expense',
        )
