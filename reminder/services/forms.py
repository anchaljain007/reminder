from django import forms
from .models import *

# class 
class ActivateServices(forms.Form):
    class Meta:
        model= ActiveServicesModel
        fields=['username','income_tax_activate','gst_tax_activate',
        'companies_activate','accounting_activate',]

class IncomeTaxForm(forms.Form):
    class Meta:
        model = IncomeTaxModel
        fields = ['username','first_install_due', 'second_install_due',
                    'third_install_due', 'fourth_install_due',
                    'tax_return_date', 'tds_return_date', 'audit_date' , ]
        
    
class GstForm(forms.Form):
    class Meta:
        model = GstModel
        fields = ['username','duration','first_due_1' ,
                   'first_due_3b' , 'annual_return','audit_date',]
        
class CompaniesActForm(forms.Form):
    class Meta:
        model = CompaniesActModel
        fields = ['username','first_install_due', 'second_install_due', ]
        
class AccountingForm(forms.Form):
    class Meta:
        model = AccountingModel
        fields = ['username','first_install_due', 'second_install_due', ]