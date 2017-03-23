from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render, get_object_or_404, redirect

from . import models
from . import forms


@login_required
def expense_list(request, year=None, month=None):
    qs = models.Expense.objects.filter(
        user=request.user,
    ).order_by('-date', '-id')

    if year:
        qs = qs.filter(date__year=year)
    if month:
        qs = qs.filter(date__month=month)

    q = request.GET.get('q')

    if q:
        qs = qs.filter(Q(title__contains=q) | Q(description__contains=q))

    total = sum(o.amount for o in qs)  # TODO: use aggregate instead

    return render(request, "core/expense_list.html", {
        'object_list': qs,
        'total': total,
        'year': year,
        'month': month,
        'q': q,
    })


@login_required
def expense_detail(request, pk):
    o = get_object_or_404(models.Expense, pk=pk, user=request.user)

    if request.method == "POST":
        form = forms.CommentForm(request.POST)
        if form.is_valid():
            form.instance.expense = o
            form.instance.user = request.user
            form.save()
            messages.success(request, "Comment created.")
            return redirect(o)
    else:
        form = forms.CommentForm()

    return render(request, "core/expense_detail.html", {
        'object': o,
        'form': form,
    })


def get_expense_form(user, *args, **kwargs):
    form = forms.ExpenseForm(*args, **kwargs)
    form.fields['categories'].queryset = user.categories.all()
    return form


@login_required
def expense_create(request):
    if request.method == "POST":
        form = get_expense_form(request.user, request.POST)
        if form.is_valid():
            form.instance.user = request.user
            o = form.save()
            messages.success(request, "Expense created.")
            return redirect(o)
    else:
        form = get_expense_form(request.user)

    return render(request, 'core/expense_form.html', {
        'form': form,
    })


@login_required
def expense_update(request, pk):
    o = get_object_or_404(models.Expense, pk=pk, user=request.user)

    if request.method == "POST":
        form = get_expense_form(request.user, request.POST, instance=o)
        if form.is_valid():
            o = form.save()
            messages.success(request, "Expense updated.")
            return redirect(o)
    else:
        form = get_expense_form(request.user, instance=o)

    return render(request, 'core/expense_form.html', {
        'form': form,
    })
