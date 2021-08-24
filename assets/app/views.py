from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView
from .models import post

# Create your views here.

def home (request):
    return render(request,"home.html" )

class blogpost (ListView):
    model = post
    template_name='blogpost.html'

class blogdetail(DetailView):
    model= post
    template_name='Blog-article.html'

def about (request):
    return render(request,"about.html" )

def contact (request):
    return render(request,"contact.html" )
    
def login (request):
    return render(request,"login.html" )

def register (request):
    return render(request,"register.html" )