from django.shortcuts import render
from django.http import HttpResponse

def start(request,id):
    return render(request,"index.html",{"a":id})