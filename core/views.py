from django.contrib import messages
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from . import forms


def expense_list(request, year=None, month=None):

    qs = models.Expense.objects.order_by('-date', '-id')

    if year:
        qs = qs.filter(date__year=year)
    if month:
        qs = qs.filter(date__month=month)

    q = request.GET.get('q')

    if q:
        qs = qs.filter(Q(title__contains=q) | Q(comments__contains=q))

    total = sum(o.amount for o in qs)  # TODO: use aggregate instead

    return render(request, "core/expense_list.html", {
        'object_list': qs,
        'total': total,
        'year': year,
        'month': month,
        'q': q,
    })


def expense_detail(request, pk):
    o = get_object_or_404(models.Expense, pk=pk)
    return render(request, "core/expense_detail.html", {
        'object': o,
    })


def expense_create(request):
    if request.method == "POST":
        form = forms.ExpenseForm(request.POST)
        if form.is_valid():
            o = form.save()
            messages.success(request, "Expense created.")
            return redirect(o)
    else:
        form = forms.ExpenseForm()

    return render(request, 'core/expense_form.html', {
        'form': form,
    })
