from contextlib import redirect_stderr
import email
from multiprocessing import context
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth

# Create your views here.
def signup(request):
    firstname = ""
    lastname = ""
    username = ""
    email = ""
    password = ""
    terms = None
   
    if request.method == "POST" and 'save' in request.POST:
        if 'firstname' in request.POST: firstname = request.POST['firstname']
        else: messages.error(request,"Please enter the first name")
        if 'lastname' in  request.POST: lastname = request.POST['lastname']
        else: messages.error(request,"Please enter the last name")
        if 'username' in request.POST:  username = request.POST['username']
        else: messages.error(request,"Please enter the username")
        if 'email' in request.POST:  email = request.POST['email']
        else: messages.error(request,"Please enter the email")
        if 'password' in request.POST:  password = request.POST['password']
        else: messages.error(request,"Please enter the password")
        if 'terms' in request.POST:  terms = request.POST['terms'] 
        else: messages.error(request,"Please agree to the terms")   

        if firstname and lastname and username and email and password:
            if terms == "on":
                if User.objects.filter(email=email).exists():
                    messages.error(request,"This Email is Taken")
                else:
                    if User.objects.filter(username=username).exists():
                        messages.error(request,"This username is Taken")
                    else:    
                        user = User.objects.create_user(first_name=firstname,last_name=lastname,email=email,username=username,password=password)
                        user.save()
                        messages.success(request,"Account is Create")
                        firstname = ""
                        lastname = ""
                        username = ""
                        email = ""
                        password = ""
                        return redirect('signup')   
                        
   
            else:
                messages.error(request,"Please agree to the terms") 
        else:
            messages.error(request,"Please enter the required information")
    context = {
        "firstname":firstname,
        "lastname":lastname,
        "username":username,
        "email":email,
        "password":password,
    }
    return render(request,"accounts/signup.html",context)

def login(request):
        if request.method == "POST" and "login" in request.POST:
            username = None
            password = None
            
            if 'username' in request.POST: username = request.POST['username']
            else:
                messages.error(request,"Please enter the email")
            if 'password' in request.POST: password = request.POST['password']
            else:
                messages.error(request,"Please enter the password")
            user = auth.authenticate(username=username,password=password )    
            if user is not None :
                if 'terms' not in request.POST:
                     request.session.set_expiry(0)
                auth.login(request,user)
            else:
                messages.error(request,"Please Check This Account")       
        return render(request,"accounts/login.html")

def logout(request):
    if request.user.is_authenticated:
        auth.logout(request)
    return redirect("/")           