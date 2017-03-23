from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    url(r'^$', views.expense_list, name="list"),
    url(r'^create/$', views.expense_create, name="create"),

    url(r'^month/([0-9]{4})/$', views.expense_list),
    url(r'^month/all/(?P<month>[0-9]{1,2})/$', views.expense_list,
        kwargs={'year': None}),
    url(r'^month/([0-9]{4})/([0-9]{1,2})/$', views.expense_list),

    url(r'^([0-9]+)/$', views.expense_detail,
        name="detail"),
    url(r'^([0-9]+)/edit/$', views.expense_update,
        name="update"),
]
