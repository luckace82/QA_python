from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from . models import Question
def home(request):
    return render(request,'home.html')
def python(request):
    question_list=Question.objects.all().values()
    content={
        "question_list":question_list
    }
    return render(request,'python.html',content)