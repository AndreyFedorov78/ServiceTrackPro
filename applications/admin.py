from django.contrib import admin
from .models import Customer, Object, Performer, Request

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'representative')

@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'customer', 'responsible')

@admin.register(Performer)
class PerformerAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    list_display = ('customer', 'customer_request_number', 'responsible_customer', 'object', 'request_text', 'department', 'request_date', 'status', 'completion_date', 'performer', 'simple_closure', 'invoice_number', 'payment_date', 'created_by')
