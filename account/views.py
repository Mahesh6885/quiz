from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model

User=get_user_model()
def login(request):
    return render(request,"accounts/login.html")

def profile(request):
    return render(request,"accounts/profile.html")

def register(request):
    if request.method=="POST":
        username=request.POST.get("user_name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        user=User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )
        return redirect("login")
    return render(request,"accounts/register.html")