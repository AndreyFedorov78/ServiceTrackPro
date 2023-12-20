from django.urls import path, re_path, include
from django.contrib import admin
from . import views_api

urlpatterns_api =[
    path('user', views_api.UserAPI.as_view()),
    path('customers/', views_api.CustomerListAPIView.as_view(), name='customer-list'),
    path('customer/<int:id>', views_api.CustomerAPIView.as_view(), name='customer'),
    path('objects/', views_api.ObjectListAPIView.as_view(), name='object-list'),
    path('performers/', views_api.PerformerListAPIView.as_view(), name='performer-list'),
    path('requests/', views_api.RequestListAPIView.as_view(), name='request-list'),

]
