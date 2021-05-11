from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "index.html")


def signUp(request):
    if(request.method=="POST"):
        p=Provider()
        p.name=request.POST.get('name')
        p.uname=request.POST.get('uname')
        p.email=request.POST.get('email')
        p.phone=request.POST.get('contact')
        p.area=request.POST.get('area')
        p.pin=request.POST.get('pin')
        p.city=request.POST.get('city')
        p.state=request.POST.get('state')
        pword=request.POST.get('password')
        try:
            user = User.objects.create_user(username=p.uname, email=p.email, password=pword)

            p.save()
            return HttpResponseRedirect('/')
        except:
            messages.error(request, "Username already exists")
    return render(request, "signup.html", )


def signIn(request):
    if (request.method == "POST"):
        try:
            uname = request.POST.get('uname')
            pword = request.POST.get('password')
            user = auth.authenticate(username=uname, password=pword)
            if (user.is_superuser):
                return HttpResponseRedirect('/admin/')
            if (user is not None):
                auth.login(request, user)
                return HttpResponseRedirect('/')
        except:
            messages.error(request, "Invalid Username or password")
    return render(request, "login.html",)


def signOut(request):
    auth.logout(request)
    return HttpResponseRedirect('/')
