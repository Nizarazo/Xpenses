from django.db.models import Sum
from django.http.response import JsonResponse
from rest_framework import viewsets
from rest_framework.decorators import list_route, detail_route

from . import models
from . import serializers


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = models.Expense.objects.all()
    serializer_class = serializers.ExpenseSerializer

    @list_route()
    def total(self, request, *args, **kwargs):
        value = self.queryset.aggregate(x=Sum('amount')).get('x', 0)
        return JsonResponse({'value': value})

    @detail_route()
    def comments(self, request, *args, **kwargs):
        instance = self.get_object()
        value = instance.comments.count()
        return JsonResponse({'value': value})


class CommentViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.Comment.objects.all()
    serializer_class = serializers.CommentSerializer
