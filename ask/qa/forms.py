from django import forms

from qa.models import Question, Answer


class AnswerForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea)
    question_id = forms.IntegerField(widget=forms.HiddenInput, required=False)
    
    def clean(self):
        return self.cleaned_data
    
    def save(self, id):
        answer = Answer(question_id=id, text=self.cleaned_data['text'])
        answer.save()
        return answer


class AskForm(forms.Form):
    title = forms.CharField()
    text = forms.CharField(widget=forms.Textarea)
     
    def clean(self):
        return self.cleaned_data

    def save(self):
        question = Question(title=self.cleaned_data['title'], text=self.cleaned_data['text'])
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

