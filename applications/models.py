
from django.db import models
from django.contrib.auth.models import User


class Region(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Наименование', max_length=255)
    active = models.BooleanField('Активный', default=True)

    class Meta:
        verbose_name='Регион'
        verbose_name_plural = 'Регионы'
        ordering = ["title",]

class Region_name(models.Model):
    reg_id = models.ForeignKey(Region,on_delete=models.PROTECT)
    title = models.CharField('Наименование',max_length=255)
    class Meta:
        verbose_name = 'Наименование региона'
        verbose_name_plural = 'Наименования регионов'





class Customer(models.Model):
    name = models.CharField(max_length=255)
    details = models.TextField(blank=True)
    representative = models.CharField(max_length=255, blank=True)
    active = models.BooleanField('Активный', default=True)

    def __str__(self):
        return self.name

class Object(models.Model):
    name = models.CharField(max_length=255)
    address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    responsible = models.ForeignKey(User, null=True, blank=True,  default=None, on_delete=models.SET(None))

    def __str__(self):
        return self.name

class Facility(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Наименование',max_length=255)
    address = models.TextField()
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    #responsible = models.ForeignKey(User, null=True, blank=True,  default=None, on_delete=models.SET(None))
    active = models.BooleanField('Активный', default=True)

    class Meta:
        verbose_name='Объект'
        verbose_name_plural = 'Объекты'
        ordering = ["customer__name","title",]

    def __str__(self):
        return f'{self.title} / {self.customer.name}'



class Request(models.Model):
    #customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True, blank=True)
    customer_request_number = models.CharField(max_length=255, null=True, blank=True)
    object = models.ForeignKey(Object, on_delete=models.CASCADE, null=True, blank=True)
    request_text = models.TextField(null=True, blank=True)
    #department = models.CharField(max_length=255)
    request_date = models.DateField(null=True, blank=True)
    status = models.BooleanField(default=False, null=True, blank=True)
    completion_date = models.DateField(null=True, blank=True)
    #act = models.TextField(null=True, blank=True)
    responsible = models.ForeignKey(User,related_name='responsible', null=True, blank=True,  default=None, on_delete=models.SET(None))
    notes = models.TextField(null=True, blank=True)
    estimate_number = models.CharField(max_length=255, null=True, blank=True)
    budget_line_code = models.CharField(max_length=255, null=True, blank=True)
    agreed_budget_number = models.CharField(max_length=255, null=True, blank=True)
    budget_type = models.CharField(max_length=255, null=True, blank=True)
    budget_name = models.CharField(max_length=255, null=True, blank=True)
    period = models.CharField(max_length=255, null=True, blank=True)
    amount_with_vat = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    simple_closure = models.BooleanField(default=False, null=True, blank=True)
    invoice_number = models.CharField(max_length=255, null=True, blank=True)
    payment_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET(None), null=True, blank=True)

    def __str__(self):
        return f"Request {self.id}"

    class Meta:
      ordering = [
        models.Case(
            models.When(completion_date__isnull=False, then=models.Value(1)),
            default=models.Value(0),
            output_field=models.IntegerField(),
        ),
        '-completion_date',
        '-request_date',
    ]


