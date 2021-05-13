from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.models import User
from .models import *
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q

# Create your views here.

def home(request):
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    res=0
    loc=0

    if (request.method == "POST"):
        try:
            msg = request.POST.get('search')
            c = Category.objects.get(Q(name__icontains=msg))
            r1 = Resource.objects.filter(Q(category_id=c.id))
            return render(request, "search.html", {"Resources": r1,"Res": r, "Locations": l, "R":res, "L":loc })
        except:
            messages.error(request, "Username already exists")
            return render(request, "search.html")
    return render(request, "index.html", {"Res": r, "Locations": l, "R":res, "L":loc})


def resources(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    return render(request, "display.html" ,{"Res": r, "Locations": l, "R":res, "L":loc})

def signUp(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
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
            messages.success(request, "Account Created!! Please login")
            return HttpResponseRedirect('/signin/')
        except:
            messages.error(request, "Username already exists")
    return render(request, "signup.html", {"Res": r, "Locations": l, "R":res, "L":loc})


def signIn(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
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
    return render(request, "login.html",{"Res": r, "Locations": l, "R":res, "L":loc})


def signOut(request):
    auth.logout(request)
    return HttpResponseRedirect('/')


def profile(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        # try:
            p =Provider.objects.get(uname=request.user)
            if (request.method == "POST"):
                p.name = request.POST.get('name')
                p.uname = request.POST.get('uname')
                p.email = request.POST.get('email')
                p.phone = request.POST.get('phone')
                p.area = request.POST.get('area')
                p.city = request.POST.get('city')
                p.pin = request.POST.get('pin')
                # p.state = request.POST.get('state')

                p.state = State.objects.get(state=request.POST.get('state'))
                p.save()
                return HttpResponseRedirect('/profile/')
            return render(request, "profile.html", {"Provider":p, "Res": r, "Locations": l, "R":res, "L":loc})
        # except:
        #     return render(request, "profile.html", {"Provider":p, "Res": r, "Locations": l, "R":res, "L":loc})


# @login_required(login_url='/login/')
def addResource(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    category = Category.objects.all()
    state = State.objects.all()
    if(request.method=="POST"):
        # try:
            p = Provider.objects.get(uname=request.user)
            r1 =Resource()
            r1.rname=request.POST.get('rname')
            r1.avail=int(request.POST.get('avail'))
            r1.category=Category.objects.get(name=request.POST.get('category'))
            # r1.state=State.objects.get(state=request.POST.get('state'))
            r1.blood_group = request.POST.get('blood')
            r1.provider = p
            r1.save()
            return HttpResponseRedirect('/profile/')
        # except:
        #     return HttpResponseRedirect('/')
    return render(request,"addresource.html", {"Category": category, "State": state, "Res": r, "Locations": l, "R":res, "L":loc})


# @login_required(login_url='/login/')
def editResource(request,num):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    try:
        r1 = Resource.objects.get(id=num)
        category=Category.objects.all()
        if(request.method =="POST"):
            p = Provider.objects.get(uname=request.user)
            r1.name = request.POST.get('rname')
            r1.avail = request.POST.get('avail')
            r1.category = Category.objects.get(name=request.POST.get('category'))
            r1.blood_group = request.POST.get('blood')
            r1.provider = p
            r1.save()
            return HttpResponseRedirect('/profile/')
        return render(request, "editresource.html", {
                                                    "Resource": r1,
                                                     "Category":category, "Res": r, "Locations": l,
        "R":res, "L":loc})
    except:
        return HttpResponseRedirect('/profile/')



def addCategory(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    if(request.method=="POST"):
        try:
            c = Category()
            c.name = request.POST.get('cat')
            c.save()
            return HttpResponseRedirect('/addresource/')
        except:
            return HttpResponseRedirect('/')
    return render(request, "addCategory.html", {"Res": r, "Locations": l, "R":res, "L":loc})



def resources(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    else:
        try:
            p = Provider.objects.get(uname = request.user)
            r1 = Resource.objects.filter(provider = p)
            return render(request, "resource.html", {"Resources":r1, "Res": r, "Locations": l, "R":res, "L":loc})
        except:
            return HttpResponseRedirect('/profile/')


def deleteResource(request, num):
    user = User.objects.get(username=request.user)
    if (user.is_superuser):
        return HttpResponseRedirect('/admin/')
    r1 = Resource.objects.get(id = num)
    r1.delete()
    return HttpResponseRedirect('/resources/')


def display(request, res, loc ):
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')

    if (res == 0 and loc == 0):
        r1 = Resource.objects.all()
    elif( not res == 0 and  loc == 0):
        r1 = Resource.objects.filter(category=res)
        try:
            resource = Category.objects.get(id=res)
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l, "R": res, "L": loc,
                                                   "Rname": resource})
        except:
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l,
                                                    "R": res, "L": loc, })
    elif( res == 0 and not loc == 0):
        r1 = Resource.objects.filter(provider__state=loc)
        try:
            location = State.objects.get(id=loc)
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l, "R": res, "L": loc,
                                                    "Lname": location})
        except:
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l,
                                                    "R": res, "L": loc, })
    else :
        r1 = Resource.objects.filter(provider__state=loc, category=res)
        try:
            resource = Category.objects.get(id=res)
            location = State.objects.get(id=loc)
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l, "R": res, "L": loc,
                                                    "Rname": resource, "Lname": location})
        except:
            return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l,
                                                    "R": res, "L": loc,})
    return render(request, "display.html", {"Resource": r1, "Res": r, "Locations": l, "R": res, "L": loc,})


def contactDetails(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    if(request.method=="POST"):
        c=Contact()
        c.name=request.POST.get('name')
        c.email=request.POST.get('email')
        c.subject=request.POST.get('subject')
        c.msg=request.POST.get('message')
        c.save()
        messages.success(request,"Message Sent")
        return HttpResponseRedirect('/contact/')
    return render(request,"contact-us.html", {"Res": r, "Locations": l, "R":res, "L":loc})

def optionsRes(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    r1 = Category.objects.order_by('name')
    return render(request, "optionsres.html", {"Options" :r1, "Res": r, "Locations": l, "R":res, "L":loc})


def optionsLoc(request):
    res = 0
    loc = 0
    r = Category.objects.order_by('name')
    l = State.objects.order_by('state')
    r1 = State.objects.order_by('state')
    return render(request, "optionsloc.html", {"Options" :r1, "Res": r, "Locations": l, "R":res, "L":loc})


def donate(request):
    return render(request, "donate.html")

def covInfo(request):
    return render(request, "covinfo.html")

def cmFund(request):
    return render(request, "cmfund.html")

def consult(request):
    return render(request, "consult.html")

