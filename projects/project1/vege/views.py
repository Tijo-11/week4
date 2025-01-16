from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import decorator_from_middleware


# Create your views here.
@login_required
def receipes(request):
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        print(receipe_name)
        print(receipe_description)
        print(receipe_image)
        
        Receipe.objects.create(receipe_name=receipe_name,
            receipe_description=receipe_description,
            receipe_image=receipe_image)
    
        return redirect('/receipes')
    
    queryset=Receipe.objects.all()
    
    if request.GET.get('search'):
        queryset=queryset.filter(receipe_name__icontains = request.GET.get('search'))
    
    
    
    
    context={'receipes':queryset}
    return render(request, 'receipes.html',context)

def delete_receipe(request, id):
    queryset= Receipe.objects.get(id = id)
    queryset.delete()
    return redirect('/receipes')

def update_receipe(request, id):
    queryset= Receipe.objects.get(id = id)
    if request.method=="POST":
        data=request.POST
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')
        receipe_image=request.FILES.get('receipe_image')
        queryset.receipe_name=receipe_name
        queryset.receipe_description=receipe_description
        queryset.receipe_image=receipe_image
        queryset.save()
        return redirect('/receipes')
    context={'receipe':queryset}
    return render(request, 'update_receipes.html',context)
    
# **********************************************************
def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        
        if not username or not password:
            messages.error(request, "Username and Password are required.")
            return redirect('/login/')
        
        if not User.objects.filter(username=username).exists():
            messages.error(request, "Invalid Username")
            return redirect('/login/')
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.error(request, "Invalid Password.")
            return redirect('/login/')
        
        login(request, user)
        return redirect('/receipes/')
    
    return render(request, 'login.html')


    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        email=request.POST.get('email')
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        user=User.objects.create(first_name=first_name, last_name=last_name, email=email,username=username)
        user.set_password(password)#to encrypt password
        if not username:
            return render(request, 'register.html', {'error': 'Username is required'})
        user.save()
        
        return redirect('/register/')
        
        
    return render(request, 'register.html' )

#*****************************************************
def logout_page(request):
    return redirect('/login/')


from django.contrib.auth.models import User
from django.contrib import messages


def register_page(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email = request.POST.get('email')
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Validate username and other required fields
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already taken')
            return redirect('/register/')
        user=User.objects.filter(email=email)
        if user.exists():
            messages.info(request,'This email is already registered')
            return redirect('/register/')

        # Create the user
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            email=email,
            password=password  # Automatically hashes the password
        )
        
        # Redirect to login or home page
        messages.info(request,"Account created Successfully")
        return redirect('/register/')  # Redirect to the login page after registration

    return render(request, 'register.html')
