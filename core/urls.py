from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.expense_list),
    url(r'^([0-9]+)/$', views.expense_detail),
]
