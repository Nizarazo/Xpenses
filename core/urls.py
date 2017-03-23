from django.conf.urls import url

from . import views

app_name = "expenses"

urlpatterns = [
    # url(r'^$', views.MyView.as_view(), name="list"),
    url(r'^$', views.ExpenseListView.as_view(), name="list"),
    url(r'^create/$', views.ExpenseCreateView.as_view(), name="create"),

    url(r'^month/([0-9]{4})/$', views.ExpenseListView.as_view()),
    url(r'^month/all/(?P<month>[0-9]{1,2})/$', views.ExpenseListView.as_view(),
        kwargs={'year': None}),
    url(r'^month/([0-9]{4})/([0-9]{1,2})/$', views.ExpenseListView.as_view()),

    url(r'^(?P<pk>[0-9]+)/$', views.ExpenseDetailView.as_view(),
        name="detail"),
    url(r'^(?P<pk>[0-9]+)/edit/$', views.ExpenseUpdateView.as_view(),
        name="update"),
    url(r'^(?P<pk>[0-9]+)/delete/$', views.ExpenseDeleteView.as_view(),
        name="delete"),
]
