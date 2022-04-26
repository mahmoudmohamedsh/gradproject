from django.urls import path 

from .views import CreateUser

#/user/
urlpatterns =[
    path('create/',CreateUser.as_view())
]