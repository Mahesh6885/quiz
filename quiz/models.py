from django.db import models

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