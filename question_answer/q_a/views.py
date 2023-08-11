from django.views import View
from django.shortcuts import render
from .models import Question
from .forms import QAform
from django.utils import timezone

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
class PythonansView(View):
    def get(self,request,x_id):
        ans_list=Question.objects.get(pk=x_id)
        content={
            "x":ans_list
        }
        return render(request,'pythonans.html',content)

def QA_form(request):
    form = QAform(request.POST or None)
    if form.is_valid():
        question = form.save(commit=False)  # Create an instance but don't save it yet
        question.pub_date = timezone.now()  # Set the pub_date before saving
        question.save()  # Save the instance with the pub_date set
    context = {'form': form}
    return render(request, "create.html", context)