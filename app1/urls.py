from django.urls import path
from django.urls.conf import include
from . import views

app_name='app1'

urlpatterns = [
    path('', views.home, name='home'),
    path('home', views.home2, name='home2'),


]