from django.urls import path, re_path, include
from django.contrib import admin
from .views_api import UserAPI

urlpatterns_api =[
    path('user', UserAPI.as_view()),
]