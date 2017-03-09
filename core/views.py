from django.shortcuts import render, get_object_or_404

from . import models


def expense_list(request):
    qs = models.Expense.objects.all()

    return render(request, "core/expense_list.html", {
        'object_list': qs,
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
