from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages

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

def contact(request):
    return render(request, "home/contact.html", context={})
from django.shortcuts import render

def about(request):
    # Dummy data for team members
    team_members = [
        {"name": "Raman", "role": "Project Manager"},
        {"name": "Tijo", "role": "Lead Developer"},
        {"name": "Charlie", "role": "Designer"},
    ]
    return render(request, 'home/about.html', {"team_members": team_members})
def contact(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        # Validate form data
        if not name or not email or not message:
            messages.error(request, "All fields are required.")
        else:
            # For now, just display a success message
            messages.success(request, "Thank you for contacting us!")
            # Here you could save the data to a database or send an email
        
    return render(request, "home/contact.html")
