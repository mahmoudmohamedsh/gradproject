
# from django.contrib import admin

from django.urls import path, include
from .views import HomeList , api_chatbot, api_send_mail

# /home
urlpatterns = [
    path('',HomeList.as_view()),
    path('chat',api_chatbot),
    path('mail',api_send_mail)
]
