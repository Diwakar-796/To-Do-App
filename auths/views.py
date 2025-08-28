from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from auths.forms import SignUpForm

# Create your views here.

def sign_in(request):
    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Hi, Welcom Back!")
            return redirect('home')
        else:
            return redirect('sign-in')
    return render(request, 'auths/sign-in.html')

def sign_out(request):
    logout(request)
    messages.success(request, "You logged out!")
    return redirect('sign-in')

@login_required
def profile(request):
    return render(request, 'auths/profile.html')

def sign_up(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('sign-in')
        else:
            return render(request, 'auths/sign-up.html', {'form': form})
    else:
        form = SignUpForm()
    return render(request, 'auths/sign-up.html', {'form': form})

def reset_password(request):
    return render(request, 'auths/reset-password.html')

