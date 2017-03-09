from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.expense_list),
    url(r'^month/([0-9]{4})/$', views.expense_list),
    url(r'^month/all/(?P<month>[0-9]{1,2})/$', views.expense_list, kwargs={'year':None}),
    url(r'^month/([0-9]{4})/([0-9]{1,2})/$', views.expense_list),

    url(r'^([0-9]+)/$', views.expense_detail),

]
