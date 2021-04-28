from django.contrib import admin
from django.urls import path
from home import views
from .views import *
urlpatterns = [
    path("",views.signin,name="homemain" ),
    path("register/",views.register,name="reg"),
    path("get/",AjaxHandlerView.as_view()),
    path("post",AjaxHandlerView.as_view()),
    # path("post3",AjaxHandlerView.as_view()),
]
