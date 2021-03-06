"""diary URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from . import views

app_name = 'diary'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^list/$',
        views.DiaryListView.as_view(), name='list'),
    url(r'^new/$',
        views.DiaryCreateView.as_view(), name='new'),
    url(r'^diaries/(?P<pk>[0-9]+)/update/$',
        views.DiaryUpdateView.as_view(), name='update'),
    url(r'^diaries/(?P<pk>[0-9]+)/delete/$',
        views.DiaryDeleteView.as_view(), name='delete'),
    url(r'^diaries/(?P<pk>[0-9]+)/$',
        views.DiaryDetailView.as_view(), name='detail'),
]
