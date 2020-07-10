from django.shortcuts import render
from .models import IncomeTaxModel
from .forms import IncomeTaxForm

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def service_view(request):
    return render(request, 'service.html')

def incometax_view(request):
    context ={} 
    form = IncomeTaxForm() 
    context['form']= form 
    if request.POST: 
        temp = request.POST['first_install_due'] 
        print(temp) 
        form.save()
    print(request)
    print(request.POST)
    context={}
    form = IncomeTaxForm(request.POST or None )
    if form.is_valid() :
        form.save()
    context['form'] = form
    return render(request, 'incometax.html', context )

def gst_view(request):
    return render(request, 'gst.html')

def companies_act_view(request):
    return render(request, 'companies_act.html')

def accounting_view(request):
    return render(request, 'accounting.html')

