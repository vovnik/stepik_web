from django.db import models
from  django.contrib.auth.models import User  

# Create your models here.

class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    rating = models.IntegerField(default = 0) 
    author = models.OneToOneField(User)
    likes = models.ManyToManyFields(User, related_name='question_like_user') 
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    question = models.OneToOne(Question)
    author = models.OneToOne(User) 
