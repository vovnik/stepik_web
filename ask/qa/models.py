from django.db import models
from  django.contrib.auth.models import User  
from django.contrib.auth.hashers import check_password

from datetime import datetime, timedelta
import random, string


def get_random_string(length):
    symbols = string.ascii_letters + string.digits
    random_str = ''.join(random.choice(symbols) for i in range(length))
    return random_str 


# Create your models here.
class QuestionManager(models.Manager):                                          
    def new(self):
        return self.order_by('-added_at')

    def popular(self):
        return self.order_by('-rating')


class Session(models.Model):
    key = models.CharField(unique=True, max_length=255)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    expires = models.DateTimeField()


class Question(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    rating = models.IntegerField(default = 0) 
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    likes = models.ManyToManyField(User, related_name='question_like_user') 
    
    objects = QuestionManager()
    

class Answer(models.Model):
    text = models.TextField()
    added_at = models.DateTimeField(blank=True, auto_now_add=True) 
    question = models.ForeignKey(Question, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User, null=True, on_delete=models.SET_NULL) 
    
    
def do_login(login, password):
    try:
        user = User.objects.get(username=login)
    except User.DoesNotExist:
        return None
    if password != user.password:
        raise Exception
        return None 
    session = Session()
    session.key = get_random_string(255)
    session.user = user
    session.expires = datetime.now() + timedelta(days=5)
    session.save()
    return session.key

