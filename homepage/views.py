from django.shortcuts import render
from accounts.models import Account
# Create your views here.
def home_screen(request):
    #print(request.headers)
    context={}
    # context['some_string']='hello this is the variable passed'
    accounts= Account.objects.all()
    context['accounts']=accounts
    return render(request, "home/home.html",context)