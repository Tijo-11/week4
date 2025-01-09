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
    vegetables=['Pumpkin','Onion','Potato','Beans']
    text="""What is Lorem Ipsum?
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
    return render(request , "home/index.html", context={'people':people, 'text':text, 'vegetables':vegetables})
def about(request):
    return render(request, "home/about.html", context={})
def contact(request):
    return render(request, "home/contact.html", context={})