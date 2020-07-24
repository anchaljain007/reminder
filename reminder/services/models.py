from django.db import models

# Create your models here.
class ActiveServicesModel(models.Model):
    username=models.CharField(max_length=100)
    income_tax_activate = models.BooleanField(null=False, blank=False)
    gst_tax_activate = models.BooleanField(null=False, blank=False)
    companies_activate = models.BooleanField(null=False, blank=False)
    accounting_activate = models.BooleanField(null=False, blank=False)

class IncomeTaxModel(models.Model):
    username=models.CharField(max_length=100)
    first_install_due=models.DateField()
    second_install_due=models.DateField()
    third_install_due=models.DateField()
    fourth_install_due=models.DateField()
    tax_return_date=models.DateField()
    tds_return_date=models.DateField()
    audit_date=models.DateField()

class GstModel(models.Model) :
    username=models.CharField(max_length=100)
    duration=models.CharField(max_length=100)
    first_due_1=models.DateField()
    first_due_3b=models.DateField()
    annual_return=models.DateField()
    audit_date=models.DateField()


class CompaniesActModel(models.Model):
    username=models.CharField(max_length=100)
    first_return_due=models.DateField()
    second_return_due=models.DateField()

class AccountingModel(models.Model):
    username=models.CharField(max_length=100)
    first_return_due=models.DateField()
    second_return_due=models.DateField()