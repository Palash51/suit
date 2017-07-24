from django.conf.urls import url
from django.contrib import admin
from suit import views

urlpatterns = [
	url(r'^$', views.home,name='homepage'),
	]