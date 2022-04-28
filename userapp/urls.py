from django.urls import path 

from .views import CreateUser

#/user/
urlpatterns =[
    path('register/',CreateUser.as_view())
]