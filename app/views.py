from django.core import exceptions
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, detail
from .models import post
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from .form import blogform

# Create your views here.

class home (ListView):
    model = post
    template_name='home.html'
    ordering=['-created_at']

class blogpost (ListView):
    model = post
    template_name='blogpost.html'
    ordering=['-created_at']

class blogdetail(DetailView):
    model= post
    template_name='Blog-article.html'

def add_blog(request):
    context={ 'form': blogform }
    try:
        if request.method =='POST':
            form=blogform(request.POST)
            image=request.FILES['image']
            title=request.POST.get('title')
            desc=request.POST.get('description')
            detail=request.POST.get('detail')
            user=request.user
        
                
            if form.is_valid():
                detail=form.cleaned_data['detail']
    
            Post_obj=post.objects.create(title=title,desc=desc,image=image,detail=detail,author=user)
            Post_obj.save()
            return redirect ('blogpost')
    except Exception as e:
        print(e)    
    return render(request,"create_post.html",context)       

def about (request):
    return render(request,"about.html" )

def contact (request):
    return render(request,"contact.html" )

def User_profile (request):
    
    Post_obj =post.objects.filter(author_id=request.user)
    context={'Post_obj':Post_obj}
    return render(request,"profile.html",context )

def user_delete(request,slug):
    Post_obj=post.objects.get(slug=slug)
    Post_obj.delete()
    return redirect('profile')  

def update_blog(request, slug):
    context={}
    try:
        Post_obj=post.objects.get(slug=slug)
       

        intial_dict={'detail':Post_obj.detail,'image':Post_obj.image}
        form=blogform(initial= intial_dict)    
        if request.method =='POST':
            form=blogform(request.POST)
           
                
            if form.is_valid():
                detail=form.cleaned_data['detail']
                
            Post_obj.title=request.POST.get('title')
            Post_obj.desc=request.POST.get('description')
            Post_obj.detail=request.POST.get('detail')
            Post_obj.image=request.FILES['image']

                  
            Post_obj.save()
            return redirect('profile')
        
        context['Post_obj']=Post_obj
        context['form']=form
      
    except exceptions as e:
        print(e)
    return render (request,"update.html",context )

def loginpage (request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']
        user= authenticate(request=None,username=username,password=password)
        print(user,password)
        
        if user is not None:
            login(request,user)
            return redirect('/')
        else:
            messages.warning(request,'password or username is incorrect ! Try Again ')   
            return redirect('login') 
    else:        
        return render(request,"login.html" )

def register (request):
    if request.method=='POST':
        lname=request.POST.get('lastname')
        fname=request.POST.get('firstname')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        
        if pass1!=pass2:
            messages.warning(request,'Password does not match ! try again')
            return redirect('register') 
    
            
        elif User.objects.filter(username=uname).exists():
            messages.warning(request,'username is all ready taken')
            return redirect ('register')
            
            
        elif User.objects.filter(email=email).exists():
            messages.warning(request,'email is all ready taken')
            return redirect ('register')

            
        else:
            user= User.objects.create(first_name=fname,last_name=lname,email=email,password=pass1,username=uname)
            user.save()
            messages.success(request,'You have registered successfully')
            return redirect('login')

    else:
        return render(request,"register.html" )

def userlogout(request):
    logout(request)
    return redirect('/')       