from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task, Category, LEVEL,  User
from django.contrib import messages
from django.db.models import Q

from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
# from paypal.standard.forms import PayPalPaymentsForm

# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return render(request, 'core/home.html')
    else:
        return render(request, 'core/default.html')

@login_required
def add_task(request):
    if request.method == "POST":
        title = request.POST.get('add-task')
        category_id = request.POST.get('category')
        level = request.POST.get('level')
        category = None

        if category_id:  # only if user picked one
            category = Category.objects.get(id=category_id, user=request.user)

        if title:
            Task.objects.create(
                user=request.user,
                title=title,
                category=category,
                level = level
            )
            messages.success(request, "Task added successfully.")
        else:
            messages.warning(request, "Task can't be empty.")
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

@login_required
def filter_task(request):
    if request.method == "POST":
        category_id = request.POST.get("category")
        level = request.POST.get("level")

        if category_id == "All Tasks":
            task = Task.objects.filter(user=request.user).order_by('-level')
        else:
            task = Task.objects.filter(user=request.user, category_id=category_id).order_by('-level')

        if level == "All Tasks":
            tasks = task.filter(user=request.user)
        else:
            tasks = task.filter(user=request.user, level=level)

        return render(request, "core/home.html", {"tasks": tasks})

    return redirect("home")

@login_required
def search_task(request):
    query = request.GET.get('query')
    tasks = Task.objects.filter(
        Q(title__icontains=query) |
        Q(category__title__icontains=query) |
        Q(level__icontains=query)
    )
    return render(request, 'core/home.html', {'tasks': tasks})

@login_required
def add_category(request):
    if request.method == "POST":
        title = request.POST.get('add-category')
        if title:
            Category.objects.create(user=request.user, title=title)
            messages.success(request, "Category added successfully.")
        else:
            messages.warning(request, "Category can't be empty.")
        return redirect('home')
    return redirect('home')
