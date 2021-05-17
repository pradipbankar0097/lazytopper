from django.shortcuts import redirect, render
from django.contrib.auth import login
# Create your views here.
from django.http import HttpResponse


def base(request):
    #user='user'
    pass  
context = {
        'no_of_questions' : 40,
        'no_of_answers' : 35,
        'no_of_best_answers' : 12,
        'no_of_users' : 9,
        'user':'user',
     } 
def index(request):
    
    
    return render(request,'index.html',context)

def search(request):
    return render(request,'search.html')

def login(request):
    if request.method == "POST":
        user = request.POST['log']
        pwd = request.POST.get('pwd')
        request.session['username'] = user
        request.session['password'] = pwd
        context['user'] = user
    return render(request,'index.html',context)