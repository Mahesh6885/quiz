from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Quiz,Question

def quiz_list(request):
    quizes=Quiz.objects.filter(is_active=True)
    return render(request,'quiz/quiz_list.html',{'quizes':quizes})

def quiz_detail(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    return render(request,"quiz/quiz_detail.html",{'quiz':quiz})

def start_quiz(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    question=Question.objects.filter(quiz=quiz).prefetch_related('choice_set')
    return render(request,"quiz/question.html",{'quizs':quiz},{'questions':question})