"""ask URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from qa.views import test, get_question_by_id, question_list, popular_question_list

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', question_list) ,
    path('login/', test),
    path('signup/', test),
    path('question/<int:id>/', get_question_by_id),
    path('ask/', test),
    path('popular/', popular_question_list),
    path('new/', test),
    ]
