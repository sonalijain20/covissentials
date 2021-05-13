from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    if (request.method == "POST"):
        try:
            msg = request.POST.get('search')
            c = Category.objects.get(Q(name__icontains=msg))
            r = Resource.objects.filter(Q(category_id=c.id))
            return render(request, "search.html", {"Resources": r})
        except:
            messages.error(request, "Username already exists")
            return render(request, "search.html")
    return render(request, "index.html")


def resources(request):
    return render(request, "display.html")

def signUp(request):
    if(request.method=="POST"):
        p=Provider()
        p.name=request.POST.get('name')
        p.uname=request.POST.get('uname')
        p.email=request.POST.get('email')
        p.phone=request.POST.get('phone')
        p.area=request.POST.get('area')
        p.pin=request.POST.get('pin')
        p.city=request.POST.get('city')
        p.state=request.POST.get('state')
        pword=request.POST.get('password')
        try:
            user = User.objects.create_user(username=p.uname, email=p.email, password=pword)

            p.save()
            return HttpResponseRedirect('/signin/')
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


def profile(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        try:
            p =Provider.objects.get(uname=request.user)
            if (request.method == "POST"):
                p.name = request.POST.get('name')
                p.uname = request.POST.get('uname')
                p.email = request.POST.get('email')
                p.phone = request.POST.get('phone')
                p.area = request.POST.get('area')
                p.city = request.POST.get('city')
                p.pin = request.POST.get('pin')
                p.state = request.POST.get('state')
                p.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "profile.html", {"Provider":p})
        except:
            return render(request, "profile.html")


# @login_required(login_url='/login/')
def addResource(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    category = Category.objects.all()
    if(request.method=="POST"):
        try:
            p = Provider.objects.get(uname=request.user)
            r =Resource()
            r.rname=request.POST.get('rname')
            r.avail=int(request.POST.get('avail'))
            r.category=Category.objects.get(name=request.POST.get('category'))
            r.blood_group = request.POST.get('blood')
            r.provider = p
            r.save()
            return HttpResponseRedirect('/profile/')
        except:
            return HttpResponseRedirect('/')
    return render(request,"addresource.html", {"Category": category})


# @login_required(login_url='/login/')
def editResource(request,num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        r = Resource.objects.get(id=num)
        category=Category.objects.all()
        if(request.method =="POST"):
            p = Provider.objects.get(uname=request.user)
            r.name = request.POST.get('rname')
            r.avail = request.POST.get('avail')
            r.category = Category.objects.get(name=request.POST.get('category'))
            r.blood_group = request.POST.get('blood')
            r.provider = p
            r.save()
            return HttpResponseRedirect('/profile/')
        return render(request, "editresource.html", {
                                                    "Resource": r,
                                                     "Category":category})
    except:
        return HttpResponseRedirect('/profile/')



def addCategory(request):
    if(request.method=="POST"):
        try:
            c = Category()
            c.name = request.POST.get('cat')
            c.save()
            return HttpResponseRedirect('/addresource/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addCategory.html")



def resources(request):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        try:
            p = Provider.objects.get(uname = request.user)
            r = Resource.objects.filter(provider = p)
            return render(request, "resource.html", {"Resources":r})
        except:
            return HttpResponseRedirect('/profile/')


def deleteResource(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    r = Resource.objects.get(id = num)
    r.delete()
    return HttpResponseRedirect('/resources/')


def display(request):
    r = Resource.objects.all()
    return render(request, "display.html", {"Resource": r})

def contactDetails(request):
    if(request.method=="POST"):
        c=Contact()
        c.name=request.POST.get('name')
        c.email=request.POST.get('email')
        c.subject=request.POST.get('subject')
        c.msg=request.POST.get('message')
        c.save()
        messages.success(request,"Message Sent")
        return HttpResponseRedirect('/contact/')
    return render(request,"contact-us.html")

