from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    people=[{'name':'Abhijeet','age':26},
            {'name':'Tijo','age':29},
            {'name':'Vicky','age':24},
            {'name':'Jithin','age':20},
            {'name':'Sandeep','age':17},
            {'name':'Abhishek','age':13},           
            ]
    return render(request , "home/index.html", context={'people':people})

