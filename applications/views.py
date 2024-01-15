from django.contrib.auth import logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import redirect, render
from django.views.generic import View


class CustomLoginView(LoginView):
    template_name = 'applications/login.html'


class CustomLogoutView(View):
    @staticmethod
    def get(request):
        logout(request)
        return redirect('/')


class IndexView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "applications/index.html")


class RegionsView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "applications/regions.html")


class CustomersView(LoginRequiredMixin, View):
    @staticmethod
    def get(request):
        return render(request, "applications/customers.html")


class CustomerView(LoginRequiredMixin, View):
    @staticmethod
    def get(request,id):
        return render(request, "applications/customer.html", {'id':id})
