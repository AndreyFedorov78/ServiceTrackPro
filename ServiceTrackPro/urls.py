from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from applications import urls_api
from applications import urls
from applications import views
from django.contrib.auth.views import LogoutView



urlpatterns = [
    path('logout/', views.CustomLogoutView.as_view(), name='logout'),
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('accounts/login/', views.CustomLoginView.as_view(), name='login'),
    path('admin/', admin.site.urls),
    path('api/', include(urls_api.urlpatterns_api)),
    path(r'', views.IndexView.as_view(),name="index"),
    path(r'',include(urls.urlpatterns)),


]
