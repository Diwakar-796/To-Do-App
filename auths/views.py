from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from auths.forms import SignUpForm

# Create your views here.

def sign_in(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hi, Welcom Back!")
            return redirect('home')
        else:
            return redirect('sign-in')
    return render(request, 'sign-in.html')

def sign_out(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect('sign-in')

@login_required
def profile(request):
    return render(request, 'profile.html')

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # messages.success(request, f"{username}, Your account created successfully.")
            return redirect('sign-in')
        else:
            return render(request, 'sign-up.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'sign-up.html', {'form': form})

