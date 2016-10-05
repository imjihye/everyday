from django.conf.urls import url
from . import views

app_name = 'sense'
urlpatterns = [
	url(r'^$', views.index),
]