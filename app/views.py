from dataclasses import field
from urllib import request
from django.shortcuts import render
from .forms import UserLogin, UserRegistration
from .models import *
from django.views.generic import View
from django.contrib import messages
from django.contrib.auth import authenticate


# Create your views here.

def index(request):
    return render(request,'index.html')

class SignUpView(View):
    def get(self,request):
        fm = UserRegistration()
        return render(request,'signup.html',{'form':fm})

    def post(self,request):
        fm=UserRegistration(request.POST)
        if fm.is_valid():
            fm.save()
            return render(request,'login.html')
        else:
            messages.error(request,'Invalid Details')
            return render(request,'signup.html')

class LoginView(View):
    frm = UserLogin()
    def get(self,request):
        return render(request,'login.html',{'form1':self.frm})
        
    def post(self,request):
        logs = UserLogin(request.POST)
        if logs.is_valid(): 
            user=authenticate(logs.cleaned_data)
            return render(request,'logged.html')




        

        # return render(request,'index.html')
    
    




