from django.shortcuts import render,HttpResponse
from accounts.models import Account
# Create your views here.

def home_screen(request):
    #print(request.headers)
    context={}
    # context['some_string']='hello this is the variable passed'
    accounts= Account.objects.all()
    context['accounts']=accounts
    return render(request, "home/home.html",context)

def manager_screen(request):
    context={}
    if request.user.is_authenticated:
        manager_table=Account.objects.filter(manager=request.user)
        context['manager_table']=manager_table
    return render(request, "account/myteam.html",context)




