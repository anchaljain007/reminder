from django.shortcuts import render,redirect
from services.models import *
from services.forms import *
from django.contrib.auth import authenticate,login
import psycopg2
from background_task import background
import datetime as dt
from reminder.settings import EMAIL_HOST_USER
from django.core.mail import send_mail

current_date = '2020-07-10'
conn = psycopg2.connect(database="Reminder", user = "postgres", password = "root", host = "localhost", port = "5432")
cur = conn.cursor()

# Create your views here.
def email_adress_adder_from_username(username):
    query_for_getting_username = "SELECT email FROM public.auth_user WHERE username ='"+ str(username)+"'"
    cur.execute(query_for_getting_username)
    rows=cur.fetchall()
    return str(rows[0][0])

@background()
def send_mailssss():
    all_email_address=[]
    # complete_string= str(dt.datetime.today())
    # date_string= complete_string[:10]
    # current_date = date_string
    # print("Mails has to be sent")


    #################################################################################################################################################################
    #income tax model has 7 dates
    query_first_due_date= "SELECT username FROM public.services_incometaxmodel WHERE first_install_due = '"+ str(current_date)+"'"
    query_second_due_date= "SELECT username FROM public.services_incometaxmodel WHERE second_install_due = '"+ str(current_date)+"'"
    query_third_due_date= "SELECT username FROM public.services_incometaxmodel WHERE third_install_due = '"+ str(current_date)+"'"
    query_fourth_due_date= "SELECT username FROM public.services_incometaxmodel WHERE fourth_install_due = '"+ str(current_date)+"'"
    query_tax_return_date= "SELECT username FROM public.services_incometaxmodel WHERE tax_return_date = '"+ str(current_date)+"'"
    query_tds_return_date= "SELECT username FROM public.services_incometaxmodel WHERE tds_return_date = '"+ str(current_date)+"'"
    query_audit_date_it= "SELECT username FROM public.services_incometaxmodel WHERE audit_date = '"+ str(current_date)+"'"
    
    
    
    cur.execute(query_first_due_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_second_due_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_third_due_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_fourth_due_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_tax_return_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_tds_return_date)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_audit_date_it)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    #################################################################################################################################################################
    #gst model has 4 dates
    print("=="*100)
    query_first_due_1 = "SELECT username FROM public.services_gstmodel WHERE first_due_1 = '"+ str(current_date)+"'"
    query_first_due_3b = "SELECT username FROM public.services_gstmodel WHERE first_due_3b = '"+ str(current_date)+"'"
    query_annual_return = "SELECT username FROM public.services_gstmodel WHERE annual_return = '"+ str(current_date)+"'"
    query_audit_date_gst = "SELECT username FROM public.services_gstmodel WHERE audit_date = '"+ str(current_date)+"'"
    

    cur.execute(query_first_due_1)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_first_due_3b)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_annual_return)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    
    cur.execute(query_audit_date_gst)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)

    #################################################################################################################################################################
    #companies act model has 4 dates
    print("=="*100)
    query_first_return_due =  "SELECT username FROM public.services_companiesactmodel WHERE first_return_due = '"+ str(current_date)+"'"
    query_second_return_due =  "SELECT username FROM public.services_companiesactmodel WHERE second_return_due = '"+ str(current_date)+"'"
    

    cur.execute(query_first_return_due)
    rows=cur.fetchall()
    print(rows[0])
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)

    cur.execute(query_second_return_due)
    rows=cur.fetchall()
    print(rows[0][0])
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)

    #################################################################################################################################################################
    #accounting model has 4 dates
    print("=="*100)
    query_first_return_due_acc = "SELECT username FROM public.services_accountingmodel WHERE first_return_due = '"+ str(current_date)+"'"
    query_second_return_due_acc = "SELECT username FROM public.services_accountingmodel WHERE second_return_due = '"+ str(current_date)+"'"

    cur.execute(query_first_return_due_acc)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)

    cur.execute(query_second_return_due_acc)
    rows=cur.fetchall()
    print(rows)
    if(len(rows)!=0):
        temp_email = email_adress_adder_from_username(rows[0][0])
        all_email_address.append(temp_email)
    

    print("****"*50)
    print(all_email_address)

    subject='You have a Request Due'
    message= 'We request you to check with your deadlined of your requests'
    
    for i in range(0,len(all_email_address)):
        reciepent= str(all_email_address[i])
        send_mail(subject,message,EMAIL_HOST_USER,[reciepent],fail_silently=False)


def home_view(request):
    complete_string= str(dt.datetime.today())
    date_string= complete_string[:10]
    if(date_string!=current_date):
        print("WE are scheduling")
        send_mailssss()
    # scheduler.start()
    # scheduler.add_job(send_mails,'interval',seconds=5)
    return render(request, 'home.html')

