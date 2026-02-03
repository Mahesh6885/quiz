from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from . models import Quiz,Question,Choice,quizAttempt

from . models import Quiz,Question,Choice,quizAttempt,Category

def quiz_list(request):
    # Fetch all active quizzes
    quizzes = Quiz.objects.filter(is_active=True).select_related('category')
    return render(request, 'quiz/quiz_list.html', {'quizzes': quizzes})

def quiz_detail(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    return render(request,"quiz/quiz_detail.html",{'quiz':quiz})

@login_required(login_url='login')
def start_quiz(request,id):
    quiz=get_object_or_404(Quiz,id=id,is_active=True)
    existing_attempt = quizAttempt.objects.filter(user=request.user, quiz=quiz).first()
    if existing_attempt:
        return render(request, "quiz/result.html", {
            "quiz": quiz,
            "total": existing_attempt.total,
            "score": existing_attempt.score,
            "error_message": "You can't attempt the quiz more than once"
        })
        
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
        attempt, created = quizAttempt.objects.get_or_create(
            user=request.user,
            quiz=quiz,
            defaults={
                'total': total,
                'score': score
            }
        )

        if not created:
            attempt.total = total
            attempt.score = score
            attempt.save()
        return render(request,"quiz/result.html",{"quiz":quiz,"total":total,"score":score})
    return render(request,"quiz/question.html",{'quizs':quiz,'questions':question})

def leaderboard(request):
    categories = Category.objects.all()
    active_category_id = request.GET.get('category')
    
    if active_category_id:
        active_category = get_object_or_404(Category, id=active_category_id)
    else:
        active_category = categories.first()
        
    attempts = []
    if active_category:
        attempts = quizAttempt.objects.filter(quiz__category=active_category).select_related('user', 'quiz').order_by('-score')[:20]
            
    context = {
        'categories': categories,
        'active_category': active_category,
        'attempts': attempts
    }
    return render(request, 'quiz/leaderboard.html', context)