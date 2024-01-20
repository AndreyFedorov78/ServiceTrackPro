from django.urls import path, re_path, include
from django.contrib import admin
from . import views




urlpatterns =[
    path('regions/', views.RegionsView.as_view(),name="regions"),
    path('customers/', views.CustomersView.as_view(), name='customers'),
    path('customer/<int:id>', views.CustomerView.as_view(), name='customer'),
    path('facility/<int:id>', views.FacilityView.as_view(), name='customer'),


    path('test', views.TestView.as_view(), name='test'),


]
