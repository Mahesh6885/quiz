from django.db import models
from django.conf import settings

class Category(models.Model):
    name=models.CharField(max_length=200)

    def __str__(self):
        return self.name
class Quiz(models.Model):
    category= models.ForeignKey(Category,on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description=models.TextField()
    time_limit=models.IntegerField()
    is_active=models.BooleanField(default=True)
    def __str__(self):
        return self.title
class Question(models.Model):
    quiz=models.ForeignKey(Quiz,on_delete=models.CASCADE)
    text=models.TextField()
    def __str__(self):
        return self.text
class Choice(models.Model):
    question=models.ForeignKey(Question,on_delete=models.CASCADE)
    text=models.CharField(max_length=200)
    is_correct=models.BooleanField(default=False)

    def __str__(self):
        return self.text
class quizAttempt(models.Model):
    user=models.ForeignKey(
        settings.AUTH_USER_MODEL,on_delete=models.CASCADE
    )
    quiz=models.ForeignKey(
        Quiz,on_delete=models.CASCADE
    )
    total=models.IntegerField()
    score=models.IntegerField()
    created_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        unique_together=('user','quiz')
    def __str__(self):
        return (f"{self.quiz}  total: {self.total} score: {self.score} attempted at {self.created_at}")