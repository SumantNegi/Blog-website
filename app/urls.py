from django.urls import path
from .import views

from .views import blogpost, blogdetail,home

urlpatterns = [
    path('',home.as_view(), name="home"),
    path('blogpost',blogpost.as_view(), name="blogpost"),
    path('addpost',views.add_blog, name="addpost"),
    path('postdetail/<slug>',blogdetail.as_view(), name="blogdetail"),
    path('about',views.about, name="about"),
    path('contact',views.contact, name="contact"),
    path('login',views.loginpage, name="login"),
    path('register',views.register, name="register"),
    path('logout',views.userlogout, name="logout"),
    path('profile',views.User_profile, name="profile"),
    path('delete/<slug>',views.user_delete, name="delete"),
    path('update/<slug>',views.update_blog, name="update"),
  

    
]

