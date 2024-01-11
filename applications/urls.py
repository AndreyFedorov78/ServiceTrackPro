from django.urls import path, re_path, include
from django.contrib import admin
from . import views




urlpatterns =[
    path(r'regions/', views.RegionsView.as_view(),name="regions"),



]
