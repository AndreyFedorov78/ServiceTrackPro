from django.contrib import admin
from .models import Customer, Object,  Request, Facility, FacilityIMG, Files

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'details', 'representative')

@admin.register(Facility)
class FacilityAdmin(admin.ModelAdmin):
    pass

"""
@admin.register(Object)
class ObjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'customer', 'responsible')
"""
@admin.register(Request)
class RequestAdmin(admin.ModelAdmin):
    pass
   # list_display = ('customer', 'customer_request_number', 'responsible_customer', 'object', 'request_text', 'department', 'request_date', 'status', 'completion_date',  'simple_closure', 'invoice_number', 'payment_date', 'created_by')

@admin.register(FacilityIMG)
class FacilityIMGAdmin(admin.ModelAdmin):
    pass
   # list_display = ('customer', 'customer_request_number', 'responsible_customer', 'object', 'request_text', 'department', 'request_date', 'status', 'completion_date',  'simple_closure', 'invoice_number', 'payment_date', 'created_by')

@admin.register(Files)
class FilesAdmin(admin.ModelAdmin):
    pass
   # list_display = ('customer', 'customer_request_number', 'responsible_customer', 'object', 'request_text', 'department', 'request_date', 'status', 'completion_date',  'simple_closure', 'invoice_number', 'payment_date', 'created_by')
