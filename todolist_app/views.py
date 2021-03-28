from django.shortcuts import render,redirect
from django.http import HttpResponse
from todolist_app.models  import TaskList
from todolist_app.forms  import TaskForm
from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

def delete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
      task.delete()
    else:
      messages.error(request,("Access Restricted you are not allowed"))      
    return redirect('todolist') 
@login_required
def complete_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    if task.manage==request.user:
     task.done=True
     task.save()
    else:
      messages.error(request,("Access Restricted you are not allowed"))      
    return redirect('todolist')    
@login_required
def pending_task(request,task_id):
    task=TaskList.objects.get(pk=task_id)
    task.done=False
    task.save()
    return redirect('todolist')   
@login_required
def todolist(request):   
   if request.method=="POST":
    form=TaskForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.manage=request.user
        instance.save()
    #form.save()
    messages.success(request,'new task added!') 
    return redirect('todolist')     
   else:
    all_tasks=TaskList.objects.filter(manage=request.user)
    paginator=Paginator(all_tasks,5)
    page=request.GET.get('pg')
    all_task=paginator.get_page(page)
     # context= {'welcome_text':"welcome to todo list page"}
    return render(request,'todolist.html',{'all_task':all_task})    
def edit_task(request,task_id):
    if request.method=="POST":
     task=TaskList.objects.get(pk=task_id)
     form=TaskForm(request.POST or None, instance=task)
     if form.is_valid():
      form.save()
     messages.success(request,'task edited!') 
     return redirect('todolist')      
    else:
     task_obj=TaskList.objects.get(pk=task_id)
     # context= {'welcome_text':"welcome to todo list page"}
     return render(request,'edit.html',{'task_obj':task_obj})
@login_required     
def contact(request):    
    context= {'contact_text':"welcome to contact page"}
    return render(request,'contact.html',context)
@login_required         
def about(request):    
    context= {'about_text':"welcome to about page"}
    return render(request,'about.html',context)
    
def index(request):    
    context= {'index_text':"welcome to index page"}
    return render(request,'index.html',context)



