from django.urls import path
from . import views

app_name="cloneapp"

urlpatterns =[
    path('hello',views.hello),
    path('',views.ind,name='index'),
    path('content',views.data,name='data1'),
    path('rooms',views.table,name='roomtype'),
    path('fblogin',views.login,name='fblog'),
    


]