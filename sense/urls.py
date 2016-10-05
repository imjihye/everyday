from django.conf.urls import url
from . import views

app_name = 'sense'
urlpatterns = [
	url(r'^$', views.index),
	url(r'^list/$', views.ListView.as_view(), name='list'),
	url(r'^create/$', views.CreateView.as_view(), name='create'),
]
