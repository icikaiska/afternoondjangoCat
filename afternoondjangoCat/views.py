from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegistrationForm



def home(request):
    return render(request, 'index.html')

def inner(request):
    return render(request,'inner-page.html')

def portfolio(request):
    return render(request,'portfolio-details.html')

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            form.save()
            messages.success(request, f'Account created for{username}')
            return redirect('users-registration')
    else:
        form = UserRegistrationForm()

    return render(request, 'register.html', {'form':form})