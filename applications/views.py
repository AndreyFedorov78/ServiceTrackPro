from django.contrib.auth import logout
from django.shortcuts import redirect, render
from django.views.generic import View
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin

class CustomLoginView(LoginView):
    template_name = 'applications/login.html'

class CustomLogoutView(View):
    def get(self, request):
        logout(request)
        return redirect('/')

class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,"applications/index.html")

class RegionsView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request,"applications/regions.html")