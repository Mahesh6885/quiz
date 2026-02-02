from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from .models import User
from quiz.models import quizAttempt

def logout_view(request):
    logout(request)
    return redirect('home')

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
    attempts = quizAttempt.objects.filter(user=request.user).select_related('quiz').order_by('-created_at')
    
    total_quizzes = attempts.count()
    total_score = sum(attempt.score for attempt in attempts)
    
    context = {
        'attempts': attempts,
        'total_quizzes': total_quizzes,
        'total_score': total_score
    }
    return render(request, "accounts/profile.html", context)

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