import imp
from django import forms
from django.contrib import messages
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
# from .forms import BankForm
from.models import Student




# Create your views here.
def home(request):
    return render(request,"home.html")


def login1(request):
    if request.method=='GET':
         return render(request,'login.html')
    elif request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        
        user=authenticate(request,username=username,password=password)
        print(user)
        if user is not None:
            print('hello',user)
            login(request,user)
            print('success')
            return render(request,'apply.html')
        else:
            messages.info(request,'invalid credentials' )
            print('failed')
            return redirect('login')



def register(request):
    if request.method=='GET':
      return render(request,'register.html')
    elif request.method=='POST':
        username=request.POST['user']
        password1=request.POST['pass1']        
        password2=request.POST['pass12'] 
        if password1==password2:
            user=User.objects.create_user(username=username,password=password1)
            
            print('usercreated')  
            return redirect('login')
        else:
            messages.info(request,'password not matching')
            return redirect('register')


def online(request):
    if request.method=="GET":
        return render(request,"form.html")
    elif request.method=="POST":
        name=request.POST['name']
        dob=request.POST['dob']
        a=request.POST['age']
        g=request.POST['gen']
        ph=request.POST['ph']
        e=request.POST['Email']
        addr=request.POST['address']
        d=request.POST['district']
        b=request.POST['branch']
        acc=request.POST['account']
        a=Student.objects.create(name=name,dob=dob,gender=g,age=a,phone=ph,email=e,address=addr,district=d,Branch=b,Accounttype=acc)
        messages.success(request,'application submitted successfully')
        return redirect('h')
        
    else:
        messages.info(request,'invalid credentials' )
        print('failed')
        return redirect('index')

    # bank=BankForm()
    # return render(request,"form.html",{'form':bank})

def logout1(request):
    logout(request)
    return redirect('/')

    
    
     
    
    

def apply(request):
    return render(request,"apply.html")

