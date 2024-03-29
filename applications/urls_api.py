from django.urls import path, re_path, include
from django.contrib import admin
from . import views_api




urlpatterns_api =[
    path('user', views_api.UserAPI.as_view()),
    path('users/', views_api.UserListAPI.as_view()),
    path('customers/', views_api.CustomerListAPIView.as_view(), name='customer-list'),
    path('customer/<int:id>', views_api.CustomerAPIView.as_view(), name='customer-api'),
    path('objects/', views_api.ObjectListAPIView.as_view(), name='object-list'),
    path('object/<int:id>', views_api.ObjectAPIView.as_view(), name='object'),
    path('file/<int:id>', views_api.UploadFacilityFileAPIView.as_view()),
    path('facility_img_upload/<int:id>', views_api.UploadFacilityIMGAPIView.as_view()),
    path('requests/', views_api.RequestListAPIView.as_view(), name='request-list'),
    path('request/<int:id>', views_api.RequestAPIView.as_view(), name='reques'),
    path('region/', views_api.RegionAPIView.as_view(), name='region_api'),
    path('facility/', views_api.FacilityAPIView.as_view(), name='facility_api'),
    path('facility/<int:id>', views_api.FacilityEditAPIView.as_view()),
    path('get_file/<int:id>', views_api.FileDownloadView.as_view()),

]
