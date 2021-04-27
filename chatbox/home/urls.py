from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.signin,name="homemain" ),
]
