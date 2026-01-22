from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.contrib.auth.models import User
from .models import BlogPost
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404

def home_view(request):
    return render(request,'blogging/home.html')

def login_view(request):
    return render(request,'blogging/login.html')

def process_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard') 
        else:
            return render(request, 'blogging/login.html', {'error_message': 'Invalid credentials'})
    else:
        return redirect('login')

def signup_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        password2 = request.POST.get('password2') 
        if password != password2:
            return render(request, 'blogging/signup.html', {'error_message': 'Passwords do not match'})

        if User.objects.filter(username=username).exists():
            return render(request, 'blogging/signup.html', {'error_message': 'Username already taken'})

        user = User.objects.create_user(username=username, password=password)
        login(request, user)  
        return redirect('dashboard')  
    
    return render(request, 'blogging/signup.html')


def dashboard(request):
    blogs = BlogPost.objects.filter(author=request.user)
    return render(request, 'blogging/dashboard.html', {'blogs': blogs})

def new_blog(request):
    if request.method == "POST":
        title = request.POST.get('title')
        description = request.POST.get('description')

        BlogPost.objects.create(
            author=request.user,
            title=title,
            description=description
        )

        return redirect('dashboard')

    return render(request, 'blogging/new_blog.html')


def logout_view(request):
    logout(request)  
    return redirect('home') 

def delete_blog(request, blog_id):
    blog = get_object_or_404(
        BlogPost,
        id=blog_id,
        author=request.user
    )

    blog.delete()
    return redirect('dashboard')


def edit_blog(request, blog_id):
    blog = get_object_or_404(
        BlogPost,
        id=blog_id,
        author=request.user  
    )

    if request.method == "POST":
        blog.title = request.POST.get('title')
        blog.description = request.POST.get('description')
        blog.save()

        return redirect('dashboard')

    return render(request, 'blogging/edit_blog.html', {'blog': blog})
