from decimal import Decimal, InvalidOperation
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Task, Category, Donation, LEVEL,  User

from django.conf import settings
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm

# from django.template.loader import render_to_string
# from django.http import JsonResponse

# Create your views here.

def home(request):
    categories = Category.objects.all()

    if request.user.is_authenticated:
        tasks = Task.objects.filter(user=request.user).order_by('-level')
        try:
            task_done = tasks.filter(is_done=True)
        except:
            task_done = 0

        context = {
            'tasks': tasks,
            'task_done': task_done,
            'categories': categories,
            'levels': LEVEL,
        }
        
        return render(request, 'core/home.html', context)
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

        if category_id == "All Tasks":
            tasks = Task.objects.filter(user=request.user).order_by('-level')
        else:
            tasks = Task.objects.filter(user=request.user, category_id=category_id).order_by('-level')

        categories = Category.objects.filter(user=request.user)
        task_done = tasks.filter(is_done=True)

        return render(request, "core/home.html", {
            "tasks": tasks,
            "categories": categories,
            "task_done": task_done,
        })

    return redirect("home")

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

@login_required
def donate_view(request):
    if request.method == "POST":
        raw = (request.POST.get('amount') or "").strip()

        # basic validation
        if not raw:
            messages.error(request, "Please enter an amount.")
            return redirect("donate")

        try:
            amount = Decimal(raw)
        except (InvalidOperation, TypeError):
            messages.error(request, "Invalid amount.")
            return redirect("donate")

        if amount <= 0:
            messages.error(request, "Amount must be greater than 0.")
            return redirect("donate")

        # create a donation row only now (on POST with valid amount)
        donation = Donation.objects.create(user=request.user, amount=amount)

        host = request.get_host()
        paypal_dict = {
            'business': settings.PAYPAL_RECEIVER_EMAIL,
            'amount': f"{amount:.2f}",              # PayPal expects a string number
            'item_name': "Donation",
            'invoice': str(donation.id),            # unique invoice id
            'currency_code': "USD",                 # keep consistent with your UI
            'notify_url': f'http://{host}{reverse("paypal-ipn")}',
            'return_url': f'http://{host}{reverse("payment-completed")}',
            'cancel_url': f'http://{host}{reverse("payment-failed")}',
        }

        paypal_form = PayPalPaymentsForm(initial=paypal_dict, button_type="donate")

        # show a confirmation screen with the generated PayPal button
        return render(
            request,
            "core/donate.html",
            {"show_paypal": True, "paypal_payment_button": paypal_form, "amount": amount}
        )

    # GET: just show the amount form
    return render(request, "core/donate.html", {"show_paypal": False})
    
@login_required
def payment_completed_view(request):
    return render(request, 'core/payment-completed.html')

@login_required
def payment_failed_view(request):
    return render(request, 'core/payment-failed.html')
