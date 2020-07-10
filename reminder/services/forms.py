from django import forms
from .models import IncomeTaxModel

# class 
class IncomeTaxForm(forms.Form):
    class Meta:
        model = IncomeTaxModel
        fields = ['first_install_due', 'second_install_due',
                    'third_install_due', 'fourth_install_due',
                    'tax_return_date', 'tds_return_date', ]
        
    
