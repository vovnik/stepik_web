from django import forms

from qa.models import Question, Answer, User


class SignUpForm(forms.Form):
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        return self.cleaned_data
    
    def save(self):
        user = User(username=self.cleaned_data['username'], 
                password=self.cleaned_data['password'],
                email=self.cleaned_data['email'])
        user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question = forms.IntegerField(widget=forms.HiddenInput)
    _user = None

    def clean(self):
        return self.cleaned_data
    
    def save(self, id):
        answer = Answer(question_id=id, 
                text=self.cleaned_data['text'],
                author=self._user)
        answer.save()
        return answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
    _user = None 

    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(title=self.cleaned_data['title'], 
                text=self.cleaned_data['text'],
                author=self._user)
        question.save()
        return question   

'''
from django.forms import ModelForm
from django.contrib.auth.models import User
from qa.models import Question, Answer


class AskForm(ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'text']

    def clean(self):
        return self.cleaned_data


class AnswerForm(ModelForm):
    class Meta:
        model = Answer
        fields = ['text', 'question']

    def clean(self):
        return self.cleaned_data

    def clean_question(self):
        question = self.cleaned_data['question']
        if not question:
            raise ModelForm.ValidationError
        return question 
'''

