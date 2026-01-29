from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . models import Quiz,Question,Choice,quizAttempt

def quiz_list(request):
    quizes=Quiz.objects.filter(is_active=True)
    return render(request,'quiz/quiz_list.html',{'quizes':quizes})

def quiz_detail(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    return render(request,"quiz/quiz_detail.html",{'quiz':quiz})

def start_quiz(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    question=Question.objects.filter(quiz=quiz).prefetch_related('choice_set')
    if request.method=="POST":
        total=question.count()
        score=0
        for ques in question:
            selected_c_id=request.POST.get(f"question_{ques.id}")
            if selected_c_id:
                selected_choice=Choice.objects.get(id=selected_c_id)
                if selected_choice.is_correct:
                    score+=1
        quizAttempt.objects.create(
            user=request.user,
            quiz=quiz,
            total=total,
            score=score,
        )
        return render(request,"quiz/result.html",{"quiz":quiz,"total":total,"score":score})
    return render(request,"quiz/question.html",{'quizs':quiz,'questions':question})