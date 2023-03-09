from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.contrib import messages
from app.models import Emp

# Create your views here.
def index(request):
    return render(request,"index.html")

def signup(request):
    if request.method =="POST":
        name = request.POST['name']
        contact = request.POST['contact']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        dob = request.POST['dob']
        if Emp.objects.filter(Email=email).exists():
            messages.error(request,'Email already exist')
            return redirect('/')
        elif Emp.objects.filter(Contact=contact).exists():
            messages.error(request,'Contact no already exist')
            return redirect('/')
        else:
            Emp.objects.create(Name=name,Contact=contact,Email=email,Password=password,DOB=dob)
            messages.success(request,'successfully created')
            return redirect('/')

def login(request):
    return render(request,"login.html")

def loign_check(request):
    if request.method =="POST":
        contact = request.POST['contact']       
        password =request.POST['password']
        if Emp.objects.filter(Contact=contact).exists():
            res = Emp.objects.get(Contact=contact)
            psw = res.Password
            if check_password(password,psw):
                return redirect('/table/')
            else:
                messages.success(request,'password incorrect')
                return redirect('/login/')
        else:
            messages.success(request,'Contact not exist')
            return redirect('/login/')
    
def table(request):
    data = Emp.objects.all()
    return render(request,'table.html',{'data':data})

def delete(request,uid):
    Emp.objects.filter(id=uid).delete()
    return redirect('/table/')

def update(request,uid):
    da = uid
    return render(request,'update.html',{'da':da})

def update_check(request):
    if request.method =="POST":
        name = request.POST['name']
        hide = request.POST['hide']
        contact = request.POST['contact']
        email = request.POST['email']
        password = make_password(request.POST['password'])
        dob = request.POST['dob']
        if Emp.objects.filter(Email=email).exists():
            messages.error(request,'Email already exist')
            return render(request,'update.html',{'da':hide})
        elif Emp.objects.filter(Contact=contact).exists():
            messages.error(request,'contact already exist')
            return render(request,'update.html',{'da':hide})
        else:
            Emp.objects.filter(id=hide).update(Name=name,Contact=contact,Email=email,Password=password,DOB=dob)
            messages.success(request,'successfully created')
            return redirect('/table/')