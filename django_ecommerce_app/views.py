from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse


# Create your views here.
def index(request):
    return render(request, "index.html")


def admin_login(request):
    return render(request, "admin_templates/login.html")


def admin_login_process(request):
    username=request.POST.get("username")
    password=request.POST.get("password")

    user=authenticate(request=request,username=username,password=password)
    if user is not None:
        login(request=request,user=user)
        return HttpResponseRedirect(reverse("admin_home"))
    else:
        messages.error(request,"Error! Please check your username and password!")
        return HttpResponseRedirect(reverse("admin_login"))


def admin_logout_process(request):
    logout(request)
    return HttpResponseRedirect(reverse("admin_login"))