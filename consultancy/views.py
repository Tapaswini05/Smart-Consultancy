from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from .models import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required



@login_required(login_url='login')
def home(request):
    context = {}
    return render(request, 'consultancy/home.html', context)

@login_required(login_url='login')
def disease(request):
    context = {}
    return render(request, 'consultancy/disease.html', context)

@login_required(login_url='login')
def consultnow(request):
    context = {}
    return render(request, 'consultancy/consultnow.html', context)

@login_required(login_url='login')
def consult(request):
    context = {}
    return render(request, 'consultancy/consult.html', context)

@login_required(login_url='login')
def derma(request):
    context = {}
    return render(request, 'consultancy/derma.html', context)

@login_required(login_url='login')
def gyno(request):
    context = {}
    return render(request, 'consultancy/gyno.html', context)

@login_required(login_url='login')
def about(request):
    context = {}
    return render(request, 'consultancy/about.html', context)


def logoutuser(request):
    logout(request)
    return redirect('login')


def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'consultancy/login.html', context)


def register(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)

                return redirect('login')

        context = {'form': form}
        return render(request, 'consultancy/register.html', context)
