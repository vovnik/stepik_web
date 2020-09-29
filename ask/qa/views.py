from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.core.paginator import Paginator, EmptyPage
#from django.views.decorators.http import require_POST

from qa.models import Question, Answer, Session, do_login
from qa.forms import AnswerForm, AskForm, SignUpForm, LoginForm

from datetime import datetime, timedelta

def get_user_by_ssid(request):
    try:
        ssid = request.COOKIES.get('sessionid')
        session = Session.objects.get(
            key=ssid,
            expires__gt=datetime.now(),
        )
        user = session.user
        return user
    except:
        raise Exception
        return None 


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


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            question = form.save()
            url = '/'
            return HttpResponseRedirect(url)
    else:
        form = SignUpForm()
    return render(request, 'qa/signup.html', {
        'form': form,
        })


def login(request):
    error = ''
    if request.method == 'POST':
        login = request.POST.get('username')
        password = request.POST.get('password')
        url = '/'
        sessid = do_login(login, password)
        if sessid:
            response = HttpResponseRedirect(url)
            response.set_cookie('sessionid', sessid,
                    httponly=True,
                    expires=datetime.now()+timedelta(days=5)
                    )
            return response 
        else:
            error = 'Wrong login/password'
    form = LoginForm()
    return render(request, 'qa/login.html', {'error': error, 'form': form})

def post_question(request):
    if request.method == 'POST':
        form = AskForm(request.POST)
        form._user = get_user_by_ssid(request)
        if form.is_valid():
            question = form.save()
            url = '/question/{id}'.format(id=question.id)
            return HttpResponseRedirect(url)
    else:
        form = AskForm()
    
    return render(request, 'qa/askform.html', {
        'form': form,
        }) 
    

def question_by_id(request, id):
    if request.method == 'POST':
        form = AnswerForm(request.POST)
        form._user = get_user_by_ssid(request)
        if form.is_valid():
            post = form.save(id)
            url = '/question/{id}'.format(id=id)
            return HttpResponseRedirect(url)
    else:
        form = AnswerForm(initial={'question': id})

       
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



