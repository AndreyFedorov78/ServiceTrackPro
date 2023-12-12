from django.contrib import admin
from django.urls import path, re_path, include
from django.views.generic import TemplateView
from applications import urls_api


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls_api.urlpatterns_api)),
    path(r'', TemplateView.as_view(template_name='index.html')),
    re_path(r'^(?!admin|static|api).*/$', TemplateView.as_view(template_name='index.html')),
]
