from django.db import models

# Create your models here.
class IncomeTaxModel(models.Model):
    first_install_due=models.DateField()
    second_install_due=models.DateField()
    third_install_due=models.DateField()
    fourth_install_due=models.DateField()
    tax_return_date=models.DateField()
    tds_return_date=models.DateField()

    