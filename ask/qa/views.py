from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage
#from django.views.decorators.http import require_POST

from qa.models import Question, Answer
from qa.forms import AnswerForm, AskForm


def paginate(request, qs):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return (paginator, page)
    

def test(request, *args, **kwargs):
    return HttpResponse('OK')

def post_ask(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = f'/question/{question.id}'
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    
    return render(request, 'qa/askform.html', {
        'form': form,
        }) 
    

def get_question_by_id(request, id):
    if request.method == 'POST':
        form = AnswerForm(id, post=request.POST)
        if form.is_valid():
            post = form.save()
            url = f'/question/{id}'
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(id)
       
    question = get_object_or_404(Question, id = id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'qa/question.html', {
        'question': question,
        'answers': answers,
        'form' : form, 
        })


def question_list(request):
    questions = Question.objects.new()
    paginator, page = paginate(request, questions)
    paginator.baseurl = '/?page='
    return render(request, 'qa/question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        }) 

def popular_question_list(request):
    questions = Question.objects.popular()
    paginator, page = paginate(request, questions)
    paginator.baseurl = 'popular/?page='
    return render(request, 'qa/question_list.html', {
        'questions': page.object_list,
        'paginator': paginator,
        'page': page,
        }) 



