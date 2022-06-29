from multiprocessing import context
from django.shortcuts import render
from .models import *
from accounts.models import *
# Create your views here.
def index(request):
    


    context={
        "dep":department.objects.all(),
        
       
    }
    return render(request,"pages/index.html",context)


def about(request):
    d = doctor.objects.all()
    context={
        "doc":str(d.count()),
        "dep":str(department.objects.all().count()),
    }
    return render(request,"pages/about.html",context)

def departments(request):
    context={
        "dept1":department.objects.get(id=2),
        "dept2":department.objects.get(id=3),
        "dept3":department.objects.get(id=4),
        "dept4":department.objects.get(id=5),
        "dept5":department.objects.get(id=6),
    }
    return render(request,"pages/departments.html",context)

def doctor1(request):
    context={
         "doc":doctor.objects.all(),
    }
    return render(request,"pages/doctor.html",context)


def services(request):

    if request.method == "POST" and "appo" in request.POST:
        name = None
        email = None
        phone = ""
        date = ""
        dep = None
        mess = ""
        if 'name' in request.POST: name = request.POST['name']
        else: messages.error(request,"Please enter the name")
        if 'email' in request.POST: email = request.POST['email']
        else: messages.error(request,"Please enter the email")
        if 'phone' in request.POST: phone = request.POST['phone']
        else: messages.error(request,"Please enter the phone")
        if 'date' in request.POST: date = request.POST['date']
        else: messages.error(request,"Please enter the date")
        if 'department' in request.POST: dep = request.POST['department']
        else: messages.error(request,"Please enter the department")
        if 'message' in request.POST: mess = request.POST['message']
        else: messages.error(request,"Please enter the message")
       
        if name and email and phone and date and dep:
            if appointment.objects.filter(email=email).exists() and appointment.objects.filter(name=name).exists():
                messages.error(request,"The appointment has already been booked")
            else:
                if mess == "" :
                    mess = "No comment"
                app = appointment.objects.create(name=name,email=email,phone=phone,date=date,messages=mess,department_name=dep)
                app.save()
                messages.success(request,"Reservation succeeded")
        else:
            messages.error(request,"Please enter information")

    
             
    context={
         "dep":department.objects.all(),
         "doc":doctor.objects.all(),
    }
    return render(request,"pages/services.html",context)

def contact(request):
    name = None
    email = None
    subject = None
    message = None
    if request.method == "POST" and 'contact' in request.POST:
        if 'name' in request.POST: name = request.POST['name']
        else:messages.error(request,"Please enter the name")
        if 'email' in request.POST: email = request.POST['email']
        else:messages.error(request,"Please enter the email")
        if 'subject' in request.POST: subject = request.POST['subject']
        else:messages.error(request,"Please enter the subject")
        if 'message' in request.POST: message = request.POST['message']
        else:messages.error(request,"Please enter the message")

        if name and email and subject and message:
            if contact1.objects.filter(email=email).exists() and contact1.objects.filter(name=name).exists():
                messages.error(request,"The message has been posted")
            else:
                cont = contact1.objects.create(name=name,email=email,subject=subject,message=message)
                cont.save()
                messages.success(request,"Massage has been sent")
        else:
            messages.error(request,"Please enter information")


    return render(request,"pages/contact.html")    