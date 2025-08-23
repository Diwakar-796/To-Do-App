from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, User

# Create your views here.

def home(request):
    tasks = Task.objects.filter(user=request.user).order_by('-id')
    task_done = tasks.filter(is_done=True)
    context = {
        'tasks': tasks,
        'task_done': task_done,
    }
    return render(request, 'home.html', context)

@login_required
def add_task(request):
    if request.method == "POST":
        new_task = request.POST.get('add-task')
        if new_task:
            Task.objects.create(title=new_task, user=request.user)
            messages.success(request, "Task added successfully.")
        else:
            messages.error(request, "Task can't be empty.")
        return redirect('home')
    return redirect('home')

@login_required
def del_task(request):
    if request.method == "POST":
        task_id = request.POST.get('del-task')
        task = Task.objects.get(id=task_id)
        task.delete()
        messages.success(request, "Task deleted successfully.")
    else:
        messages.error(request, "Something went wrong.")
    return redirect('home')

@login_required
def done_task(request):
    if request.method == "POST":
        task_id = request.POST.get('check')
        task = Task.objects.get(id=task_id)
        if task.is_done:
            task.is_done = False
            task.save()
            messages.success(request, "Task updated successfully.")
        else:
            task.is_done = True
            task.save()
            messages.success(request, "Task updated successfully.")
    else:
        messages.error(request, "Something went wrong.")
    return redirect('home')

@login_required
def edit_task(request):
    if request.method == "POST":
        task_id = request.POST.get('task_id')
        task = Task.objects.get(id=task_id)
        new_title = request.POST.get('new-title')
        if new_title:
            task.title = new_title
            task.save()
            messages.success(request, "Task updated successfully.")
        else:
            messages.error(request, "Task can't be empty.")
        return redirect('home')
    return redirect('home')

