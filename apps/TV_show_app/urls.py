from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^$', views.index),
    url(r'^shows/create$',views.add_show),
    url(r'^shows/(?P<show_id>\d+)$',views.show_detail),
    url(r'^shows/new$',views.new),
    url(r'^shows/(?P<show_id>\d+)/edit$',views.edit),
    url(r'^shows/(?P<show_id>\d+)/destroy$',views.delete),
    url(r'^shows/(?P<show_id>\d+)/update',views.update)
]