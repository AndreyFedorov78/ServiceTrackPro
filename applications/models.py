
from django.db import models
from django.contrib.auth.models import User

class Customer(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    representative = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name

class Object(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    responsible = models.ForeignKey(User, null=True, blank=True,  default=None, on_delete=models.SET(None))

    def __str__(self):
        return self.name



class Request(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    customer_request_number = models.CharField(max_length=255)
    object = models.ForeignKey(Object, on_delete=models.CASCADE)
    request_text = models.TextField()
    #department = models.CharField(max_length=255)
    request_date = models.DateField()
    status = models.BooleanField(default=False)
    completion_date = models.DateField(null=True, blank=True)
    #act = models.TextField(null=True, blank=True)
    responsible = models.ForeignKey(User,related_name='responsible', null=True, blank=True,  default=None, on_delete=models.SET(None))
    notes = models.TextField(null=True, blank=True)
    estimate_number = models.CharField(max_length=255)
    budget_line_code = models.CharField(max_length=255)
    agreed_budget_number = models.CharField(max_length=255)
    budget_type = models.CharField(max_length=255)
    budget_name = models.CharField(max_length=255)
    period = models.CharField(max_length=255)
    amount_with_vat = models.DecimalField(max_digits=10, decimal_places=2)
    simple_closure = models.BooleanField(default=False)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET(None))

    def __str__(self):
        return f"Request {self.id}"

# Другие модели и связи между ними
