from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login
from .models import User
def login_view(request):
    if request.method=="POST":
        username=request.POST.get("user_name")
        password=request.POST.get("password")
        if not username or not password:
            return render(request,"accounts/login.html",{"error":"All fields Required"})
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("profile")
        else:
            return render(request,"accounts/login.html",{"error":"Invalid credentials"})

    return render(request,"accounts/login.html")
 
def profile(request):
    return render(request,"accounts/profile.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("user_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        if not username or not email or not password:
            return render(request,"accounts/register.html",{"error":"All fields need to be filled"})
        if User.objects.filter(email=email).exists():
            return render(request,"accounts/register.html",{"error":"Email already exists"})
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect("login")
    return render(request,"accounts/register.html")