def profile_view(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username
    print(username)
    query="SELECT * FROM public.services_activeservicesmodel WHERE services_activeservicesmodel.username = '"+ str(username) +"'"
    print(query)
    cur.execute(query)
    rows = cur.fetchall()
    print(rows)
    print(type(rows))
    for row in rows:
        income_tax = row[2]
        gst = row[3]
        companies_act =row[4]
        accounting_act =row[5]
    
    print(income_tax)
    args={'income_tax':income_tax , 'gst':gst , 'companies_act':companies_act, 'accounting_act':accounting_act }
    print(args)
    return render(request, 'profile.html',args)


def service_view(request):
    if request.method == 'GET':
        return render(request, 'service.html')
        
    username=request.POST.get('username')
    income_tax_activate= request.POST.get('check_01')
    companies_activate= request.POST.get('check_02')
    gst_tax_activate= request.POST.get('check_03')
    accounting_activate= request.POST.get('check_04')
    print(accounting_activate,companies_activate,gst_tax_activate,income_tax_activate)
    
    
    class_of_income_tax = str(income_tax_activate)
    class_of_gst_tax=str(gst_tax_activate)
    class_of_companies=str(companies_activate)
    class_of_accounting=str(accounting_activate)
    print("=="*50)
    print("**"*50)
    
    if(class_of_income_tax=='None'):
        income_tax_activate=0
    if(class_of_gst_tax=='None'):
        gst_tax_activate=0
    if(class_of_companies=='None'):
        companies_activate=0
    if(class_of_accounting=='None'):
        accounting_activate=0
        
    activate_info_object= ActiveServicesModel(username=username, income_tax_activate=income_tax_activate,gst_tax_activate=gst_tax_activate,
    companies_activate=companies_activate,accounting_activate=accounting_activate)

    activate_info_object.save()
    return redirect('../profile/')


def incometax_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('first_install'))
    # print('incometax_view')
    username=request.POST.get('username')
    first_install= request.POST.get('first_install')
    second_install= request.POST.get('second_install')
    third_install= request.POST.get('third_install')
    fourth_install= request.POST.get('fourth_install')
    taxreturn= request.POST.get('taxreturn')
    tdsreturn = request.POST.get('tdsreturn')
    audit = request.POST.get('audit')
    if request.method == 'GET':
        return render(request, 'incometax.html')
    
    incom_obj = IncomeTaxModel(username=username, first_install_due=first_install, second_install_due =second_install,
    third_install_due=third_install, fourth_install_due=fourth_install,
    tax_return_date= taxreturn,tds_return_date=tdsreturn, audit_date=audit)

    incom_obj.save()

    # print('Saved')
    return redirect('../../profile/')


def gst_view(request):
    print(request.POST)
    print(request.method)
    # print(request.POST.get('first_install'))
    # print('incometax_view')
    username=request.POST.get('username')
    duration=request.POST.get('duration')
    first_due_GSTR1= request.POST.get('first_due_GSTR1')
    first_due_GSTR3B= request.POST.get('first_due_GSTR3B')
    annual_return= request.POST.get('annual_return')
    audit= request.POST.get('audit')

    # print(type(duration_monthly))
    # if str(type(duration_monthly))=='NoneType':
    #     duration_monthly=False
    # elif str(type(duration_quaterly))=='NoneType':
    #     duration_quaterly=False
    # print(type(duration_quaterly))


    if request.method == 'GET':
        return render(request, 'gst.html')
    

    incom_obj = GstModel(username=username,duration=duration,first_due_1=first_due_GSTR1, 
                first_due_3b=first_due_GSTR3B, annual_return= annual_return,audit_date=audit)

    incom_obj.save()

    print('Saved')
    return redirect('../../profile/')
 

def companies_act_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('Return_1'))
    # print('companies_act_view')

    Return_1= request.POST.get('Return_1')
    Return_2= request.POST.get('Return_2')

    if request.method == 'GET':
        return render(request, 'companies_act.html')
    
    incom_obj = CompaniesActModel(first_return_due=Return_1, second_return_due =Return_2)

    incom_obj.save()

    # print('Saved')
    return redirect('../../profile/')


def accounting_view(request):
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('Return_1'))
    # print('companies_act_view')

    Return_1= request.POST.get('Return_1')
    Return_2= request.POST.get('Return_2')

    if request.method == 'GET':
        return render(request, 'accounting.html')
    
    incom_obj = AccountingModel(first_return_due=Return_1, second_return_due =Return_2)

    incom_obj.save()

    # print('Saved')
    return redirect('../../profile/')


def team_view(request):
    return render(request,'team.html')

def aboutus_view(request):
    return render(request,'aboutus.html')