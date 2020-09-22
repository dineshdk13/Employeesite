from django.shortcuts import render
from homepage.models import Question
# Create your views here.
def home_screen(request):
    #print(request.headers)
    context={}
    # context['some_string']='hello this is the variable passed'
    questions= Question.objects.all()
    context['questions']=questions
    return render(request, "home/home.html",context)