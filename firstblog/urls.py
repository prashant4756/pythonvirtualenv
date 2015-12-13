from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^new/$', views.new_add,name='new_add'),
    url(r'(?P<pk>[0-9]+)/$', views.librarydetails, name='librarydetails'),
]