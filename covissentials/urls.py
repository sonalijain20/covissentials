"""covissentials URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('signup/',views.signUp),
    path('signin/',views.signIn),
    path('signout/',views.signOut),
    path('profile/', views.profile),
    path('resources/', views.resources),
    path('addresource/', views.addResource),
    path('editresource/<int:num>/', views.editResource),
    path('addcategory/',views.addCategory),
    path('display/<int:res>/<int:loc>/', views.display),
    path('delete/<int:num>/', views.deleteResource),
    path('contact/', views.contactDetails),
    path('optionsres/', views.optionsRes),
    path('optionsloc/', views.optionsLoc),
    path('donate/', views.donate),
    path('covinfo/', views.covInfo),
    path('cmfund/', views.cmFund),
    path('consult/', views.consult),

]
