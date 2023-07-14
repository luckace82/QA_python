from django.views import View
from django.shortcuts import render
from .models import Question

class HomeView(View):

    def get(self, request):
        return render(request, 'home.html')

class PythonView(View):
    def get(self, request):
        question_list = Question.objects.all().values()
        content = {
            "question_list": question_list
        }
        return render(request, 'python.html', content)
