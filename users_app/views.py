from django.shortcuts import render,redirect
#from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CustomRegisterForm
from django.contrib import messages
def register(request):
 if request.method=="POST":
   register_form=CustomRegisterForm(request.POST)
   if register_form.is_valid():  
       register_form.save()
       messages.success(request,("new user account created Login  to  get Started "))  
       #return render('todolist')
       return redirect('todolist')
 else:    
   register_form=CustomRegisterForm(request.POST)         
    #return HttpResponse('user app working ')
 return render(request,'register.html',{'register_form':register_form})

