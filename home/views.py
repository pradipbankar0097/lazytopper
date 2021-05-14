from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def index(request):
    context = {
        'no_of_questions' : 40,
        'no_of_answers' : 35,
        'no_of_best_answers' : 12,
        'no_of_users' : 9,
        
     } 
    return render(request,'index.html',context)