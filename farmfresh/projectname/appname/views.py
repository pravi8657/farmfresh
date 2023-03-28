from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.core.mail import message
from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NewUserForm

from django.contrib import messages, auth

from .models import table, okk, mla


# Create your views here.

def index(request):
    return HttpResponse('helooooooooo there')


def functionname(request):
    va = 'content'
    return render(request, 'tb.html', {'m': va})


def bg(request):
    na = table.objects.all()
    return render(request, 'tb.html', {'keyvalue': na})


def ind(request):
    ok = okk.objects.all()
    ml = mla.objects.all()
    return render(request, 'index.html', {'key': ok, 'n': ml})


# REGISTRATION

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "registration successful.")
            return redirect("login")
        messages.error(request, "unsuccessful registration. Invalid information")
    form = NewUserForm()
    return render(request=request, template_name="register.html", context={"register_form": form})


# login
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"you are now logged in as {username}.")
                return redirect("k")
            else:
                messages.error(request, "invlid username or password.")
        else:
            messages.error(request,"invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name="login.html", context={"login_form":form})

def logout(request):
    auth.logout(request)
    return redirect('login')