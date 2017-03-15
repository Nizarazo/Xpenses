from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from . import models


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
    # try:
    #     o = models.Expense.objects.get(pk=pk)
    # except models.Expense.DoesNotExist:
    #     raise Http404()

    # return HttpResponse("The title is: {}".format(o.title))

    return render(request, "core/expense_detail.html", {
        'object': o,
    })
