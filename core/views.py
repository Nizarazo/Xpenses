import random

from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Q, Sum
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic import DeleteView
from django.views.generic import DetailView
from django.views.generic import ListView
from django.views.generic import TemplateView
from django.views.generic import UpdateView

from . import forms
from . import models


# def view(request):
#     return response
#
#
# class View:
#     @classmethod
#     def as_view(cls, self):
#         def view(request, *args, **kwargs):
#             print("!!!!!!!!!!!!")
#             o = cls()
#             return o.dispatch(request, *args, **kwargs)
#
#         return view
#
#     def __init__(self):
#         pass
#
#     def dispatch(self, request, *args, **kwargs):
#         self.request = request
#         self.args = args
#         self.kwargs = kwargs
#         f = getattr(self, request.method.lower())
#         return f(request, *args, **kwargs)

# class MyView(View):
#     def get(self, request, *args, **kwargs):
#         assert False, "KUKU"

# class ExpenseListView(LoginRequiredMixin, TemplateView):
#     template_name = "core/expense_list.html"
#
#     def get_context_data(self, **kwargs):
#         year = self.kwargs.get('year')
#         month = self.kwargs.get('month')
#         d = super().get_context_data(**kwargs)
#         qs = models.Expense.objects.filter(
#             user=self.request.user,
#         ).order_by('-date', '-id')
#
#         if year:
#             qs = qs.filter(date__year=year)
#         if month:
#             qs = qs.filter(date__month=month)
#
#         q = self.request.GET.get('q')
#
#         if q:
#             qs = qs.filter(Q(title__contains=q) | Q(description__contains=q))
#
#         total = sum(o.amount for o in qs)  # TODO: use aggregate instead
#
#         d.update({
#             'object_list': qs,
#             'total': total,
#             'year': year,
#             'month': month,
#             'q': q,
#         })
#         return d
class MyView(TemplateView):
    template_name = "core/my_template.html"

    udi = random.randint(1, 10)

    def something(self):
        return random.randint(1, 10)

    # def get_context_data(self, **kwargs):
    #     d =  super().get_context_data(**kwargs)
    #     d['david'] = 182736218763
    #     return d

    def get_context_data(self, **kwargs):
        return super().get_context_data(
            david=random.randint(1, 10),
            **kwargs
        )


class ExpenseMixin(LoginRequiredMixin):
    model = models.Expense
    form_class = forms.ExpenseForm

    def get_queryset(self):
        return super().get_queryset().filter(
            user=self.request.user,
        )

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['categories'].queryset = self.request.user.categories.all()
        return form


# class SpecialExpenseListView(ExpenseListView):
#     template_name = "core/expense_special.html"

class ExpenseListView(ExpenseMixin, ListView):
    paginate_by = 20

    def get_queryset(self):
        self.year = self.kwargs.get('year')
        self.month = self.kwargs.get('month')
        self.q = self.request.GET.get('q')

        qs = super().get_queryset().order_by('-date', '-id')

        if self.year:
            qs = qs.filter(date__year=self.year)

        if self.month:
            qs = qs.filter(date__month=self.month)

        if self.q:
            qs = qs.filter(
                Q(title__contains=self.q) | Q(description__contains=self.q))

        return qs

    def get_context_data(self, **kwargs):

        d = super().get_context_data(**kwargs)

        self.total = self.get_queryset().aggregate(
            x=Sum('amount')
        ).get('x')

        d.update({
            'total': self.total,
            'year': self.year,
            'month': self.month,
            'q': self.q,
        })
        return d


class ExpenseDetailView(ExpenseMixin, DetailView):
    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.form = forms.CommentForm(request.POST)
        if self.form.is_valid():
            self.form.instance.expense = self.object
            self.form.instance.user = request.user
            self.form.save()
            messages.success(request, "Comment created.")
            return redirect(self.object)

    def get(self, request, *args, **kwargs):
        self.form = forms.CommentForm()
        return super().get(request, *args, **kwargs)


class ExpenseCreateView(ExpenseMixin, CreateView):
    def form_valid(self, form):
        form.instance.user = self.request.user
        resp = super().form_valid(form)
        messages.success(self.request, "Expense created.")
        return resp


class ExpenseUpdateView(ExpenseMixin, UpdateView):
    class ExpenseCreateView(ExpenseMixin, CreateView):
        def form_valid(self, form):
            resp = super().form_valid(form)
            messages.success(self.request, "Expense updated.")
            return resp


class ExpenseDeleteView(ExpenseMixin, DeleteView):
    success_url = reverse_lazy("expenses:list")
