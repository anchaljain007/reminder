from django.shortcuts import render,redirect
from authentication.models import *
from authentication.forms import *
from django.http import HttpResponse
import psycopg2
from django.contrib.auth import authenticate,login,logout
from django.core.mail import send_mail
from django.template.loader import render_to_string

# Create your views here.
conn = psycopg2.connect(database="Reminder", user = "postgres", password = "root", host = "localhost", port = "5432")
cur = conn.cursor()

def signup_view(request):
    # print("=======")
    # print(request)
    if request.method=='GET':
        return render(request, 'signup.html')

    firstname= request.POST.get('firstname')
    lastname=request.POST.get('lastname')
    username=request.POST.get('username')
    phone=request.POST.get('phone')
    email=request.POST.get('email')
    gst=request.POST.get('gst')
    aadhar=request.POST.get('aadhar')
    pan=request.POST.get('pan')
    password=request.POST.get('password') 
    repass=request.POST.get('repass')  
    # print(request.POST)
    # print(request.method)
    # print(request.POST.get('firstname'))
    # print('signup_view')
    
    # Create user and save to the database
    u1 = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
    
    sign_obj =Profile(user=u1,phone_no=phone,gst=gst,aadhar=aadhar,pan=pan,repassword=repass)  
    u1.save()
    sign_obj.save()
    print('Saved')
    login(request, u1)
    args={}
    args['username'] = username
    # email sent
    subject = 'Welcome to Reminder System' 
    html_message = render_to_string('activation_sent.html', {'context': 'values'})
    plain_message = 'Reminder System registered'
    from_email = 'remindersystemkj@gmail.com' 
    # to = ['anchal.j@somaiya.edu','ansh.jain@somaiya.edu'] 

    send_mail(subject, plain_message, from_email, [email], html_message=html_message)
    return redirect('../service/')

def login_view(request):
    print(request)
    if request.method=='GET':
         return render(request, 'login.html')
         
    email_user_input= request.POST.get('email')
    pass_user_input = request.POST.get('password')
    print(email_user_input)
    print(pass_user_input)
    username= User.objects.get(email=email_user_input)
    print(username)
    print("=="*50)
    user = authenticate(request,username=username, password=pass_user_input)
    print(user)
    if user is not None:
        login(request, user)
        return redirect('../profile/')
    else:
        return HttpResponse("Your username and password didn't match.")


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return redirect('../../../../../../')